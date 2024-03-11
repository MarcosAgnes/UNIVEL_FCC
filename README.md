
# Guia de Instalação e Execução da Aplicação Flask

Este guia fornece instruções detalhadas sobre como configurar e executar uma aplicação Flask simples, que inclui um formulário de cadastro de usuários e uma página para listar todos os usuários cadastrados. O projeto utiliza Flask como framework web e SQLite como banco de dados.

## Pré-requisitos

Para executar este projeto, você precisará ter o Python instalado em seu sistema. Este guia assume que você está usando o Python 3.

## Configuração do Ambiente Virtual

Recomenda-se usar um ambiente virtual para isolar as dependências do projeto. Você pode criar e ativar um ambiente virtual usando os seguintes comandos:

### Para usuários de Linux/Mac:

bashCopy code

`python3 -m venv venv source venv/bin/activate`

### Para usuários de Windows:

bashCopy code

`python -m venv venv .\venv\Scripts\activate`

## Instalação das Dependências

Após ativar o ambiente virtual, instale as dependências necessárias executando o seguinte comando:

bashCopy code

`pip install flask sqlalchemy`

## Estrutura do Projeto

Aqui está uma visão geral da estrutura básica do projeto:

bashCopy code

`/projeto-flask     /templates         cadastro.html         listagem.html     app.py`

- `app.py`: O arquivo principal do Flask que contém toda a lógica do backend.
- `templates/`: Diretório que contém os templates HTML para a aplicação.

## Executando a Aplicação

Para executar a aplicação, use o seguinte comando no terminal, certificando-se de que você está no diretório do projeto:

bashCopy code

`flask run`

Após iniciar o servidor, você pode acessar a aplicação em seu navegador através do endereço `http://localhost:5000`.

## Utilização da Aplicação

- **Cadastro de Usuários**: Acesse `http://localhost:5000` para ver o formulário de cadastro. Preencha os campos e submeta o formulário para cadastrar um novo usuário.
- **Listagem de Usuários**: Após o cadastro, você será redirecionado automaticamente para a página de listagem, que exibe todos os usuários cadastrados. Você também pode acessar essa página diretamente em `http://localhost:5000/listagem`.

## Encerrando a Aplicação

Para encerrar a aplicação, volte ao terminal e pressione `Ctrl+C`. Para desativar o ambiente virtual, use o comando `deactivate`.
