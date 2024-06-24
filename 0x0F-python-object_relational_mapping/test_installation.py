#!/usr/bin/python3

import MySQLdb
import sqlalchemy

# Check mysqlclient version
try:
    print("mysqlclient version:", MySQLdb.version_info)
except AttributeError:
    print("mysqlclient version: Not available")

# Check SQLAlchemy version
print("SQLAlchemy version:", sqlalchemy.__version__)

