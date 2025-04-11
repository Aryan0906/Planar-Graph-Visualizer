from flask import Flask, request, render_template, redirect, url_for, send_file
import networkx as nx
import json
import matplotlib.pyplot as plt # type: ignore
import os

app = Flask(__name__)

def check_planarity_and_euler(edges):
    graph = nx.Graph()
    graph.add_edges_from(edges)
    is_planar, embedding = nx.check_planarity(graph)
    if is_planar:
        V = graph.number_of_nodes()
        E = graph.number_of_edges()
        F = E - V + 2  # Euler's formula
        return is_planar, V, E, F, graph
    else:
        return is_planar, None, None, None, graph

def save_graph_image(graph, filename="static/graph.png"):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.savefig(filename)
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        edges_input = request.form.get("edges")
        try:
            edges = json.loads(edges_input)
            is_planar, V, E, F, graph = check_planarity_and_euler(edges)
            if is_planar:
                save_graph_image(graph)  # Save the graph visualization
                result = {
                    "is_planar": True,
                    "vertices": V,
                    "edges": E,
                    "faces": F,
                }
            else:
                result = {"is_planar": False}
        except Exception as e:
            result = {"error": str(e)}
        return redirect(url_for("result", result=json.dumps(result)))
    return render_template("index.html")

@app.route("/result")
def result():
    result = json.loads(request.args.get("result"))
    return render_template("result.html", result=result, graph_url="/static/graph.png")

if __name__ == "__main__":
    app.run(debug=True)