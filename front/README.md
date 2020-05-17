# Conta Comigo - APP / Front

Este é um projeto que tem como propósito conectar as pessoas que estão precisando de ajuda com aquelas que tem interesse em ajudar. A ajuda pode ser desde sair com o cachorro até ir ao mercado. O foco principal é, devido ao corona vírus, evitar que pessoas do grupo de risco, e.g., idosos e pessoas com asma, pressão alta e diabetes, saiam de casa e se contaminem com o vírus.

## Tecnologias 

- Node JS
- Vue JS


## Instalação e dependências

### Dependência
Instalação das dependências do sistema:
```bash
sudo apt-get update
sudo apt-get install curl
sudo apt-get install build-essential libssl-dev
```

### Instalação
#### Node JS
Instação do NVM:
```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
```

Executando o NVM:
```bash
nvm ls-remote
```

Instalando o Node JS:
```bash
nvm install v6.11.2
```

Certificando que o Node está executando corretamente:
```bash
node -v
```

Atualizando o Node, caso precise:
```bash
npm i npm -g
```

#### Vue JS
```bash
npm install vue
```

## Execução

Abaixo você encontra as informações necessárias para executar o projeto:
 
### Vue JS

```bash
cd front
npm run serve
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your unit tests
```
npm run test:unit
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


O projeto será executado na porta **8080**

```bash
 DONE  Compiled successfully in 30282ms           5:31:52 PM


  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://192.168.0.12:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.

```
