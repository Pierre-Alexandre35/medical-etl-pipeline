lint: ## Lint using flake8
	flake8 pipeline


unit: # run unit tests
	python -m pytest ./tests/unit

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t .

build-nc: ## Build the container without caching
	docker build --no-cache -t .

run: ## Run container on port configured in `config.env`
