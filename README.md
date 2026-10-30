# 🚨 RescueRoute: Emergency Vehicle Route Optimization System

**RescueRoute** is a web-based emergency dispatch and route optimization application designed to compute and visualize the fastest path between emergency origins and incident sites. It features a lightweight client-server architecture utilizing graph-based pathfinding algorithms.

---

## 🚀 Key Features

* **Pathfinding Algorithms:** Supports **Dijkstra’s Algorithm** (exhaustive optimal routing) and **A* Search Algorithm** (heuristic target routing) using Python's `heapq` priority queue.
* **Interactive Mapping:** Powered by **Leaflet.js** and OpenStreetMap for dynamic vector polyline rendering and automatic viewport scaling.
* **Live Telemetry:** Instantly calculates and displays total path distance (km), estimated time of arrival (ETA in minutes), and traversal metrics.
* **Modern Dashboard:** Styled with **Bootstrap 5** for a clean, responsive emergency control panel.

---

## 📂 Project Structure

```text
RescueRoute/
│
├── server.py              # Flask backend server & REST API endpoints
├── algorithm.py           # Graph representation, Dijkstra, and A* logic
└── templates/
    └── index.html         # Frontend dispatcher dashboard (Bootstrap & Leaflet)
