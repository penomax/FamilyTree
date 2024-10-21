
from neo4j import GraphDatabase
from datetime import datetime
import uuid
import shortuuid
import random

class UniqueIDGenerator:
    def __init__(self):
        self._generated_ids = set()

    def get_unique_id(self):
        while True:
            # Generate a random 5-digit integer
            new_id = random.randint(10000, 99999)
            # Check if the ID is unique
            if new_id not in self._generated_ids:
                self._generated_ids.add(new_id)
                return new_id
            
    def IDset(self):
        return self._generated_ids

class FamilyTree:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_person(self, name, lastName, BD, sex, FatherID):
        
        idg = UniqueIDGenerator()
        personID = idg.get_unique_id()
        
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                tx.run("CREATE (p:Person {name: $name, lastName: $lastName, BD: $BD, sex: $sex ,FatherID: $FatherID, Idd:$Idd})"
                        , name=name, lastName=lastName, BD=BD, sex=sex, FatherID=FatherID, Idd=personID)
        return(personID)                


    def create_relationship(self, person1_name, person2_name, relationship_type):
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Person {name: $person1_name}), (b:Person {name: $person2_name})
                CREATE (a)-[:RELATIONSHIP_TYPE {type: $relationship_type}]->(b)
            """, person1_name=person1_name, person2_name=person2_name, relationship_type=relationship_type)
            

    def Create_Child_Of_Relationships(self):
        # Query to find nodes where one person's fatherID matches another person's id
        query = """
        MATCH (child:Person), (father:Person)
        WHERE child.FatherID = father.Idd
        MERGE (child)-[:CHILD_OF]->(father)
        """
        
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                tx.run(query)
    
    def delete_node(self, node_id):
        query = """
        MATCH (n)
        WHERE id(n) = $node_id
        DETACH DELETE n
        """
        with self.driver.session() as session:
            session.run(query, node_id=node_id)

   #def marriage
   
    def ancestor(self, name, lastName, BD, sex, Idd, FatherID):
        
        with self.driver.session() as session:
            with session.begin_transaction() as tx:
                tx.run("CREATE (p:Person {name: $name, lastName: $lastName, BD: $BD, sex: $sex, Idd:$Idd, FatherID: $FatherID})"
                        , name=name, lastName=lastName, BD=BD, sex=sex, FatherID=FatherID, Idd=Idd)
