# Instruções

Fazer o download do projeto em uma pasta

#### Requisitos:
- Python 3.6 (já possuir instalado)
- Vue.js (possuir instalado)
- Virtualenviroment

## Deve ser feito (Windows), através da linha de comando:

### Instalar virtualenv:
```sh
$ pip install virtualenv
```
##### Dentro do diretório em que está o projeto, criar o ambiente virtual:
```sh
$ python -m venv nome_venv
```
##### Ativar a virtualvenv (estar dentro do diretório):

```sh
$ nome_venv\Scripts\activate
```
###### Caso estiver no Windows 10 e der algum erro, executar o terminal como administrador

### Instalar o Django (dentro do ambiente virtual):

```sh
$ pip install django

$ pip install django-cors-headers

$ pip install djoser

$ pip install djangorestframework

$ pip install djangorestframework-jwt

$ pip install pylint
```

##### Garantir que a última versão do pip está instalada:

```sh
$ python -m pip install --upgrade pip
```
#### Instalar dependências do projeto:

```sh
$ python -m pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Para funcionar, executar o comando:

```sh
$ python manage.py runserver
```
### Instalar o Vue (em outra janela do terminal):

```sh
$ cd app
$ npm install vue
```
#### Para rodar:

```sh
$ cd app
$ npm run serve
```
