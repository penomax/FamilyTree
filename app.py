from flask import Flask, render_template


app= Flask(__name__,
           static_folder="static", static_url_path="/static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("neo4j_graph.html")

@app.route("/example")
def example():
    return render_template("example.html")

@app.route("/new")
def new():
    return render_template("new.html")
    

if __name__ == "__main__":
    app.run(debug=True,port=8080)
   