# Team Member Management App

## Features
- List page, which shows all team members
- Add page, which creates a new team member
- Edit page, which updates or deletes a existing user

## Technology Stack
- Python 3.10.6=<
- Django 4.2.7
- SQLite

## Setup
0. Move to application and Python setup.
```bash
cd ./team-member-management-app/app
python -m venv .venv # This is optional.
```

1. Install requirements
```bash
pip install -r requirements.txt
```

2. Init database
```bash
python manage.py migrate
```

## Run
```bash
python manage.py runserver
```

## Test
```bash
python manage.py test
```

## Note
- When running migrate command, SQLite, `db.sqlite3` file will be created.
