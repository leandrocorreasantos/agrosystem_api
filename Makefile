# Caminhos
APP_DIR=src
APP_MODULE=src.main:create_flask_app
CONTAINER_APP=app
CONTAINER_DB=db

# Alembic
ALEMBIC=alembic -c $(APP_DIR)/infrastructure/db/alembic.ini

# Docker
up:
	docker-compose up -d --build

down:
	docker-compose down

logs:
	docker-compose logs -f

rebuild:
	docker-compose up -d --build --force-recreate

restart: down up

# Shell
sh:
	docker-compose exec $(CONTAINER_APP) sh

dbsh:
	docker-compose exec $(CONTAINER_DB) sh

# Alembic
migrate-init:
	$(ALEMBIC) init $(APP_DIR)/infrastructure/db/migrations

migrate:
	$(ALEMBIC) revision --autogenerate -m "auto migration"

upgrade:
	$(ALEMBIC) upgrade head

downgrade:
	$(ALEMBIC) downgrade -1

# Testes
test:
	pytest --cov=$(APP_DIR) tests/

# Reinstalar dependências
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

