db-upgrade: # upgrades the database
	dotenv run flask db upgrade
pip-install: # install main and dev dependencies
	pip install -r requirements.txt -r requirements-dev.txt
run: # run server in debug mode
	dotenv run flask --debug run
run-no-debug: # run server in non-debug mode
	dotenv run flask run
shell: # start flask shell
	dotenv run flask shell
