# Import modul
import os
from dotenv import load_dotenv
import pymongo

# Memuat variabel lingkungan dari file .env ke dalam sistem
load_dotenv()

def get_mongo_client(mongo_uri):
    # Membuat koneksi ke MongoDB
    try:
        client = pymongo.MongoClient(mongo_uri)
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return client
        except Exception as e:
            print(e)
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None

def load(database, collection):
    # Memuat koleksi MongoDB berdasarkan database dan koleksi yang definisikan sebelumnya
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        print("MONGO_URI not set in environment variables")
        return None

    mongo_client = get_mongo_client(mongo_uri)

    # Memasukkan data ke MongoDB
    db = mongo_client[database]
    col = db[collection]

    return col
