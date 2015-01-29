__author__ = 'nazymko'
# !/usr/bin/python
import MySQLdb
import os

comment_separator = "-- "
db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="0000",  # your password
                     db="database")  # name of the data base


cur = db.cursor()

# Use all the SQL you like
cur.execute("SHOW TABLES")
collection = []

# collect all tables in database
for row in cur.fetchall():
    collection.append(row[0])

print collection
for table in collection:
    execute = cur.execute("show create table " + table)
    fetchall = cur.fetchall()
    print comment_separator + fetchall[0][0] + os.linesep  #table name
    print fetchall[0][1] + ";"  #create query
    print os.linesep
