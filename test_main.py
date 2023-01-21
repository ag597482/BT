from models.user import Person
from enums.gender import Gender
from configparser import ConfigParser
from clients.mysql_client import MySQLClient
from clients.mongo_client import MongoClient

p1 = Person("Aman", "36", 24, Gender.MALE)

# print(p1.name)
# print(p1.age)
# print(p1.gender == Gender.MALE)
# print(p1.getGender())

file = "config.ini"
config = ConfigParser()
config.read(file)
mysqlConfig = config['mysql']
mongoConfig = config['mongo']

mysql_client = MySQLClient(mysqlConfig['user'], 
    mysqlConfig['password'], 
    mysqlConfig['host'],
    mysqlConfig['database'])

# users = mysql_client.read_users()
# print(users)
mysql_client.update_user()
# mysql_client.insert_user(p1)

# mongo_client = MongoClient(mongoConfig['local_uri'])
# print(mongo_client.list_database_names())
# booksinfo_collection = mongo_client.get_database_collection('books','booksinfo')
# res =booksinfo_collection.find({
#     "$or" : [{
#                  "title" : { "$eq" : 'Don Quixote'}
#               }]
# })
# print(booksinfo_collection.find_one())
# print(type(res))
# print(res[1])
# for book in res:
#     print(book['title'])

