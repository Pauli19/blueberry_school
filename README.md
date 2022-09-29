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

First, create the database schema by running the following command:

```
dotenv run flask --app school db upgrade
```

Second, add yourself to the list `users` in [`scripts/populate_db.py`](./scripts/populate_db.py).

Third, start the Flask's shell:

```
dotenv run flask --app school shell
```

Fourth, inside the Flask's shell, run the script to populate the database:

```
In [1]: run scripts/populate_db.py
```

Fifth, create a new branch, commit the changes adding yourself and open up a Pull Request (PR).


## Makefile

The following commands are available in [`Makefile`](./Makefile).

### Commands

* `db-upgrade` - upgrade database
* `db-downgrade` - downgrade database
* `pip-install` - install main and dev dependencies
* `run` - run server in debug mode
* `run-no-debug` - run server in non-debug mode
* `shell` - start Flask shell

### Execution

Before executing a command, make sure the virtual environment is active.

```
make <command-name>
```
