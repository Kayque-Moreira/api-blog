# 🐍 Blog API Simples (Primeiro Projeto em Python)

Uma API RESTful simples desenvolvida em **Python** usando o framework **Flask** e **Flask-SQLAlchemy** para gerenciar postagens de um blog. Este projeto foi meu primeiro contato com o desenvolvimento de APIs em Python, focando na implementação de rotas CRUD e um sistema de autenticação com JWT.

## 🚀 Tecnologias Utilizadas

* **Python**
* **Flask:** Framework Web.
* **Flask-SQLAlchemy:** ORM (Object-Relational Mapping) para interagir com o banco de dados.
* **SQLite:** Banco de dados simples e leve (para fins de desenvolvimento).
* **PyJWT:** Para geração e validação de JSON Web Tokens (JWT).

## 💻 Funcionalidades da API

A API é dividida em dois Blueprints principais: **Autenticação** e **Postagens**. Todas as rotas de postagens requerem um token JWT válido.

### 🔑 Autenticação

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/auth/login` | Realiza o login do autor e retorna um **token JWT**. |

### ✍️ Postagens

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/postagens/` | Lista todas as postagens (requer token). |
| `GET` | `/postagens/<int:id>` | Obtém uma postagem específica pelo ID (requer token). |
| `POST` | `/postagens/` | Cria uma nova postagem (requer token). |
| `PUT` | `/postagens/<int:id>` | Atualiza uma postagem existente pelo ID (requer token). |
| `DELETE`| `/postagens/<int:id>`| Exclui uma postagem existente pelo ID (requer token). |

## ⚙️ Configuração e Execução

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado em seu sistema.

### Instalação das Dependências

1.  Clone este repositório:
    ```bash
    git clone [SEU_LINK_DO_REPOSITORIO]
    cd [pasta_do_projeto]
    ```

2.  Instale as bibliotecas necessárias. É altamente recomendado usar um ambiente virtual (`venv`):
    ```bash
    # Cria ambiente virtual (opcional, mas recomendado)
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate     # No Windows

    # Instala as dependências
    pip install Flask Flask-SQLAlchemy PyJWT
    ```

### Inicialização do Banco de Dados

O projeto inclui um arquivo para criar o banco de dados e um usuário administrador padrão:

1.  Execute o arquivo `banco_de_dados.py` para criar o banco de dados SQLite (`blog.db`) e inserir um usuário `admin` inicial:
    ```bash
    python banco_de_dados.py
    ```
    * **Credenciais Padrão (Admin):**
        * **Email:** `w1eak@email.com`
        * **Senha:** `123456`

### Rodando a API

1.  Execute o arquivo principal `app.py`:
    ```bash
    python app.py
    ```

2.  A API estará rodando em `http://localhost:5000`.

## 🔒 Como Usar (Fluxo de Exemplo)

1.  **Obter o Token (Login):**
    * **Endpoint:** `POST http://localhost:5000/auth/login`
    * **Body (JSON):**
        ```json
        {
            "email": "w1eak@email.com",
            "senha": "123456"
        }
        ```
    * **Resposta:** Receberá o token JWT.

2.  **Acessar uma Rota Protegida (Listar Postagens):**
    * **Endpoint:** `GET http://localhost:5000/postagens/`
    * **Header:** Adicione o cabeçalho `Authorization` com o valor do token que você recebeu.

## 🤝 Contribuições (Se aplicável no futuro)

Este é um projeto de portfólio inicial. Sugestões de melhorias ou correções de bugs são bem-vindas.

## ⭐️ Licença (Opcional, mas recomendado)

Este projeto está licenciado sob a Licença MIT.
