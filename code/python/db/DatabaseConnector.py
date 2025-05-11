from pymongo import MongoClient
import os
from dotenv import load_dotenv

class DatabaseConnector: 
    def __init__(self):
        load_dotenv()
        connection_string = os.getenv("MONGO_DB_CONNECTION_STRING")
        self.client = MongoClient(connection_string)
        
        print("Successfully connected to MongoDB!")
        print(f"Available databases: {self.client.list_database_names()}")
 
    def get_database(self):
        return self.client["SCS_Lists"]