#!/usr/bin/env python

from app import app, db

from flask_script import Manager


manager = Manager(app)


@manager.command
def create_database():
	db.create_all()


@manager.command
def drop_database():
	db.drop_all()


if __name__ == '__main__':
	manager.run()