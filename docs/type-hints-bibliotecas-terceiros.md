# Type hints com bibliotecas de terceiros

Este template usa o **Pyright** em modo **`strict`** (ver `[tool.pyright]` no
`pyproject.toml`). Isso significa que o analisador exige anotações completas no
**seu** código e também tenta inferir tipos em **todo** o código — inclusive
quando você importa bibliotecas externas.

Na prática, você controla os type hints das funções e módulos do projeto; o
Pyright avalia se essas anotações são coerentes com o que as bibliotecas
declaram (ou deixa de declarar). Este guia mostra como manter o projeto limpo
nos dois cenários: bibliotecas bem tipadas (ex.: NumPy) e bibliotecas com
tipagem incompleta (ex.: Matplotlib), comuns em modo strict.

---

## Sumário

- [O que o Pyright strict cobra](#o-que-o-pyright-strict-cobra)
- [Como verificar tipos no projeto](#como-verificar-tipos-no-projeto)
- [Bibliotecas com type hints: exemplo com NumPy](#bibliotecas-com-type-hints-exemplo-com-numpy)
- [Bibliotecas com tipagem incompleta: exemplo com Matplotlib](#bibliotecas-com-tipagem-incompleta-exemplo-com-matplotlib)
- [Ordem de preferência ao lidar com tipagem ausente](#ordem-de-preferência-ao-lidar-com-tipagem-ausente)
- [Referências](#referências)

---

## O que o Pyright strict cobra

Com `typeCheckingMode = "strict"`, além de exigir anotações em parâmetros e
retornos das suas funções, o Pyright tende a reportar problemas como:

| Diagnóstico                 | Significado típico                                       |
| --------------------------- | -------------------------------------------------------- |
| `reportMissingTypeStubs`    | A biblioteca não fornece stubs (`.pyi`) nem inline types |
| `reportUnknownMemberType`   | Atributo ou método de objeto com tipo desconhecido       |
| `reportUnknownArgumentType` | Argumento passado a função sem tipo inferível            |
| `reportUnknownVariableType` | Variável cujo tipo não pôde ser determinado              |

Erros desses tipos **não significam** que o código Python está errado em
runtime — significam que o analisador não consegue garantir segurança de tipos
com as informações disponíveis. O objetivo deste guia é fechar essa lacuna de
forma explícita e documentada, sem desligar o strict mode do projeto.

---

## Como verificar tipos no projeto

Na raiz do projeto:

```bash
uv run pyright
```

Corrija os diagnósticos antes de commitar, da mesma forma que você trata avisos
do Ruff. A IDE (VS Code/Cursor) usa as mesmas regras quando o interpretador
aponta para `.venv`.

---

## Bibliotecas com type hints: exemplo com NumPy

O NumPy moderno (2.x) inclui anotações de tipo e o submódulo `numpy.typing`,
que expõe aliases estáveis como `NDArray` e `ArrayLike`. Ao usar esses tipos,
você mantém compatibilidade com o Pyright strict **sem** precisar de `# type:
ignore`.

### Instalar a dependência

```bash
uv add numpy
```

### Exemplo: normalizar um vetor

Coloque funções que dependem de NumPy em um módulo do pacote (por exemplo,
`src/my_project/utils/normalize.py`):

```python
"""Utilities for normalizing NumPy arrays."""

import numpy as np
from numpy.typing import NDArray


def normalize(values: NDArray[np.float64]) -> NDArray[np.float64]:
    """Normalize a 1-D array to zero mean and unit variance.

    Args:
        values: Input array of floating-point values.

    Returns:
        Normalized array with the same shape as the input.

    """
    mean = values.mean()
    std = values.std()
    if std == 0:
        return values - mean
    return (values - mean) / std
```

Pontos importantes neste exemplo:

- **`NDArray[np.float64]`** deixa explícito que a função trabalha com arrays
  de ponto flutuante de 64 bits. O Pyright consegue validar operações como
  `.mean()` e `.std()`.
- **Entrada e saída tipadas** — o contrato da função fica claro para quem lê o
  código e para a IDE.
- **Nenhum `# type: ignore`** — a biblioteca fornece informação suficiente;
  use-a em vez de contornar o analisador.

### Alias de tipo para reduzir verbosidade

Se `NDArray[np.float64]` se repete em muitas assinaturas, defina um alias no
topo do módulo (ou em um arquivo compartilhado, como
`src/my_project/types.py`):

```python
"""Utilities for normalizing NumPy arrays."""

import numpy as np
from numpy.typing import NDArray

type FloatArray = NDArray[np.float64]


def normalize(values: FloatArray) -> FloatArray:
    """Normalize a 1-D array to zero mean and unit variance.

    Args:
        values: Input array of floating-point values.

    Returns:
        Normalized array with the same shape as the input.

    """
    mean = values.mean()
    std = values.std()
    if std == 0:
        return values - mean
    return (values - mean) / std
```

`FloatArray` é apenas um nome mais curto para o mesmo tipo — o Pyright continua
checando da mesma forma. Centralize aliases usados em vários módulos em um único
arquivo para evitar definições duplicadas.

### Aceitar entradas flexíveis com `ArrayLike`

Quando a função deve aceitar listas, tuplas ou arrays, use `ArrayLike` na
entrada e converta cedo para `NDArray`:

```python
import numpy as np
from numpy.typing import ArrayLike, NDArray

type FloatArray = NDArray[np.float64]


def as_float64_array(data: ArrayLike) -> FloatArray:
    """Convert supported array-like input to a float64 ndarray."""
    return np.asarray(data, dtype=np.float64)
```

Convertendo na borda da função, o restante do módulo opera só sobre
`FloatArray`, o que simplifica a checagem de tipos.

---

## Bibliotecas com tipagem incompleta: exemplo com Matplotlib

O **Matplotlib** é um caso frequente no dia a dia: a biblioteca funciona bem em
runtime, mas o Pyright strict costuma acusar tipos **`Unknown`** — em especial
ao usar `pyplot` (`plt.subplots()`, `ax.plot()`, `fig.savefig()`, etc.). Os
stubs existentes (`types-matplotlib`) ajudam, porém **não cobrem toda a API**.

A regra do template: **não desligue o strict mode globalmente**. Isole o
código Matplotlib e documente a decisão.

### Instalar as dependências

```bash
uv add matplotlib numpy
uv add --dev types-matplotlib
```

O pacote `types-matplotlib` reduz avisos de `reportMissingTypeStubs`, mas ainda
é comum ver `reportUnknownMemberType` ou `reportUnknownVariableType` em trechos
como o abaixo.

### Código que costuma gerar `Unknown`

Um script direto com `pyplot` — típico em `scripts/`, difícil de manter limpo
no strict mode:

```python
"""Script that plots a line chart (typical strict-mode pain points)."""

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    x = np.linspace(0, 10, 50)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)  # reportUnknownMemberType: Type of "plot" is partially unknown
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    fig.savefig("chart.png")
    plt.close(fig)
```

Problemas típicos reportados pelo Pyright:

- **`fig, ax = plt.subplots()`** — tipo de `ax` (ou de `fig`) inferido como
  `Unknown` ou parcialmente desconhecido.
- **`ax.plot(...)`** — `reportUnknownMemberType` no retorno ou nos argumentos.
- **`fig.savefig(...)`** — cadeia de tipos quebrada a partir do `subplots()`.

O restante do projeto não precisa importar `matplotlib.pyplot` diretamente;
concentre essas chamadas em um módulo dedicado (próxima seção).

---

## Ordem de preferência ao lidar com tipagem ausente

Siga esta ordem do **mais preferível** ao **último recurso**.

### 1. Instalar pacotes de stubs (`types-*`)

Antes de contornar manualmente, verifique se existe stub no
[typeshed](https://github.com/python/typeshed) ou no PyPI. Para Matplotlib:

```bash
uv add --dev types-matplotlib
```

Pacotes `types-<nome>` costumam resolver `reportMissingTypeStubs` de forma
centralizada. No Matplotlib, porém, **stubs incompletos ainda deixam passar
`Unknown`** — as opções abaixo continuam necessárias.

### 2. Encapsular atrás de funções tipadas (wrapper)

Concentre o Matplotlib em um único módulo (por exemplo,
`src/my_project/utils/plotting.py`) e exponha uma API com tipos que **você**
controla (`Path`, `FloatArray`, etc.). O restante do projeto só chama o
wrapper:

```python
"""Line-plot utilities built on Matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

type FloatArray = NDArray[np.float64]


def save_line_plot(
    x: FloatArray,
    y: FloatArray,
    output_path: Path,
    *,
    title: str = "",
    xlabel: str = "x",
    ylabel: str = "y",
) -> Path:
    """Plot y versus x and save the figure to disk.

    Args:
        x: X-axis values.
        y: Y-axis values.
        output_path: Destination file path (e.g. ``Path("out/chart.png")``).
        title: Optional plot title.
        xlabel: Label for the x-axis.
        ylabel: Label for the y-axis.

    Returns:
        The path where the figure was saved.

    """
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.savefig(output_path)
    plt.close(fig)
    return output_path
```

Vantagens:

- Scripts e `main.py` importam `save_line_plot` e não encostam em `pyplot`.
- Entrada e saída tipadas com NumPy/`Path`; o contrato fica claro fora do
  módulo de plotagem.
- Ajustes pontuais de tipo (próximos itens) ficam **só** neste arquivo.

### 3. Usar `typing.cast` quando o tipo é conhecido em runtime

Depois de `plt.subplots()`, o objeto retornado **é** um `Figure` e um `Axes`;
use `cast` para informar isso ao Pyright quando os stubs não bastam:

```python
from typing import cast

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def _create_figure() -> tuple[Figure, Axes]:
    fig, ax = plt.subplots()
    return cast(Figure, fig), cast(Axes, ax)
```

Integre no wrapper, por exemplo:

```python
fig, ax = _create_figure()
ax.plot(x, y)
```

`cast` não altera o objeto em runtime; ele informa ao analisador o tipo que
você já sabe que o Matplotlib devolve na prática.

### 4. `# pyright: ignore` ou `# type: ignore` — último recurso

Quando stubs e `cast` ainda não bastam (overload de `plot`, retorno de
`subplots` em versões antigas dos stubs, script pontual), suprima o diagnóstico
**com código específico** e comentário que explique o motivo — de preferência
**dentro do módulo wrapper**:

```python
fig, ax = plt.subplots()
ax.plot(x, y)  # pyright: ignore[reportUnknownMemberType] — stubs incompletos em plot()
```

Evite:

- `# type: ignore` sem código de erro (esconde problemas novos).
- Ignorar arquivos inteiros no `pyproject.toml` para “facilitar” — isso
  contradiz o padrão do template.
- Espalhar `# pyright: ignore` em vários módulos; mantenha-os no wrapper de
  plotagem sempre que possível.

---

## Resumo prático

| Situação                                                      | Abordagem recomendada                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| Biblioteca com tipos (NumPy, pydantic, etc.)                  | Use os tipos públicos da biblioteca (`NDArray`, modelos, etc.)        |
| Existe pacote `types-*` (ex.: `types-matplotlib`)             | `uv add --dev types-<pacote>` — pode não eliminar todo `Unknown`      |
| Biblioteca com stubs incompletos (Matplotlib), uso recorrente | Wrapper tipado em um módulo dedicado (ex.: `utils/plotting.py`)       |
| Stubs incompletos, chamada pontual no wrapper                 | `cast` para `Figure`/`Axes` ou `# pyright: ignore[código]` localizado |
| Nada mais funciona                                            | `# pyright: ignore[código]` com comentário explicativo, só no wrapper |

Mantenha **seu** código 100% anotado; trate bibliotecas de terceiros como
fronteiras onde você define contratos explícitos para o Pyright strict.

---

## Referências

- [Pyright — configuration](https://microsoft.github.io/pyright/#/configuration)
- [NumPy typing guide](https://numpy.org/doc/stable/reference/typing.html)
- [PEP 484 — Type Hints](https://peps.python.org/pep-0484/)
- [types-matplotlib](https://pypi.org/project/types-matplotlib/) — stubs de
  desenvolvimento no PyPI
- [typeshed](https://github.com/python/typeshed) — repositório de stubs da
  biblioteca padrão e pacotes `types-*`
