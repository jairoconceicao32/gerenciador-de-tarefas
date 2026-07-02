# Gerenciador de Tarefas

Projeto backend em Python focado em arquitetura em camadas, tratamento de erros estruturados e boas práticas de codificação, com o objetivo futuro de evoluir para uma API.

## Visão Geral

Sistema que gerencia tarefas, desenvolvido com foco em separação de responsabilidades, testabilidade e preparação para exposição via API.

## Arquitetura

O projeto segue uma estrutura em camadas:

- **Model** — entidades de domínio (Task, Deadline)
- **Repository** — persistência de dados (SQLite)
- **Service (Manager)** — orquestração da lógica de negócio
- **Controller** — validação de entrada e regras de aplicação
- **View** — interface com o usuário (CLI)

A conexão com o banco é injetada via construtor (dependency injection),
permitindo trocar facilmente entre banco de produção e banco de testes.

## Tratamento de Erros

O projeto utiliza uma hierarquia de exceções customizadas
(`ValidationError`, `NotFoundError`, `DatabaseError`) em vez de retornos
de erro genéricos, facilitando o mapeamento futuro para códigos de status
HTTP quando o projeto evoluir para API.

## Principais Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Remover tarefas

## Tecnologias Utilizadas

- Python — linguagem principal do projeto.
- SQLite3 — banco de dados utilizado para persistência das informações.

## Execução

Para executar o projeto, clone o repositório e rode o arquivo `app.py` pelo terminal, que é o entry point dele:

\`\`\`bash
python app.py
\`\`\`

Certifique-se de ter o Python instalado antes de rodar o comando acima. O projeto usa SQLite3, que já vem embutido no Python, então não é necessário instalar nenhuma dependência externa.

**Importante:** o comando deve ser executado a partir da raiz do projeto (a pasta onde o `app.py` está localizado), já que os imports internos dependem desse caminho para funcionar corretamente.