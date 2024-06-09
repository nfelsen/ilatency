.PHONY: install clean dist publish

install:
	python setup.py install

clean:
	rm -rf build/ dist/ *.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

dist: clean
	python setup.py sdist bdist_wheel

publish: dist
	twine upload dist/*

help:
	@echo "install - Install the package"
	@echo "clean - Clean up the project"
	@echo "dist - Package distribution"
	@echo "publish - Publish the package to PyPI"
	@echo "help - Print this help message"
