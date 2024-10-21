
from FamilyModule import FamilyTree as ft

# Connection to Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"
ft = ft(uri, username, password)

# Connect to the Neo4j database
#driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))

# def delete_node(node_id):
#     query = """
#     MATCH (n)
#     WHERE id(n) = $node_id
#     DETACH DELETE n
#     """
#     with driver.session() as session:
#         session.run(query, node_id=node_id)


#ID = int(input("enter id:"))

count=int(input("enter count:"))

for ID in range(count):
    ft.delete_node(ID)

# Close the driver
ft.close()