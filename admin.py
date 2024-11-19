import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv('database_path')
USER_TABLE = os.getenv("user_table")

from pymilvus import MilvusClient
conn = MilvusClient(DATABASE_PATH)

query = "vector == '[1,2,3,4,5]'"

res = conn.query(
        collection_name=USER_TABLE,
        filter=query,
        output_fields=["vector"]
    )


print(query)

conn.close()
