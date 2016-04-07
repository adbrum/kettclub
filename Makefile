all:
	pip install -r requirements-dev.txt
	./manage.py migrate
	./manage.py loaddata */config/fixtures/*.json
	./manage.py createsuperuser --username='admin' --email=''
	./manage.py runserver