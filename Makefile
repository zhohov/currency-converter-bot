run:
	cd bot && poetry run python src/__main__.py

flake8:
	cd bot && poetry run flake8 --config .flake8

black:
	cd bot && poetry run black src

isort:
	cd bot && poetry run isort src

build:
	docker-compose up --build