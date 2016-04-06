all:
	python manage.py migrate
	python manage.py loaddata */config/fixtures/*.json