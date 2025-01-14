from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passwd
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #USER = 'aacuser'
        #PASS = 'FJB2020'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 32379
        #DB = 'AAC'
        #COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]


# Method to implement the C in CRUD.
    def create(self, animal):
        if animal is not None:
            self.database.animals.insert_one(animal)  # insert a new animal doc
            print("Document inserted/created?: True")
        else:
            raise Exception("Document inserted/created?: False")

# Method to implement the R in CRUD.
    def read(self, animal):
        if animal is not None:
            read_results = list(self.database.animals.find(animal)) #read_results var in a list format
            return read_results
        else:
            raise Exception("Empty list")           

# Method to implement the U in CRUD.
    def update(self, animal, updateAnimal):
        if animal is not None:
            updated = self.database.animals.update_one(animal, updateAnimal) #update var in JSON format
            print("print(updated)", updated)
            self.read(animal)
            print("Updates: ", updated.modified_count) #quantity updated shown
        else:
            raise Exception("Empty list")

# Method to implement the D in CRUD.
    def delete(self, animal):
        if animal is not None:
            delete_results = self.database.animals.delete_many(animal)
            print(delete_results.deleted_count) #quantity deleted shown
        else:
            raise Exception("Empty list")


