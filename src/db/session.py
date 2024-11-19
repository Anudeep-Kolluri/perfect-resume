from pymilvus import MilvusClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_PATH = os.getenv('database_path')
SECTION_COLLECTION = os.getenv('section_collection')
KEYWORD_COLLECTION = os.getenv('keyword_collection')
EMBEDDING_SIZE = os.getenv('embedding_size')


def init_db():

    conn = MilvusClient(DATABASE_PATH)

    collections = conn.list_collections()
    if SECTION_COLLECTION not in collections:
        conn.create_collection(
            collection_name=SECTION_COLLECTION,
            dimension=EMBEDDING_SIZE,
            auto_id = True
        )

    if KEYWORD_COLLECTION not in collections:
        conn.create_collection(
            collection_name=KEYWORD_COLLECTION,
            dimension=EMBEDDING_SIZE,
            auto_id = True
        )

    conn.close()