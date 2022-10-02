env_file:=.env_dev
db-downgrade: # downgrade database
	dotenv -f ${env_file} run flask --app school db downgrade
db-upgrade: # upgrade database
	dotenv -f ${env_file} run flask --app school db upgrade
pip-install: # install main and dev dependencies
	pip install -r requirements.txt -r requirements-dev.txt
run: # run server in debug mode
	dotenv -f .env_dev run flask --app school --debug run
run-no-debug: # run server in non-debug mode
	dotenv -f .env_dev run flask --app school run
shell: # start Flask shell
	dotenv -f .env_dev run flask --app school shell
test:
	dotenv -f .env_test run pytest -v
