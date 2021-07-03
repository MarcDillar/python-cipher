init:
	pip install -r requirements.txt

install:
	pip install -e .

test:
	python setup.py test