from py2neo import Graph
import networkx as nx
import plotly.graph_objs as go

from FamilyModule import FamilyTree as ft

# Connection to Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"
# ft = ft(uri, username, password)

# Connection to Neo4j database
graph_db = Graph(uri, auth=(username, password))


query = """
MATCH (n)-[r]->(m)
RETURN n.name AS source, m.name AS target
"""
results = graph_db.run(query)

# 3. ایجاد گراف با استفاده از NetworkX

G = nx.DiGraph()  
for record in results:
    G.add_edge(record["source"], record["target"])


pos = nx.spring_layout(G, dim=3)  

# گرفتن لیست گرهها و یالها
node_x = []
node_y = []
node_z = []
for node in G.nodes():
    x, y, z = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_z.append(z)

edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

# نمایش گرهها
node_trace = go.Scatter3d(
    x=node_x, y=node_y, z=node_z,
    mode='markers',
    marker=dict(size=10, color='blue'),
    text=list(G.nodes()),
    hoverinfo='text'
)

# نمایش یالها
edge_trace = go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    mode='lines',
    line=dict(width=2, color='gray'),
    hoverinfo='none'
)

# تنظیمات نهایی برای نمایش گراف
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='3D Graph Visualization',
                    showlegend=False,
                    scene=dict(
                        xaxis=dict(showbackground=False),
                        yaxis=dict(showbackground=False),
                        zaxis=dict(showbackground=False)
                    )
                ))

fig.show()