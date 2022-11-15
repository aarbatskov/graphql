makemigrations:
    docker-compose --env-file env_files/common.env run --rm core alembic revision --autogenerate -m "$(name)"

migrate:
    docker-compose --env-file env_files/common.env run --rm core alembic upgrade head

downgrade:
    docker-compose --env-file env_files/common.env run --rm core alembic downgrade -1
