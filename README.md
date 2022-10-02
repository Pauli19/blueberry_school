# Blueberry School

This project is an online school for lifelong learners.

## Getting Started

### Prerequisites:

#### Required:

- [Python 3.10.5](https://www.python.org/downloads/)
- [PostgreSQL 14](https://www.postgresql.org/download/)
- [pre-commit](https://pre-commit.com/)

#### Optional:

- [pgAdmin](https://www.pgadmin.org/download/)
- [make](https://www.gnu.org/software/make/)

### Installation

First, clone the repository:

```
git clone git@github.com:Pauli19/blueberry_school.git
```

Second, create a virtual environment inside the project's root directory:

```
cd blueberry_school
python -m venv .venv
```
Third, activate the virtual environment.

For Windows:

```
.venv\Scripts\activate.bat
```

For Mac/Linux:

```
source .venv/bin/activate
```

Fourth, install the dependencies defined in [`requirements.txt`](./requirements.txt) and [`requirements-dev.txt`](./requirements-dev.txt):

```
pip install -r requirements.txt -r requirements-dev.txt
```

Fifth, install the pre-commit script:

```
pre-commit install
```

Sixth, create a file called `.env` based on [`.env_example`](./.env_example).

```
cp .env_example .env
```

Ask for the missing values of the environment variables.

## Usage

**Note :** _make sure that the virtual environment is enabled_.

In order to run the Flask server, execute the following command:

```
dotenv run flask --app school --debug run
```

## Database Initialization

First, create two databases using PostgreSQL called `school` and `school_test`.

Second, make sure the virtual environment is enable, then create the database
schema by running the following command:

```
dotenv run flask --app school db upgrade
```

Third, start the Flask's shell:

```
dotenv run flask --app school shell
```

Fourth, inside the Flask's shell, run the script to populate the database:

```
In [1]: run scripts/populate_db.py
```


## Makefile

The following commands are available in [`Makefile`](./Makefile).

### Commands

* `coverage` - produce a coverage report
* `coverage-html` - produce an HTML coverage report
* `db-downgrade` - downgrade database
* `db-upgrade` - upgrade database
* `pip-install` - install main and dev dependencies
* `run` - run server in debug mode
* `run-no-debug` - run server in non-debug mode
* `shell` - start Flask shell
* `test` - run tests

### Execution

Before executing a command, make sure the virtual environment is active.

```
make <command-name>
```
