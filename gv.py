from py2neo import Graph
from pyvis.network import Network
import pandas as pd

# Step 1: Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

# Step 2: Query Nodes and Relationships using elementId
nodes_query = "MATCH (n) RETURN elementId(n) as id, n.name as name"
relationships_query = "MATCH (a)-[r]->(b) RETURN elementId(a) as source, elementId(b) as target"

nodes = graph.run(nodes_query).data()
relationships = graph.run(relationships_query).data()

# Convert to DataFrame for easier handling
nodes_df = pd.DataFrame(nodes)
relationships_df = pd.DataFrame(relationships)


# Step 3: Create a PyVis Network
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

# Add nodes to the network
for _, row in nodes_df.iterrows():
    net.add_node(row['id'], label=row['name'], title=row['name'], physics=True)

# Add edges to the network
for _, row in relationships_df.iterrows():
    net.add_edge(row['source'], row['target'])

# Step 4: Configure the Network
net.show_buttons(filter_=['physics'])

# Save the visualization to an HTML file
html_file = 'neo4j_graph.html'
net.save_graph(html_file)
net.show(html_file)
