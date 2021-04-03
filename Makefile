.PHONY: setup deps up lint test help
.DEFAULT_GOAL := help

setup:  ## Install dependencies
	poetry install

deps:  ## Update dependencies
	poetry update

up: lint  ## Start the application, assuming data.csv is in your current directory
	poetry run python app.py --filepath=data.csv

lint:  ## Run black, isort, mypy
	poetry run black .
	poetry run isort .

test: lint  ## Run unit tests
	poetry run pytest app_test.py

help:  ## Print Make usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
