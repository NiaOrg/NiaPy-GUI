# Project settings
PROJECT := NiaPy-GUI
PACKAGE := app
RESOURCES := resources
REPOSITORY := NiaOrg/NiaPy-GUI

# set python interpreter
PYTHON := python
PYTHON_VER := 3.6.7

# DEV TASKS ###################################################################
.PHONY: all
all: install

.PHONY: install
install:
	pipenv --python $(PYTHON_VER) install -d

.PHONY: run
run: check build-resources start

.PHONY: check
check:
	pipenv run flake8 app

.PHONY: build-resources
build-resources:
	pipenv run $(PYTHON) setup.py build_res

.PHONY: start
start:
	pipenv run app

# CI TASKS ####################################################################
.PHONY: ci-install
ci-install:
	pipenv run pip freeze >> requirements.txt
	pip install -r requirements.txt

# DOCS TASKS ##################################################################
.PHONY: docs
docs: cleanup build-resources
	pipenv run $(PYTHON) setup.py build_docs

# BUILD TASKS #################################################################
.PHONY: dist
dist: cleanup
	pipenv run $(PYTHON) setup.py bdist_app

# CLEAN TASKS #################################################################
.PHONY: cleanup
cleanup: .clean-resources .clean-build .clean-install

.PHONY: .clean-resources
.clean-resources:
	find $(PACKAGE) -name '*_ui.py' -delete
	find $(PACKAGE) -name '*_rc.py' -delete
	find $(RESOURCES) -name '*.qm' -delete

.PHONY: .clean-build
.clean-build:
	rm -rf dist build

.PHONY: .clean-install
.clean-install:
	find $(PACKAGE) -name '*.pyc' -delete
	find $(PACKAGE) -name '__pycache__' -delete
	rm -rf *.egg-info

# HELP ######################################################################
.PHONY: help
help: all
		@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
