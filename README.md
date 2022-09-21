# Blueberry School

This project is an online school for lifelong learners.

## Getting Started

### Prerequisites:

#### Required:

- [Python 3.10.5](https://www.python.org/downloads/)
- [PostgreSQL 14](https://www.postgresql.org/download/)

#### Optional:

- [pgAdmin](https://www.pgadmin.org/download/)

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

Fourth, install the dependencies defined in [`requirements.txt`](./requirements.txt):

```
pip install -r requirements.txt
```

## Usage

**Note :** _make sure that the virtual environment is enabled_.

In order to run the Flask server, execute the following command:

```
flask --debug run
```
