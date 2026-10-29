from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from algorithm import RescueGraph

app = Flask(__name__)
CORS(app)

graph = RescueGraph()

# Setup simulated urban network nodes & coordinates
city_intersections = {
    'Hospital': (0, 0),
    'Junction_A': (1, 3),
    'Junction_B': (3, 1),
    'Junction_C': (4, 4),
    'Junction_D': (6, 2),
    'Accident_Site': (7, 6)
}

for node, coords in city_intersections.items():
    graph.add_node(node, coords[0], coords[1])

# Setup road connections with simulated traffic bottlenecks
graph.add_edge('Hospital', 'Junction_A', base_weight=3.2, traffic_multiplier=1.0)
graph.add_edge('Hospital', 'Junction_B', base_weight=4.0, traffic_multiplier=1.8) # Heavy Traffic
graph.add_edge('Junction_A', 'Junction_C', base_weight=2.5, traffic_multiplier=1.0)
graph.add_edge('Junction_B', 'Junction_D', base_weight=3.0, traffic_multiplier=1.1)
graph.add_edge('Junction_C', 'Accident_Site', base_weight=3.5, traffic_multiplier=1.2)
graph.add_edge('Junction_D', 'Accident_Site', base_weight=2.8, traffic_multiplier=1.0)
graph.add_edge('Junction_A', 'Junction_B', base_weight=2.0, traffic_multiplier=1.0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/optimize-route', methods=['POST'])
def optimize_route():
    data = request.json
    start = data.get('start', 'Hospital')
    goal = data.get('goal', 'Accident_Site')
    algorithm = data.get('algorithm', 'astar')

    if algorithm == 'dijkstra':
        path, total_cost, nodes_explored = graph.dijkstra(start, goal)
    else:
        path, total_cost, nodes_explored = graph.a_star_search(start, goal)

    if not path:
        return jsonify({"error": "No valid route found"}), 404

    return jsonify({
        "success": True,
        "algorithm_used": algorithm.upper(),
        "path": path,
        "total_cost": round(total_cost, 2),
        "nodes_explored": nodes_explored,
        "coordinates": [graph.nodes[n] for n in path]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)