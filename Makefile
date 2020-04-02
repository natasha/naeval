
test:
	pytest -vv --pep8 --flakes naeval

wheel:
	python setup.py bdist_wheel

version:
	bumpversion minor

upload:
	twine upload dist/*

clean:
	find . \
		-name '*.pyc' \
		-o -name __pycache__ \
		-o -name .DS_Store \
		-o -name .ipynb_checkpoints \
		| xargs rm -rf
	rm -rf dist/ build/ .pytest_cache/ .cache/ \
		 *.egg-info/ .coverage
