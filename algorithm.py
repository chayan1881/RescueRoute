import heapq

class RescueGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_id, x, y):
        self.nodes[node_id] = (x, y)
        if node_id not in self.edges:
            self.edges[node_id] = {}

    def add_edge(self, u, v, base_weight, traffic_multiplier=1.0):
        final_weight = base_weight * traffic_multiplier
        self.edges[u][v] = final_weight
        self.edges[v][u] = final_weight

    def heuristic(self, u, v):
        x1, y1 = self.nodes[u]
        x2, y2 = self.nodes[v]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def dijkstra(self, start, goal):
        if start not in self.nodes or goal not in self.nodes:
            return None, float('inf'), 0

        pq = [(0, start)]
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        nodes_explored = 0

        while pq:
            current_cost, current = heapq.heappop(pq)
            if current in came_from and current_cost > g_score[current]:
                continue
            
            nodes_explored += 1

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, g_score[goal], nodes_explored

            for neighbor, weight in self.edges[current].items():
                temp_g = g_score[current] + weight
                if temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    came_from[neighbor] = current
                    heapq.heappush(pq, (temp_g, neighbor))

        return None, float('inf'), nodes_explored

    def a_star_search(self, start, goal):
        if start not in self.nodes or goal not in self.nodes:
            return None, float('inf'), 0

        open_set = [(0, start)]
        came_from = {}
        g_score = {node: float('inf') for node in self.nodes}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.nodes}
        f_score[start] = self.heuristic(start, goal)
        open_set_hash = {start}
        nodes_explored = 0

        while open_set:
            current = heapq.heappop(open_set)[1]
            open_set_hash.remove(current)
            nodes_explored += 1

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, g_score[goal], nodes_explored

            for neighbor, weight in self.edges[current].items():
                temp_g = g_score[current] + weight
                if temp_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + self.heuristic(neighbor, goal)
                    if neighbor not in open_set_hash:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        open_set_hash.add(neighbor)

        return None, float('inf'), nodes_explored