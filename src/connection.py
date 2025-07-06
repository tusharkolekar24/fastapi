from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # loads from .env into os.environ

password    = os.getenv('PASSWORD')
username    = os.getenv('USERID')
server_name = os.getenv('SERVER_NAME')
database    = os.getenv('DATABASE')
driver      = os.getenv('DRIVER')

# print("------------------------------------------------------------------------")
# print(password,username,server_name,database)
# print("------------------------------------------------------------------------")

# Build URL using SQLAlchemy's URL.create()
connection_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host=server_name,
    database=database,
    query={
        "driver": driver,
        "Encrypt": "yes",
        "TrustServerCertificate": "yes"
    }
)