init:
	pip install -r requirements.txt

install:
	pip install -e .

lint:
	flake8 --extend-ignore=W605 .

build:
	python -m build

test:
	python setup.py test