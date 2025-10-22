# 🏨 Sistema de Gestão de Reservas Hoteleiras

Este projeto implementa um sistema básico de gestão de reservas hoteleiras, modelado em classes Python para interagir com um Banco de Dados Oracle (Oracle XE/XEPDB1).

## 🚀 Como Executar o Projeto no Linux

Siga os passos abaixo para configurar o ambiente, o banco de dados e rodar o sistema.

### Pré-requisitos

1.  **Python 3.8+** (Recomendado usar Python 3.10 ou superior).
2.  **Oracle Database** (Oracle XE, XEPDB1 ou similar) instalado e rodando localmente (endereço `localhost:1521`).
3.  **Variáveis de Ambiente Oracle** (Opcional, mas recomendado para o driver `oracledb`).

### Passo 1: Clone o Repositório

Abra o terminal e clone seu projeto:

```bash
git clone https://www.youtube.com/watch?v=351MZvGXpnY
cd trabalho_c2
```

### Passo 2: Configuração do Ambiente Python

Crie e ative um ambiente virtual para isolar as dependências do projeto.

```bash
# 1. Cria o ambiente virtual
python3 -m venv .venv

# 2. Ativa o ambiente virtual
source .venv/bin/activate 

# 3. Instala as dependências listadas no requirements.txt
pip install -r requirements.txt
```

### Passo 3: Configuração das Credenciais do Oracle

O sistema lê as credenciais de acesso ao banco de dados Oracle a partir de um arquivo específico para segurança.

1.  Crie a pasta de autenticação:

    ```bash
    mkdir -p src/conexion/passphrase
    ```

2.  Crie o arquivo de autenticação `authentication.oracle` dentro da pasta `src/conexion/passphrase/`:

    ```bash
    touch src/conexion/passphrase/authentication.oracle
    ```

3.  Edite o arquivo `authentication.oracle` e insira o seu nome de usuário e senha, separados por uma vírgula **e um espaço**, sem quebra de linha.

    **Exemplo do conteúdo de `authentication.oracle`:**

    ```
    NOME_USUARIO, SENHA_DO_USUARIO
    ```

    *(**ATENÇÃO:** O usuário e a senha devem ser os mesmos configurados para o seu banco de dados Oracle, ex: `SYSTEM, oracle`)*

### Passo 4: Inicialização do Banco de Dados

Antes de rodar o menu principal, você deve criar as tabelas e popular o banco com dados de amostra. Para isso, execute o *script* dedicado:

```bash
python3 src/create_tables_and_records.py 
```

Este script irá:

1.  Conectar ao Oracle.
2.  Executar todos os comandos DDL (`CREATE TABLE`) a partir dos arquivos SQL.
3.  Inserir os registros de amostra.

**Confirmação:** Se o processo for bem-sucedido, você verá as mensagens de *Successfully executed* no terminal.

### Passo 5: Execução do Sistema

Com o banco de dados configurado e populado, você pode iniciar o sistema principal:

```bash
python3 src/principal.py
```

O sistema irá carregar o menu de opções.

-----

## 🛠️ Estrutura do Projeto

O projeto segue a arquitetura Model-View-Controller (MVC) ou similar para organização de responsabilidades:

```
trabalho_c2/
├── sql/                        # Contém scripts SQL para relatórios e setup.
├── src/
│   ├── conexion/               # Lógica de conexão com o Oracle (OracleQueries).
│   ├── controller/             # Lógica de negócio (regras e manipulação de dados).
│   ├── model/                  # Classes de Entidades (Hospede, Quarto, Reserva, etc.).
│   ├── reports/                # Lógica para geração e exibição de relatórios.
│   └── utils/                  # Classes utilitárias (Ex: splash screen, manipulação de paths).
└── README.md
```
