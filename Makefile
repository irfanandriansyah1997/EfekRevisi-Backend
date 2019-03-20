PYTHON=python
PIP=pip
PYTEST=py.test

all: env testing

env:
	cp ./etc/git-hooks/pre-commit ./.git/hooks/pre-commit
	chmod +x ./.git/hooks/pre-commit
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

testing:
	mkdir -p build/coverage
	$(PYTEST) -v --junit-xml build/test-report.xml --cov-report html:build/coverage --cov-report xml:build/coverage.xml --cov-report term-missing --cov=src -s test/ --ignore=src/generated

FORCE: