init:
	pip install -r requirements.txt

install:
	pip install -e .

build:
	python -m build

test:
	python setup.py test