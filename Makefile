coverage: # produce coverage report
	TEST_MODE=true dotenv run pytest --cov=app tests
coverage-html: # produce HTML coverage report
	TEST_MODE=true dotenv run pytest --cov=app --cov-report=html tests
db-downgrade: # downgrade database
	dotenv run flask --app school db downgrade
db-upgrade: # upgrade database
	dotenv run flask --app school db upgrade
pip-install: # install main and dev dependencies
	pip install -r requirements.txt -r requirements-dev.txt
run: # run server in debug mode
	dotenv run flask --app school --debug run
run-no-debug: # run server in non-debug mode
	dotenv run flask --app school run
shell: # start Flask shell
	dotenv run flask --app school --debug shell
test: # run tests
	TEST_MODE=true dotenv run pytest -v tests
