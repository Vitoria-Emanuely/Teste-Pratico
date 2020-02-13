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
#### Instalar banco de dados do projeto:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
##### Em outro terminal:

```sh
$ cd app
$ npm install 
```

#### Para funcionar, executar o comando na venv:

```sh
$ python manage.py runserver
```

#### Para rodar o vue:

```sh
$ cd app
$ npm run serve
```
