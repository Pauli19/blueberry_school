coverage: # produce a coverage report
	TESTING=1 FLASK_DEBUG=1 dotenv run pytest --cov=app tests
coverage-html: # produce an HTML coverage report
	TESTING=1 FLASK_DEBUG=1 dotenv run pytest --cov=app --cov-report=html tests
db-downgrade: # downgrade database
	dotenv run flask --app school db downgrade
db-migrate: # autogenerates a revision script (migration), `message` must be passed.
	dotenv run flask --app school db migrate -m "$(message)"
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
test: # run tests, `file_or_dir` is optional, if not passed all tests are run.
	if [ -z "$(file_or_dir)" ]; then \
		echo "Running all tests"; \
		TESTING=1 FLASK_DEBUG=1 dotenv run pytest -v tests; \
	else \
		echo "Running $(file_or_dir)"; \
		TESTING=1 FLASK_DEBUG=1 dotenv run pytest -v "${file_or_dir}"; \
	fi
test-no-capture: # run tests disabling capturing, `file_or_dir` is optional, if not passed all tests are run.
	if [ -z "$(file_or_dir)" ]; then \
		echo "Running all tests"; \
		TESTING=1 FLASK_DEBUG=1 dotenv run pytest -v -s tests; \
	else \
		echo "Running $(file_or_dir)"; \
		TESTING=1 FLASK_DEBUG=1 dotenv run pytest -v -s "${file_or_dir}"; \
	fi
