# kettclub

Sistema de Administração para academia de ginástica

[![Build Status](https://travis-ci.org/adbrum/kettclub.svg?branch=master)](https://travis-ci.org/adbrum/kettclub)
[![Code Health](https://landscape.io/github/adbrum/kettclub/master/landscape.svg?style=flat)](https://landscape.io/github/adbrum/kettclub/master)


## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as depêndencias
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/adbrum/kettclub.git kettclub
cd kettclub
python -m venv .kett
source .kett/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY= 'python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```