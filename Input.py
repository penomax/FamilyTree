
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

name = input("INput name:")
lastName = input("Input Last Name:")
BD = int(input("input date:"))
sex = input("Input Gender:")
FUID = int(input("INput FAther UUID:"))

ft.create_person(name,lastName,BD,sex,FUID)
ft.Create_Child_Of_Relationships()
ft.close
