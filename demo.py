#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import MySQLDatabase, Model, CharField

# Connect to a MySQL database on network.
db = MySQLDatabase(
    'test',
    user='root',
    password='gb@qwer1234',
    host='192.168.40.124',
    port=3306)

db.connect()

class BModel(Model):
    class Meta:
        database = db
        import pdb
        pdb.set_trace()

class User(BModel):
    name = CharField()

print db.extract_date('t', 'a')
print db.get_tables()
print db.get_tables()
