# Practice FastAPI Project (BASICS)

## Purpose

To clone and practice writing FastAPI services from scratch in Python.

## Quick Start

We must type each below commands without the help of AI.

1. Create a Python VENV

`python -m venv .venv`

2. Activate VENV

`. .venv/bin/activate`

3. Install FastAPI

`pip install fastapi`

4. Install SQLAlchemy

`pip install sqlalchemy`

5. Install Uvicorn

`pip install uvicorn`

6. Freeze Requirments

`pip freeze > requirements.txt`

7. Create 'main.py' Script

`touch app/main.py`

8. Import and make use of FastAPI to create a basic API

## Running Uvicorn

Use command as:

`uvicorn app.main:app --reload`

## BASIC DRILL #1

As an API Consumer,
I want to query the '/' root level directory of the API,
So that I can test the API works and see more details about it.

As an API Consumer,
I want to retrieve the item list and use query params to specify a limit,
So that I can view all the items existing in items list.

As an API Consumer,
I want to retrieve a specific item by specifiying the index / ID of the item,
So that I can check the value of specific items.

As an API Consumer,
I want to append items into a list,
So that I can build a list of items to perform lookups on later.

## BASIC DRILL #2

Create a SQLLITE DB using sqlalchemy

1. Make files: app/database.py and app/models.py

2. Write the database file

3. Write the models file

4. Import and init the DB in the main.py file

5. Query the DB to create, read, update, delete list item

## Hints

Check the example-*.py files only when stuck for hints!

### Finished