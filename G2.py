from py2neo import Graph
import plotly.graph_objects as go
import pandas as pd

# Step 1: Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

# Step 2: Query Nodes and Relationships
nodes_query = "MATCH (n) RETURN id(n) as id, n.name as name, n.x as x, n.y as y, n.z as z"
relationships_query = "MATCH (a)-[r]->(b) RETURN id(a) as source, id(b) as target"

nodes = graph.run(nodes_query).data()
relationships = graph.run(relationships_query).data()

# Convert to DataFrame for easier handling
nodes_df = pd.DataFrame(nodes)
relationships_df = pd.DataFrame(relationships)

# Step 3: Create a 3D Scatter Plot
fig = go.Figure()

# Add nodes to the figure
fig.add_trace(go.Scatter3d(
    x=nodes_df['x'],
    y=nodes_df['y'],
    z=nodes_df['z'],
    mode='markers+text',
    text=nodes_df['name'],
    marker=dict(size=5, color='blue', opacity=0.8),
))

# Add edges to the figure
for index, row in relationships_df.iterrows():
    source = nodes_df[nodes_df['id'] == row['source']]
    target = nodes_df[nodes_df['id'] == row['target']]
    fig.add_trace(go.Scatter3d(
        x=[source['x'].values[0], target['x'].values[0]],
        y=[source['y'].values[0], target['y'].values[0]],
        z=[source['z'].values[0], target['z'].values[0]],
        mode='lines',
        line=dict(width=2, color='gray'),
    ))

# Update layout
fig.update_layout(title='3D Graph Visualization', scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
))

# Show the plot
fig.show()