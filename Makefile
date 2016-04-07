install:
	pip install -r requirements-dev.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

test:
	python manage.py test -n

createuser:
	./manage.py createsuperuser --username='admin' --email=''

load:
	./manage.py loaddata */config/fixtures/*.json

run:
	./manage.py runserver