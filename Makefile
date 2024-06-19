default: test lint

test:
	pytest .

lint:
	pylint *.py
