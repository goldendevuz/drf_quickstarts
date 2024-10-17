env:
	python3 -m venv env && . env/bin/activate
migration:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
run:
	python3 manage.py runserver 8000
cru:
	python manage.py createsuperuser
i:
	pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt