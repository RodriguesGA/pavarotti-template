# Pavarotti Template

Template padrão para projetos Python modernos. Use este repositório como ponto de partida para seus novos projetos.

---

## Sumário

- [O que é este template?](#o-que-é-este-template)
- [Pré-requisitos](#pré-requisitos)
- [Como usar o template (passo a passo)](#como-usar-o-template-passo-a-passo)
- [Estrutura de arquivos do template](#estrutura-de-arquivos-do-template)
- [Dicas para quem está começando](#dicas-para-quem-está-começando)
- [Resumo rápido (checklist)](#resumo-rápido-checklist)

---

## O que é este template?

O **Pavarotti Template** é um esqueleto de projeto Python já configurado com:

- **uv** para gerenciar a versão do Python e o ambiente virtual (não é preciso instalar Python manualmente)
- **Ambiente virtual** (`.venv`) para isolar dependências
- **Ruff** para formatação e análise estática de código (lint)
- **Pyright** para checagem de tipos
- **Configurações do VS Code/Cursor** (formatação ao salvar, extensões recomendadas)

---

## Pré-requisitos

Antes de usar o template, você precisa ter instalado no computador:

1. **Editor de código**

   - Recomendamos **VS Code** ou **Cursor**. O projeto já traz configurações e extensões sugeridas para eles.

2. **uv** (gerenciador de projetos e ambientes Python)

   - Com o **uv** instalado, você não precisa instalar nenhuma versão específica do Python: o uv baixa e gerencia a versão correta automaticamente.
   - **Como verificar:** abra um terminal e digite `uv --version`. Se aparecer a versão, o uv já está instalado.
   - **Como instalar o uv:**

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

3. **Git** (opcional, mas recomendado)
   - Para clonar o repositório e versionar seu projeto.
   - Verifique com `git --version`.

---

## Como usar o template (passo a passo)

### Passo 1: Obter uma cópia do template

Você pode fazer de duas formas:

**Opção A – Clonar com Git (recomendado)**  
Se o template estiver em um repositório (GitHub, GitLab, etc.):

```bash
git clone <URL_DO_REPOSITORIO_DO_TEMPLATE> meu_projeto
cd meu_projeto
```

Troque `meu_projeto` pelo nome que você quer dar ao seu projeto.

**Opção B – Copiar a pasta manualmente**  
Copie toda a pasta do Pavarotti Template para o local desejado e renomeie
a pasta para o nome do seu projeto. Depois abra essa pasta no seu editor
de código.

---

### Passo 2: Configurar pyproject.toml e .python-version

Antes de criar o ambiente virtual, configure o nome do projeto e a versão do Python. São as únicas alterações obrigatórias (ou desejadas) nessa etapa.

#### Arquivo `.python-version`

Esse arquivo tem uma única linha com a versão do Python que o **uv** e a IDE usarão para o projeto.

- **Recomendamos a versão 3.12** (já é a padrão do template): estável e bem suportada pelas ferramentas do template (Ruff, Pyright, Pytest).
- **A escolha é livre:** se você quiser outra versão (por exemplo 3.11 ou 3.13), edite o `.python-version` e coloque apenas o número, por exemplo:

  ```
  3.11
  ```

  ou

  ```
  3.13
  ```

Se mudar a versão, ajuste também o `pyproject.toml` (veja abaixo) para manter consistência.

#### Arquivo `pyproject.toml`

Nele ficam o nome do projeto, a versão do Python exigida, dependências e configurações das ferramentas. **As únicas mudanças necessárias são:**

1. **Trocar `my_project` pelo nome do seu projeto**  
   O template usa o nome genérico `my_project`. Substitua em todo o arquivo pelo nome do seu projeto (em minúsculas, sem espaços; ex.: `meu_experimento`). Os pontos principais são:

   - `name = "my_project"` → `name = "meu_experimento"`
   - `[project.scripts]`: `my_project = "my_project.main:main"` → `meu_experimento = "meu_experimento.main:main"`
   - `[tool.ruff.lint.isort]`: `known-first-party = ["my_project"]` → `known-first-party = ["meu_experimento"]`
   - Em `[tool.ruff]`: `target-version = "py312"` (use o mesmo que a versão escolhida, ex.: `"py311"` ou `"py313"`).
   - Em `[tool.pyright]`: `pythonVersion = "3.12"` (mesma versão que no `.python-version`).

2. **Modificar a versão do Python, caso desejado**  
   Se você alterou o `.python-version` para outra versão, atualize no `pyproject.toml`:
   - `requires-python = ">=3.12"` → por exemplo `">=3.11"` ou `">=3.13"`, conforme a versão que escolheu.
   - `[tool.ruff]` → `target-version = "py311"` (ou `"py313"`, etc.).
   - `[tool.pyright]` → `pythonVersion = "3.11"` (ou `"3.13"`, etc.).

Campos como `description` e `version` podem ser ajustados quando quiser; não são obrigatórios para o template funcionar.

---

### Passo 3: Criar o ambiente virtual e instalar dependências

O ambiente virtual evita misturar as bibliotecas deste projeto com as de outros. Com o **uv**, você cria o ambiente e instala tudo em um passo.

1. Abra um terminal **dentro da pasta do projeto** (no VS Code/Cursor: Terminal → Novo Terminal).

2. Crie o ambiente virtual e instale o projeto:

   ```bash
   uv sync --extra dev
   ```

   O uv vai:

   - Ler o arquivo `.python-version` e usar (ou baixar, se necessário) a versão do Python definida ali.
   - Criar a pasta `.venv` com o ambiente virtual.
   - Instalar o projeto em modo editável e todas as dependências do `pyproject.toml`, incluindo as de desenvolvimento (ruff, pyright, pytest).

   **Alternativa:** se quiser só criar o ambiente sem instalar ainda, use `uv venv`. Depois use `uv sync --extra dev` para instalar as dependências.

3. **Opcional – Ativar o ambiente virtual:**  
   Se preferir ativar o `.venv` no terminal (por exemplo, para o interpretador Python aparecer como ".venv" no editor), use:

   - **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
   - **Windows (CMD):** `.\.venv\Scripts\activate.bat`
   - **Linux/macOS:** `source .venv/bin/activate`

   Quando ativado, o início da linha do terminal costuma mostrar `(.venv)`. **Não é obrigatório ativar:** os comandos `uv run` (próximos passos) já usam o ambiente do projeto automaticamente.

---

### Passo 4: Estrutura de pastas e pacote

O `pyproject.toml` espera o código dentro de uma pasta `src` e um pacote com o mesmo nome do projeto (o nome que você definiu no Passo 2). Se ainda não existir:

- Crie a pasta `src`.
- Dentro de `src`, crie uma pasta com o nome do seu projeto (ex.: `src/meu_experimento/`).
- Mova ou recrie seu `main.py` dentro desse pacote (ex.: `src/meu_experimento/main.py`).
- Crie, se necessário, o arquivo `src/meu_experimento/__init__.py` (pode ser vazio).

Assim, o comando definido em `[project.scripts]` no `pyproject.toml` (ex.: `meu_experimento = "meu_experimento.main:main"`) funcionará corretamente. Se você já ajustou `known-first-party` no Passo 2, não é preciso alterar de novo.

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

### Passo 6: Formatação e análise de código (Ruff)

Para formatar e verificar o código com Ruff usando o ambiente do projeto:

```bash
uv run ruff format .
uv run ruff check .
```

Para aplicar correções automáticas onde o Ruff permitir:

```bash
uv run ruff check --fix .
```

(Se você tiver ativado o `.venv`, pode usar `ruff format .` e `ruff check .` diretamente.)

No VS Code/Cursor, com a extensão Ruff instalada e o interpretador apontando para `.venv`, o código pode ser formatado automaticamente ao salvar (conforme as configurações do projeto).

---

### Passo 7: Testes (Pytest)

O template está configurado para testes na pasta `tests/`, com código em `src/`.

1. Crie a pasta `tests/` na raiz do projeto (se ainda não existir).
2. Crie arquivos de teste cujo nome comece com `test_` (ex.: `tests/test_main.py`).
3. Rode os testes com o uv (usando o ambiente do projeto):

   ```bash
   uv run pytest
   ```

Para mais detalhes na saída:

```bash
uv run pytest -v
```

---

## Estrutura de arquivos do template

Estrutura de pastas do projeto:

```
raiz_do_projeto/
├── .gitignore
├── .python-version
├── .venv/                    # criado pelo uv, não versionado
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── config/
│   └── default.yaml
├── pyproject.toml
├── README.md
├── scripts/                   # opcional
│   └── __init__.py
├── src/
│   └── <my_project>/     # pacote principal (ex.: my_project)
│       ├── __init__.py
│       ├── main.py            # ponto de entrada
│       ├── cfg/               # opcional
│       ├── core/              # opcional
│       ├── schemas/           # opcional
│       ├── typing/            # opcional
│       └── utils/             # uso geral
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
| `.vscode/extensions.json` | Extensões recomendadas (Python, Ruff, Pylance, tema Dracula, etc.).                                        |
| `README.md`               | Este arquivo: instruções de uso do template.                                                               |

### Pastas e uso recomendado

| Pasta                        | Obrigatória? | O que colocar e como usar                                                                                                                                                                                                                                    |
| ---------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`config/`**                | Opcional     | Arquivos de configuração (ex.: YAML, JSON). Use para parâmetros do projeto que variam por ambiente. O `config/default.yaml` traz um exemplo de carregamento com PyYAML.                                                                                      |
| **`scripts/`**               | Opcional     | Scripts de linha de comando ou automação que **não** são o entrypoint principal do projeto (ex.: scripts de pré-processamento, export, one-offs). Rode com `uv run python scripts/meu_script.py`. Não substitui o `main.py` definido em `[project.scripts]`. |
| **`src/<projeto>/`**         | Sim          | Pacote principal. O nome da pasta deve ser o mesmo do projeto (definido no `pyproject.toml`). Todo o código importável do projeto fica aqui.                                                                                                                 |
| **`src/<projeto>/main.py`**  | Sim          | Ponto de entrada do projeto. É o que roda quando você executa `uv run nome_do_projeto`. Concentre aqui a orquestração (leitura de config, chamada da lógica em `core` ou em outros módulos).                                                                 |
| **`src/<projeto>/utils/`**   | Uso geral    | Funções e classes utilitárias reutilizáveis (formatação, I/O, helpers). Use em qualquer parte do projeto; não contém a lógica de negócio principal.                                                                                                          |
| **`src/<projeto>/core/`**    | Opcional     | Lógica central e regras de negócio do projeto. Coloque aqui o “cérebro” do experimento ou da aplicação, separado de I/O e de configuração.                                                                                                                   |
| **`src/<projeto>/cfg/`**     | Opcional     | Código de carregamento e validação de configuração (ex.: ler YAML do `config/`, expor objetos de config para o resto do projeto). Útil quando a configuração é mais que um arquivo estático.                                                                 |
| **`src/<projeto>/schemas/`** | Opcional     | Modelos e schemas **Pydantic** (validação de dados, serialização, tipos estruturados). Use quando precisar de validação forte de entradas, config ou dados entre etapas. Requer dependência `pydantic` no `pyproject.toml`.                                  |
| **`src/<projeto>/typing/`**  | Opcional     | Definições de tipos reutilizáveis que não são modelos Pydantic. Ajuda a manter type hints consistentes em todo o projeto.                                                                                                                                    |
| **`tests/`**                 | Recomendado  | Testes (Pytest). Crie arquivos `test_*.py` e rode com `uv run pytest`. O `pyproject.toml` já configura `pythonpath = ["src"]` para importar o pacote.                                                                                                        |

Pastas opcionais podem ser removidas se não forem usadas; o template inclui todas para servir de referência. **`utils`** e **`main.py`** são os pontos de uso mais geral; **`schemas`**, **`core`**, **`cfg`** e **`typing`** são para organizar projetos maiores ou com mais estrutura.

---

## Dicas para quem está começando

1. **Configure o `pyproject.toml` e o `.python-version` (Passo 2)** antes de rodar `uv sync --extra dev`; assim o ambiente já nasce com o nome e a versão do Python desejados. O uv cria o `.venv` e instala todas as dependências (incluindo ruff, pytest e pyright).
2. **Prefira `uv run`** para rodar comandos (ex.: Para rodar o main do seu projeto faça `uv run my_project`, para rodar um script específico faça `uv run python path/to/script/my_script.py .`): assim você usa sempre o ambiente do projeto, sem precisar ativar o `.venv`.
3. **Para adicionar dependências**, use `uv add nome_do_pacote` (dependência normal) ou `uv add --dev nome_do_pacote` (desenvolvimento). O uv atualiza o `pyproject.toml` e o lockfile automaticamente. Depois, outros pesquisadores só precisam rodar `uv sync` para ficar igual.
4. **Aceite as extensões recomendadas** no VS Code/Cursor quando o editor sugerir; elas ajudam a manter o mesmo padrão de código.
5. **Rode `uv run ruff format .` e `uv run ruff check .`** de vez em quando (ou confie no “format on save”) para manter o estilo consistente.

---

## Resumo rápido (checklist)

- [ ] **uv** instalado (`uv --version`)
- [ ] Cópia do template obtida (clone ou pasta copiada)
- [ ] `pyproject.toml` e `.python-version` configurados (nome do projeto e, se quiser, versão do Python)
- [ ] Ambiente e dependências instalados: `uv sync`
- [ ] Estrutura de pastas `src/my_project` e pacote com o nome do projeto
- [ ] Código de exemplo rodando (`uv run my_project`)

Se algo não funcionar como descrito aqui, consulte o responsável pelo template.
