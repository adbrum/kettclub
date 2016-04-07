# kettclub
[![Build Status](https://travis-ci.org/adbrum/kettclub.svg?branch=master)](https://travis-ci.org/adbrum/kettclub)

Python 3.5 e Django >= 1.9


## Objetivo

Sistema de Administração para academia de ginástica.

Registro de entradas dos atletas.


## Baixando e executando a app

Realize o download e execute o `setup.sh`.

```bash
wget https://raw.githubusercontent.com/adbrum/kettclub/master/setup.sh
source setup.sh
```



## Ou siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as depêndencias
5. Configure a instância com o .env
7. Execute makefile
8. Execute os testes

```bash
git clone https://github.com/adbrum/kettclub.git kettclub
cd kettclub
python -m venv .kett
source .kett/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
make
cp contrib/env-sample .env
```


## Convenções

**Título de entidades**: primeira maiúscula e no singular. Ex: *Person, Employee, Seller, Proposal, Entry*.

**Classes**: em nomes compostos maiúscula e juntas. Ex: *PersonCreate, PersonList, PersonDetail* ([PEP 8][4]).

**Funções**: nomes compostos minúsculos e separados com underline. Ex: *is_entry* ([PEP 8][4]).

**Templates**: usar a mesma convenção. Ex: *person_list.html, person_detail.html, person_form.html*.


## Como fazer o deploy para o heroku?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY= 'python contrib/secret_gen.py'
heroku config:set DEBUG=False
git push heroku master --force
```