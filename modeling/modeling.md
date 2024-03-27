# Modeling and Simulation

## Intro to ```NetworkX```
### Modeling a network with ```NetworkX```
- [tutorial](https://networkx.org/documentation/stable/tutorial.html)
- [drawing a graph with labels](https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html)

### Graph algorithms in ```NetworkX```
- [shortest path](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html)
- [coloring](https://networkx.org/documentation/stable/reference/algorithms/coloring.html)

### Import graph data
- [topology zoo](http://www.topology-zoo.org/dataset.html)
- [```read_gml```](https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.gml.read_gml.html#read-gml)


## Modeling a routing problem in optical networks

### Simulation Assumptions
- We do not use real datasets (request traces or network capacity). We need to put reasonable assumptions to simulate the behaviors of networks and requests.
- Parameters
  - Link capacity (e.g. 10)
  - Requests (num_requests = 40)
    - source and destination nodes (random)
    - holding time (random between 2 and 5)
  - Network topology 
    - A simple graph topology:
      - (1,2), (1,3), (1,4), (2,4), (3,0), (4,0)
    - (ATMnet: http://www.topology-zoo.org/files/Atmnet.gml)
- Algorithm
  - routing algorithm (e.g., shortest path)
  - color selection algorithm (e.g., smaller index first)

### First implementation
- Assume simple routing and color selection algorithms, map requests onto a network.
- When a list does not have enough capacity, block the request.
- Keep track of how many requests were blocked.
- Also, compute the utilization of each link (% of slots occupied)

### Efficient routing and color selection
- Come up with some heuristics (routing and color selection) to improve the blocking probability and/or the utilization, compared to the first implementation.