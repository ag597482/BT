
from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()
UsersTable = Table('users', meta,
Column('id', Integer, primary_key = True), 
Column('name', String(150)),
Column('email', String(150)),
Column('gender', String(150)), 
Column('age', Integer()))