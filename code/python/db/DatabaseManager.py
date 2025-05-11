from typing import List, Dict, Any
from pymongo import UpdateOne
from .DatabaseConnector import DatabaseConnector

class DatabaseManager:
    def __init__(self):
        self.connector = DatabaseConnector()
        self.db = self.connector.get_database()
        self.db["Blacklist"]
        self.db["Redlist"]

    def get_blacklist(self):
        return self.db["Blacklist"]

    def get_redlist(self):
        return self.db["Redlist"]
    
    def _create_query(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        query = entry.copy()
        return query
    
    def _insert_entries(self, collection_name: str, entries: List[Dict[str, Any]]) -> int:
        if not entries:
            return 0
            
        collection = self.db[collection_name]
        print(f"Got collection: {collection.name}")
        print(f"Collection stats: {collection.count_documents({})}")    
        
        operations = []
        
        for entry in entries:
            query = self._create_query(entry)
            print(query)
            operations.append(
                UpdateOne(
                    query,
                    {'$set': entry},
                    upsert=True
                )
            )
                    
        result = collection.bulk_write(operations, ordered=False)
        return result.upserted_count

    def insert_into_blacklist(self, entries: List[Dict[str, Any]]) -> int:
        count = self._insert_entries("Blacklists", entries)
        print(f"Inserted {count} new entries into blacklist out of {len(entries)} total entries")
        return count
        
    def insert_into_redlist(self, entries: List[Dict[str, Any]]) -> int:
        count = self._insert_entries("Redlists", entries)
        print(f"Inserted {count} new entries into redlist out of {len(entries)} total entries")
        return count