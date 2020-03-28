# Conta Comigo - APP

Este é um projeto que tem como propósito conectar as pessoas que estão precisando de ajuda com aquelas que tem interesse em ajudar. A ajuda pode ser desde sair com o cachorro até ir ao mercado. O foco principal é, devido ao corona vírus, evitar que pessoas do grupo de risco, e.g., idosos e pessoas com asma, pressão alta e diabetes, saiam de casa e se contaminem com o vírus.

## Tecnologias 

- Python 3
- Docker
- Django
- Postgres
- Vue

## Execução

Abaixo você encontra as informações necessárias para executar o projeto em produção e a configuração do ambiente de desenvolvimento.

### Docker (Produção)

```bash
docker-compose up --build
```

O serviço será executado na porta **8000**

A documentação (Swagger) do projeto pode ser encontrada no endpoint:

> http://localhost:8000/docs/

### Montando o ambiente de desenvolvimento

Clonar o projeto no [repositório](https://github.com/maan-git/conta-comigo-app.git) e entrar no mesmo.

```bash
git clone https://github.com/maan-git/conta-comigo-app.git && cd $_
```

Você deve instalar o **pyenv** ou  **virtualenvwrapper**

Nesse [link](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation) você pode encontrar dicas de como instalar o **pyenv**.

Nesse [link](https://virtualenvwrapper.readthedocs.io/en/latest/) você pode encontar dicas de como instalar o **virtualenvwrapper**

Após instalação e ativação de sua **env** execute o comando **make install** para instalar todas as dependencias do projeto.

```bash
$ make install
```

## Executando os Testes Unitários

Para executar os testes, certifique-se de ter os requisitos de desenvolvimento instalados.

```bash
$ make test
```
