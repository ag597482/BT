from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData
from models.user import Person
from sqlalchemy.orm import sessionmaker
from clients.tables_structure import UsersTable
import itertools


class MySQLClient():

    def __init__(self, user, password, host, database):
        self.meta = MetaData()
        self.engine = create_engine(f'mysql://{user}:{password}@{host}/{database}', echo = True)
        self.conn = self.engine.connect()
        self.session = sessionmaker(bind = self.engine)()
        # self.meta.create_all(self.engine)

    def insert_user(self, user = Person):
        print(user.name + " details to be inserted in table")
        ins = UsersTable.insert().values(name = user.name, 
        email = user.email, 
        gender = user.gender,
        age = user.age)
        self.conn.execute(ins)
        # self.session.add(user)
        # self.session.commit()

    # def __repr__(self):
    #     return str(vars(self))
    
    def update_user(self):
        result = self.session.query(UsersTable).offset(0).limit(2).all()
        print(result)
        # r = []
        # for res in result:
        #     y = list(res)
        #     y[4] = 2*res['age']
        #     r.append(tuple(y))
        #     res = tuple(y)
        # print("RRRR")
        # print(r)
        # stmt = UsersTable.update().values(result)
        # self.conn.execute(stmt)

    def read_users(self):
        print(self.session.query(UsersTable))
        result = self.session.query(UsersTable).filter(UsersTable.columns[1] == 'John').all()
        print(result[0])
        return result
        # print(result[0].age)
        # print(result)
        # print("@@")
        # print(UsersTable.columns)
        # result = self.session.query(UsersTable).filter(UsersTable.name == 'users' and UsersTable.columns[1] == 'John').all()
        # print(result)
        # p1 = result[0]
        # p1 = result[0]
        # print(p1.name )
        # out = list(itertools.chain(*result))
        #print(out)
        # s = UsersTable.select()
        # result = self.conn.execute(s)
        # print("data in table is ==>")
        # for row in result:
        #     print(row)






