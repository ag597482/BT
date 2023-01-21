import pymongo

class MongoClient():

    def __init__(self, url):
        self.client = pymongo.MongoClient(url)
        self.db = self.client.test
    
    def list_database_names(self):
        return self.client.list_database_names()
    
    def get_database_collection(self, database, collection):
        return self.client.get_database(database).get_collection(collection)
