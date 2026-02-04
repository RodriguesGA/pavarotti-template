# Pavarotti Template

Template padrão para projetos Python modernos. Use este repositório como ponto de partida para seus novos projetos.

---

## Sumário

- [O que é este template?](#o-que-é-este-template)
- [Pré-requisitos](#pré-requisitos)
- [Como usar o template (passo a passo)](#como-usar-o-template-passo-a-passo)
- [Estrutura de arquivos do template](#estrutura-de-arquivos-do-template)
  - [A pasta `utils`: funções auxiliares](#a-pasta-utils-funções-auxiliares)
  - [A pasta `scripts`: scripts auxiliares](#a-pasta-scripts-scripts-auxiliares)
- [Dicas para quem está começando](#dicas-para-quem-está-começando)
- [Resumo rápido (checklist)](#resumo-rápido-checklist)

---

## O que é este template?

O **Pavarotti Template** é um esqueleto de projeto Python já configurado com:

- **uv** para gerenciar dependências e a versão do Python
- **Ambiente virtual** (`.venv`) para isolar dependências
- **Ruff** para formatação e análise estática de código (lint)
- **Pyright** para checagem de tipos
- **Configurações do VS Code/Cursor** (formatação ao salvar, extensões recomendadas)
- **Estrutura** recomendada de pastas e arquivos para o seu projeto

---

## Pré-requisitos

Antes de usar o template, você precisa ter instalado no computador:

1. **Editor de código**

   - Recomendamos **VS Code** ou **Cursor**. O projeto já traz configurações e extensões sugeridas para eles.

2. **Extensão do Ruff**

   - Instale a extensão **Ruff** no VS Code ou no Cursor (por exemplo, pela paleta de comandos: “Extensions: Install Extensions” e busque por “Ruff”). O template usa o Ruff para formatação e análise estática do código; com a extensão, você tem realce e correções integrados ao editor.

3. **uv** (gerenciador de projetos e ambientes Python)

   - Com o **uv** instalado, você não precisa instalar nenhuma versão específica do Python: o uv baixa e gerencia a versão correta automaticamente.
   - **Como verificar:** abra um terminal e digite `uv --version`. Se aparecer a versão, o uv já está instalado.
   - **Como instalar o uv:**

     - **Via pip:** se você já tem o **pip** instalado (o pip vem junto com o Python), pode instalar o uv com:

       ```bash
       pip install uv
       ```

       É necessário ter o pip disponível no sistema; caso não tenha Python/pip instalado, use uma das opções acima (PowerShell, curl, etc.), pois o uv pode gerenciar o Python por conta própria.

     - **Windows (PowerShell):** execute no PowerShell:

       ```powershell
       powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
       ```

     - **Windows (WinGet):** `winget install --id=astral-sh.uv -e`

     - **macOS ou Linux:** execute no terminal:

       ```bash
       curl -LsSf https://astral.sh/uv/install.sh | sh
       ```

     - **macOS (Homebrew):** `brew install uv`

   - Documentação oficial: [Instalação do uv](https://docs.astral.sh/uv/getting-started/installation/).

4. **Git** (opcional, mas recomendado)
   - Para clonar o repositório e versionar seu projeto.

---

## Como usar o template (passo a passo)

### Passo 1: Obter uma cópia do template

Você pode fazer de duas formas:

**Opção A – Clonar com Git (recomendado)**  
Se o template estiver em um repositório (GitHub, GitLab, etc.):

```bash
git clone <URL_DO_REPOSITORIO_DO_TEMPLATE> my_project
cd my_project
```

Troque `my_project` pelo nome que você quer dar ao seu projeto.

**Opção B – Copiar a pasta manualmente**  
Copie toda a pasta do Pavarotti Template para o local desejado e renomeie
a pasta para o nome do seu projeto. Depois abra essa pasta no seu editor
de código.

---

### Passo 2: Configurar pyproject.toml e .python-version

Antes de criar o ambiente virtual, configure o nome do projeto e a versão do Python. São as únicas alterações obrigatórias (ou desejadas) nessa etapa. No `pyproject.toml`, as linhas a alterar são as indicadas abaixo.

#### Arquivo `.python-version`

Esse arquivo tem uma única linha com a versão do Python que o **uv** e a IDE usarão para o projeto.

- **Recomendamos a versão 3.12** (já é a padrão do template): estável e bem suportada pelas ferramentas do template (Ruff, Pyright, Pytest).
- **A escolha é livre:** se você quiser outra versão (por exemplo 3.11 ou 3.13), edite o `.python-version` e coloque apenas o número. Se mudar a versão, ajuste também o `pyproject.toml` (veja abaixo) para manter consistência.

#### Arquivo `pyproject.toml`

Nele ficam o nome do projeto, a versão do Python exigida, dependências e configurações das ferramentas. **As únicas mudanças necessárias são:**

1. **Trocar `my_project` pelo nome do seu projeto**  
   O template usa o nome genérico `my_project`. Substitua pelo nome do seu projeto (em minúsculas, sem espaços; ex.: `meu_experimento`) nas seguintes linhas do `pyproject.toml`:

   - **Linha 4:** `name = "my_project"`
   - **Linha 15:** `my_project = "my_project.main:main"` → `meu_experimento = "meu_experimento.main:main"`
   - **Linha 41:** `known-first-party = ["my_project"]` → `known-first-party = ["meu_experimento"]`

2. **Modificar a versão do Python, caso desejado**  
   Se você alterou o `.python-version` para outra versão, atualize no `pyproject.toml`:

   - **Linha 8:** `requires-python = ">=3.12"` → ex.: `">=3.11"` ou `">=3.13"`.
   - **Linha 18** (`[tool.ruff]`): `target-version = "py312"` → ex.: `"py311"` ou `"py313"`.
   - **Linha 48** (`[tool.pyright]`): `pythonVersion = "3.12"` → ex.: `"3.11"` ou `"3.13"` (mesma do `.python-version`).

Campos como `description` e `version` podem ser ajustados quando quiser; não são obrigatórios para o template funcionar.

---

### Passo 3: Criar o ambiente virtual e instalar dependências

O **uv** gerencia tudo sozinho: você não precisa ativar o ambiente virtual nem instalar o Python manualmente. Basta rodar um comando.

Na pasta do projeto, abra um terminal (no VS Code/Cursor: Terminal → Novo Terminal) e execute:

```bash
uv sync
```

ou (para ter também as dependências de desenvolvimento)

```bash
uv sync --extra dev
```

O uv lê o `.python-version`, usa ou baixa a versão do Python indicada, cria a pasta `.venv`, instala o projeto em modo editável e todas as dependências do `pyproject.toml` (incluindo as de desenvolvimento: ruff, pyright, pytest). Nos próximos passos, use sempre `uv run` para rodar comandos; ele usa o ambiente do projeto automaticamente.

Ao chamar `uv run` (por exemplo `uv run my_project` ou `uv run pytest`), o uv executa um `uv sync` automaticamente se o ambiente ainda não estiver em dia com o `pyproject.toml` e o lockfile. Assim, você não precisa lembrar de rodar `uv sync` toda vez que tiver alterado as dependências. Em outras palavras, o uv faz tudo sozinho.

---

### Passo 4: Estrutura de pastas e pacote

O `pyproject.toml` espera o código dentro de uma pasta `src` e um pacote com o mesmo nome do projeto (o nome que você definiu no Passo 2). Se ainda não existir:

- Dentro de `src`, mude o nome da pasta 'my_project' para o nome definido para o seu projeto.

Assim, o comando definido em `[project.scripts]` no `pyproject.toml` (ex.: `my_project = "my_project.main:main"`)
funcionará corretamente. Se você já ajustou `known-first-party` no Passo 2, não é preciso alterar de novo.

---

### Passo 5: Rodar o projeto

Use `uv run` para executar comandos no ambiente do projeto (não é preciso ativar o `.venv` antes):

- **Se o script estiver configurado em `[project.scripts]` no `pyproject.toml`** (ex.: `meu_experimento = "meu_experimento.main:main"`):

  ```bash
  uv run nome_do_seu_projeto
  ```

  (troque `nome_do_seu_projeto` pelo nome que você definiu em `[project.scripts]`.)

- **Para rodar um arquivo Python diretamente** (ex.: `main.py` na raiz ou dentro de `src`):

  ```bash
  uv run python main.py
  ```

  O uv usa o ambiente do projeto (`.venv`) automaticamente.

---

### Passo 6: Como adicionar dependências

Para incluir novas bibliotecas no projeto, use o **uv** na raiz do repositório:

- **Dependência de produção** (usada quando o projeto roda): `uv add nome_do_pacote`
- **Dependência de desenvolvimento** (só para desenvolvimento/testes, ex.: pytest, ruff): `uv add --dev nome_do_pacote`

O uv atualiza o `pyproject.toml` e o `uv.lock` e instala o pacote no ambiente.

**Exemplo – adicionar NumPy:**

```bash
uv add numpy
```

Depois você pode usar no código, por exemplo em `main.py` ou em um script em `scripts/`:

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.sum())  # 6
```

Para remover uma dependência: `uv remove nome_do_pacote`.

---

### Passo 7: Formatação e análise de código (Ruff)

Para formatar e verificar o código com Ruff usando o ambiente do projeto:

```bash
uv run ruff format .
uv run ruff check .
```

Para aplicar correções automáticas onde o Ruff permitir:

```bash
uv run ruff check --fix .
```

No VS Code/Cursor, com a extensão Ruff instalada e o interpretador apontando para `.venv`, o código pode ser formatado automaticamente ao salvar (conforme as configurações do projeto). Nem sempre o interpretador aponta automaticamente para o `.venv`; em alguns casos é preciso escolher manualmente:

- **Como apontar para o `.venv`:** abra a Paleta de Comandos (**Ctrl+Shift+P** ou **Cmd+Shift+P** no macOS), digite **“Python: Select Interpreter”** e selecione o interpretador que mostra o ambiente do projeto (ex.: **Python 3.12.x ('.venv': venv)**). Outra opção é clicar na versão do Python exibida na **barra de status** (canto inferior direito) e escolher o `.venv` na lista.

- **Como saber se o Ruff está funcionando:** com o interpretador correto e a extensão Ruff ativa, ao abrir um arquivo Python você verá **sublinhados ou marcados** em trechos que o Ruff sinaliza (imports não usados, estilo, etc.); ao passar o mouse, aparece a regra (ex.: “Unused import”). Se “Format on Save” estiver ligado nas configurações do projeto, ao salvar (**Ctrl+S**) o arquivo será formatado pelo Ruff. O projeto inclui um exemplo de código com erros em **`src/my_project/utils/add_wrong.py`**: abra esse arquivo e confira os avisos do linter. Os erros apontados são:

  - **Pyright (type hints):** o tipo de retorno está declarado como `-> str`, mas a função devolve `a + b` (um número). O analisador indica algo como “Expression of type \"float\" is incompatible with return type \"str\"” — o correto seria `-> float`.

  - **Ruff (RET504):** a variável `c` recebe `a + b` e em seguida é usada só no `return c`. O Ruff sinaliza que essa atribuição é desnecessária e sugere retornar diretamente: `return a + b`.

- **Por que corrigir tudo o que o Ruff (e o Pyright) apontam?** Mesmo que o código rode, vale a pena resolver todos os avisos e erros. Seguir as orientações do Ruff **facilita o desenvolvimento**: o código fica mais legível, previsível e fácil de manter; reduz bugs (imports não usados, variáveis inacessíveis, type hints incorretos); e **reduz escolhas de estilo** — todo o projeto passa a seguir as mesmas regras (aspas, quebras de linha, ordem de imports, etc.). Em resumo: tratar o Ruff como obrigatório mantém o projeto consistente e poupa tempo no longo prazo.

- **Type hints e docstrings:** o template espera o uso de **type hints** (anotações de tipo) e **docstrings** nas funções e módulos; o Ruff e o Pyright ajudam a cobrar e checar isso. **Type hints** documentam os tipos dos parâmetros e do retorno (ex.: `def add(a: float, b: float) -> float`), melhoram o autocomplete e a detecção de erros na IDE e permitem que ferramentas como o Pyright encontrem bugs antes da execução. **Docstrings** descrevem o que a função ou o módulo faz, os argumentos e o retorno em linguagem natural, facilitando a leitura e a manutenção do código e o uso por outras pessoas (ou por você no futuro). Leitura extra: [PEP 484](https://peps.python.org/pep-0484/) (Type Hints), [PEP 3107](https://peps.python.org/pep-3107/) (sintaxe de anotações) e [PEP 257](https://peps.python.org/pep-0257/) (convenções para docstrings).

---

### Passo 8: Testes (Pytest)

Os testes são **recomendados**, mas **opcionais**: você pode usar o template sem escrever testes, se preferir.

**Por que escrever testes?** **Testes unitários** verificam funções ou classes isoladas (ex.: que `add(1, 1)` retorna `2`), ajudam a garantir que cada parte do código se comporta como esperado e facilitam refatorar sem quebrar o que já funciona. **Testes de integração** verificam que várias partes do sistema funcionam juntas (ex.: que o `main` chama corretamente as funções de `utils` e produz a saída esperada). Em conjunto, testes dão confiança para alterar o código, documentam o comportamento esperado e reduzem bugs. Se quiser adotar testes no projeto, o template já está preparado.

O template está configurado para testes na pasta `tests/`, com código em `src/`. O Pytest descobre automaticamente arquivos cujo nome comece com `test_` e funções cujo nome comece com `test_`. Documentação oficial: [pytest](https://docs.pytest.org/).

1. O template já inclui o arquivo **`tests/test_add.py`** com testes para a função `add` (e para `add_wrong`; veja abaixo). Você pode usar esse arquivo como modelo para outros testes.
2. Rode os testes e observe o resultado:

   ```bash
   uv run pytest
   ```

   Todos os testes em `tests/test_add.py` devem passar. O arquivo testa tanto a função `add` (correta) quanto a função `add_wrong` (com type hint de retorno errado, em `utils/add_wrong.py`): os testes para `add_wrong` também passam, porque **em tempo de execução** as duas funções se comportam igual — ambas retornam a soma dos números. Isso ilustra que **type hints não têm influência em runtime**: o Python ignora as anotações ao executar; elas servem para ferramentas estáticas (Pyright, IDE) e para documentação. Por isso é importante corrigir os erros do linter mesmo quando “o código roda”.

Para mais detalhes na saída:

```bash
uv run pytest -v
```

---

## Estrutura de arquivos do template

Estrutura de pastas do projeto:

```text
raiz_do_projeto/
├── .gitignore
├── .python-version
├── .venv/                    # criado pelo uv, não versionado
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── pyproject.toml
├── README.md
├── scripts/                   # scripts auxiliares (gráficos, análises, etc.)
│   └── __init__.py
├── src/
│   └── <my_project>/         # pacote principal (ex.: my_project)
│       ├── __init__.py
│       ├── main.py            # ponto de entrada
│       └── utils/             # funções auxiliares reutilizáveis
│           ├── __init__.py
└── tests/
```

### Arquivos na raiz

| Item                      | Descrição                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `pyproject.toml`          | Configuração do projeto: nome, versão, dependências, Ruff, Pyright, Pytest e Setuptools.                   |
| `.python-version`         | Indica a versão do Python para o **uv** e para a IDE; o uv usa esse arquivo para criar o ambiente correto. |
| `.venv/`                  | Ambiente virtual (criado pelo **uv** com `uv sync` ou `uv venv`). Não é versionado no Git.                 |
| `.gitignore`              | Lista de arquivos e pastas que o Git deve ignorar (ex.: `__pycache__`, `.venv`).                           |
| `.vscode/settings.json`   | Configurações do workspace para VS Code/Cursor (fonte, formatação, Ruff, Python).                          |
| `.vscode/extensions.json` | Extensões recomendadas (Python, Ruff, tema Dracula, etc.).                                                 |
| `README.md`               | Este arquivo: instruções de uso do template.                                                               |

### A pasta `utils`: funções auxiliares

A pasta **`src/<projeto>/utils/`** serve para **adicionar funções auxiliares** reutilizáveis em todo o projeto. São funções que não representam a lógica principal da aplicação, mas ajudam em tarefas comuns: cálculos, formatação, leitura/escrita de arquivos, validações simples, etc.

**Como adicionar e usar uma função auxiliar (exemplo com `add`):**

1. **Crie o arquivo da função** dentro de `utils/`. Por exemplo, em `src/my_project/utils/add.py`:

   ```python
   def add(a: float, b: float) -> float:
       """Soma dois números."""
       return a + b
   ```

2. **Exportar no `__init__.py` de `utils` é opcional.** Se quiser importar com `from my_project.utils import add`, adicione em `src/my_project/utils/__init__.py`:

   ```python
   from .add import add

   __all__ = ["add"]
   ```

   Se não exportar no `__init__.py`, você pode importar direto do módulo (veja o passo 3).

3. **Importe e use no `main.py`** (ou em qualquer outro módulo do projeto). Duas formas:

   - **Se exportou no `__init__.py`:** `from my_project.utils import add`
   - **Importando direto do módulo:** `from my_project.utils.add import add`

---

### A pasta `scripts`: scripts auxiliares

A pasta **`scripts/`** (na raiz do projeto) é destinada a **scripts que realizam tarefas auxiliares**, executados sob demanda e **não** como ponto de entrada principal do projeto. Ou seja: o que roda com `uv run nome_do_projeto` é o `main.py`; os arquivos em `scripts/` são para atividades complementares.

**Exemplos do que colocar em `scripts/`:**

- **Plotar gráficos**: scripts que leem dados (CSV, banco, etc.) e geram figuras (matplotlib, seaborn, plotly).
- **Análise estatística de dados**: scripts que calculam médias, desvios, correlações, testes estatísticos, etc.
- **Pré-processamento ou export**: converter formatos, gerar relatórios, exportar resultados para planilhas ou outros sistemas.
- **Tarefas one-off**: automações pontuais, migrações de dados, geração de arquivos de configuração.

**Como executar um script em `scripts/`:**

```bash
uv run python scripts/meu_script.py
```

Se o script importar o pacote do projeto (ex.: `my_project`), o ambiente instalado pelo `uv` já deixa o pacote disponível; use `from my_project.utils import ...` dentro do script e rode com o mesmo comando trocando `meu_script.py` pelo nome do arquivo.

O template inclui o script **`scripts/add_and_print.py`** como exemplo: ele importa a função `add` de `utils`, soma dois números e imprime o resultado. **Para testar:** na raiz do projeto, execute `uv run python scripts/add_and_print.py` e confira a saída; depois abra o arquivo, altere os valores de `a` e `b` (por exemplo para `10` e `20`), salve e rode de novo para ver o resultado atualizado.

Em resumo: **`main.py`** é o coração do projeto (o que você roda no dia a dia); **`scripts/`** reúne ferramentas auxiliares como gráficos, análises e automações que você executa quando precisar.

---

### Pastas e uso recomendado

| Pasta                       | Obrigatória? | O que colocar e como usar                                                                                                                                                                                                       |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`scripts/`**              | Opcional     | Scripts auxiliares: plotar gráficos, análise estatística de dados, pré-processamento, export, automações. Rode com `uv run python scripts/meu_script.py`. Não substitui o `main.py` definido em `[project.scripts]`.            |
| **`src/<projeto>/`**        | Sim          | Pacote principal. O nome da pasta deve ser o mesmo do projeto (definido no `pyproject.toml`). Todo o código importável do projeto fica aqui.                                                                                    |
| **`src/<projeto>/main.py`** | Sim          | Ponto de entrada do projeto. É o que roda quando você executa `uv run nome_do_projeto`. Concentre aqui a orquestração e as chamadas às funções em `utils` ou outros módulos.                                                    |
| **`src/<projeto>/utils/`**  | Uso geral    | **Funções auxiliares** reutilizáveis (ex.: `add`). Crie um arquivo por função (ou grupo de funções), exporte no `utils/__init__.py` e importe no `main` ou em outros módulos com `from my_project.utils import nome_da_funcao`. |
| **`tests/`**                | Recomendado  | Testes (Pytest). Crie arquivos `test_*.py` e rode com `uv run pytest`. O `pyproject.toml` já configura `pythonpath = ["src"]` para importar o pacote.                                                                           |

---

## Dicas para quem está começando

1. **Configure o `pyproject.toml` e o `.python-version` (Passo 2)** antes de rodar `uv sync --extra dev`; assim o ambiente já nasce com o nome e a versão do Python desejados. O uv cria o `.venv` e instala todas as dependências (incluindo ruff, pytest e pyright).
2. **Prefira `uv run`** para rodar comandos (ex.: Para rodar o main do seu projeto faça `uv run my_project`, para rodar um script específico faça `uv run python path/to/script/my_script.py .`): assim você usa sempre o ambiente do projeto, sem precisar ativar o `.venv`.
3. **Para adicionar dependências**, use `uv add nome_do_pacote` (dependência normal) ou `uv add --dev nome_do_pacote` (desenvolvimento). O uv atualiza o `pyproject.toml` e o lockfile automaticamente.
4. **Aceite as extensões recomendadas** no VS Code/Cursor quando o editor sugerir, elas ajudam a manter o mesmo padrão de código.
5. **Extensão do Ruff em tempo real:** a extensão do Ruff pode ser incômoda ao apontar erros e avisos enquanto o código ainda está sendo escrito (por exemplo, imports não usados ou linhas incompletas). Se preferir, você pode **desativar a extensão** e **ativá-la só quando quiser** revisar o arquivo (via painel de extensões ou comando “Disable/Enable”), ou **usar apenas o Ruff pela linha de comando** (`uv run ruff format .` e `uv run ruff check .`) quando terminar de editar, sem a extensão instalada ou com ela desativada.
6. **Salve antes de rodar:** executar `uv run ...` no terminal **não salva** os arquivos abertos no editor. O que roda é o conteúdo já gravado em disco; se você alterou o código e não salvou, pode ver resultados inesperados ou erros que já “corrigiu” na tela. **Solução:** use sempre **Ctrl+S** (ou Cmd+S no macOS) para salvar — e, se tiver “format on save” ativo, formatar — antes de rodar comandos no terminal.

---

## Resumo rápido (checklist)

- [ ] **uv** instalado (`uv --version`)
- [ ] Cópia do template obtida (clone ou pasta copiada)
- [ ] `pyproject.toml` e `.python-version` configurados (nome do projeto e, se quiser, versão do Python)
- [ ] Ambiente e dependências instalados: `uv sync`
- [ ] Estrutura de pastas `src/my_project` e pacote com o nome do projeto
- [ ] Código de exemplo rodando (`uv run my_project`)

Se algo não funcionar como descrito aqui, consulte o responsável pelo template.
