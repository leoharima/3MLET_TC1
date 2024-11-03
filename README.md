# EmbrapAPI

Um projeto de API em Flask que possui como funcionalidade a extração de dados da Embrapa, 
como entrega do Tech Challenge da fase 1 do curso de Engenharia de Machine Learning da FIAP.

## Tech Challenge - Fase 01

Você foi contratado(a) para uma consultoria e seu trabalho envolve
analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis [aqui](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).

**Aviso**: O link pode eventualmente sofrer instabilidade por se tratar do site do
EMBRAPA. Caso isso ocorra, por gentileza, tente novamente em alguns
minutos.

A ideia do projeto é a criação de uma API pública de consulta nos dados
do site nas respectivas abas:
- **Produção**.
- **Processamento**
- **Comercialização**
- **Importação**
- **Exportação**

A API vai servir para alimentar uma base de dados que futuramente será
usada para um modelo de Machine Learning.

**Seus objetivos incluem:**

- Criar uma Rest API em Python que faça a consulta no site da Embrapa.

- Sua API deve estar documentada.

- É recomendável (não obrigatório) a escolha de um método de
autenticação (JWT, por exemplo).

- Criar um plano para fazer o deploy da API, desenhando a arquitetura
do projeto desde a ingestão até a alimentação do modelo (aqui não é
necessário elaborar um modelo de ML, mas é preciso que vocês
escolham um cenário interessante em que a API possa ser utilizada).

- Fazer um MVP realizando o deploy com um link compartilhável e um
repositório no github.

## 📁 Estrutura da Aplicação

```bash
intro_api/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── scraping_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── __init__.py
│   └── config.py
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por funcionalidades.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
  - **`utils/`**: Utilitários, como autenticação.
  - **`config.py`**: Configurações da aplicação Flask.
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências da aplicação.
- **`README.md`**: Documentação da aplicação.
- **`.gitignore`**: Arquivo com exceções para commit do repositório.

## 🛠️ Como Executar a Aplicação

### 1. Clone o Repositório

```bash
git clone https://github.com/leoharima/3MLET_TC1/
cd my_flask_app
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a Aplicação

```bash
python run.py
```

A aplicação estará disponível em `http://localhost:5000`.

## 📐 Plano de Arquitetura

![Diagrama UML](http://www.plantuml.com/plantuml/png/ZPGzRzim441t_eg3vnJUEnJvQ18Ka077Jf6Xw72XBWvXcbIFnwP5qVzU7oF8QY8QNWn9llT4YGywJu8iUUSDMeaCNnEnCVeB7px1bNSK13x2YdvaIc9CXtQB6u9P4x65I_GOBF4C_XW0W6__NOMhkEjYe23VpTyH-a2Fi2R-EU9kSt0sSgWX5rtddKLnCGpCZSUqXOlbbnhq6GKVCT50B6EI3TFwhgaXb_k3t0t0wsbPhBDqz7aiO-V2ve0IPd5FsQzZxewj4DOIUNysaELYWrk2EPJZ1sHwZZdHKStITUHTE7YkxnjOShIKKWrSe7tU8z0GSXYlVj708hRaQ-2AKlQI3c-MgNLMj-VjlLuJqfXcbJXcexxgCofuNucoDv5VaDl1CJcc-4GmolVlQE2dvrGmrOyQxZBnRvYNdQIoPwOogvPQL6hg_okA-ZegRQcWTDYleJwdaXCoKsF_K2jywQMdSNg7oG1LUVrB6AsSmJrZI4-HTsUW6szgYDhU9QagDRW0S-W3D9DZYayMgePR2iGe17tJfZAg5lqkbbebSnY0Smfjtlb_)

Um caso possível de uso dos dados provenientes desta API é a aplicação em análises e modelos preditivos (como, por exemplo, a previsão da produção de vinhos através de séries temporais ou modelos de regressão).

## 🔗 Link Compartilhável

A aplicação está implantada no link [https://embrapapi.onrender.com/](https://embrapapi.onrender.com/)

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.

## 🤝 Equipe (Grupo 20)
- Leonardo André Ferreira - RM359721
