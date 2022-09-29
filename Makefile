db-upgrade: # upgrade database
	dotenv run flask --app school db upgrade
db-downgrade: # downgrade database
	dotenv run flask --app school db downgrade
pip-install: # install main and dev dependencies
	pip install -r requirements.txt -r requirements-dev.txt
run: # run server in debug mode
	dotenv run flask --app school --debug run
run-no-debug: # run server in non-debug mode
	dotenv run flask --app school run
shell: # start Flask shell
	dotenv run flask --app school shell
