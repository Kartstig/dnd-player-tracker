dnd-player-tracker
===================

This is a player tracker designed to provide an API
to DM based actions to alleviate the problem in querying
player attributes and determining roll requirements

The underlying web framework is [Flask](http://flask.pocoo.org/)

## Setup (Debian/Ubuntu)

### Create virtualenv
```
$ sudo apt-get install libzmq-dev libevent-dev
$ mkvirtualenv dnd_players
$ pip install -r requirements.txt
```

### Set Configs
Copy Config.py.sample to Config.py
See [Flask Config](http://flask.pocoo.org/docs/0.10/config/)

### Run Migrations
```
$ alembic upgrade head
```
See [Alembic](http://alembic.readthedocs.org/en/latest/)
and [SQLAlchemy](http://www.sqlalchemy.org/)

### Run Server

```
$ python enginv.py runserver
```

### Workbench

```
$ python -i workbench.py
```