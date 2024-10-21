from neo4j import GraphDatabase
from datetime import datetime
import uuid
import shortuuid
from FamilyModule import FamilyTree as ft

# Connection to Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"
ft = ft(uri, username, password)

ft.Create_Child_Of_Relationships()

