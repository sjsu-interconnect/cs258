# The RSA Problem

## Motivation
Efficiently solving the Routing and Spectrum Allocation (RSA) problem in optical communication networks is crucial for maximizing resource utilization, improving quality of service, and reducing operational costs. By allocating spectrum and routing data optimally, these networks can handle increasing traffic demands, support emerging technologies, and ensure reliable and high-speed communication services for users. Effective solutions to the RSA problem enable optical networks to scale efficiently, minimize congestion, and support the continued growth of digital communication infrastructure.

## The Problem
The objective is to maximize the utilization of optical resources across the network. Let $c(e)$ denote the capacity of a link $e$. When we represent the occupied slots at time $t$ on a link $e$ as $o(e)$, the utilization $u_t$ of the link $e$ at time $t$ can be computed by:
$$u_t(e) := \dfrac{o_t(e)}{c(e)}.$$

Therefore, the total utilization $U(e)$ of a link $e$ over $T$ episodes (equivalent to $T$ arrivals of requests) is
$$U(e) := \sum_{t = 0}^{T-1}\dfrac{o_t(e)}{c(e)}.$$
The formal objective is to achieve maximum network-wide utilization. We define the network-wide utilization $U$ as the average of the edge total utility:
$$\text{Maximize } U := \dfrac{1}{|E|}\sum_{e\in E}U(e)$$

The continuity and capacity constraints should be imposed following our Assignment 4.


## Methods
### Routing
- Wrap the optical network simulator we developed for Assignment 4 by the gymnasium environment
- Choose a few RL algorithms from the rllib implementation

### Spectrum Allocation
- Use a reasonable heuristic algorithm 
- A simple example we saw was the index-based allocation. You can modify it or come up with a new algorithm

## Simulation Settings
- Use ```nsfnet.gml``` as the optical network topology
- Set the link capacity to 10 for all edges
- Generate 100 (=num_requests) requests that
   - The source and destination nodes are selected uniform-randomly among all nodes. (Make sure $s \neq d$)
   - with a uniformly randomly generated holding time
     - You should generate a different holding time for each request by
     - ```np.random.randint(min_ht, max_ht)```
     - As described below, you execute multiple simulations changing ```min_ht``` and ```max_ht``` and observe the difference in utilization and blocking
     - Use ```min_ht = 10``` and ```max_ht = 20```

## Evaluation
- Show the learning curve (reward vs episode)
- Show the increase of the objective function over time (the objective vs episode)
- Compare the values of the objective function obtained by RL methods and the values of the objective obtained by simple heuristics, which we used in Assignment 4 (shortest path + index-based allocation)
