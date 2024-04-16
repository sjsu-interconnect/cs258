# The Routing and Spectrum Allocation Problem
CS258 Final Project (Spring 2024)

## Motivation
Efficiently solving the Routing and Spectrum Allocation (RSA) problem in optical communication networks is crucial for maximizing resource utilization, improving quality of service, and reducing operational costs. By allocating spectrum and routing optimally, these networks can handle increasing traffic demands, support emerging technologies, and ensure reliable and high-speed communication services for users. Effective solutions to the RSA problem enable optical networks to scale efficiently, minimize congestion, and support the continued growth of digital communication infrastructure.

## The Problem
The objective is to maximize the utilization of optical resources across the network. Let $c(e)$ denote the capacity of a link $e$. When we represent the occupied slots at time $t$ on a link $e$ as $o(e)$, the utilization $u_t$ of the link $e$ at time $t$ can be computed by:
$$u_t(e) := \dfrac{o_t(e)}{c(e)}.$$

Therefore, the average utilization $U(e)$ of a link $e$ over $T$ episodes (equivalent to $T$ arrivals of requests) is
$$U(e) := \dfrac{1}{T}\sum_{t = 0}^{T-1}\dfrac{o_t(e)}{c(e)}.$$
The formal objective is to achieve maximum network-wide utilization. We define the network-wide utilization $U$ as the average of the edge total utility:
$$\text{Maximize } U := \dfrac{1}{|E|}\sum_{e\in E}U(e)$$

The continuity and capacity constraints should be imposed following our Assignment 4.


## Methods
### Routing
- Based on the optical network simulator we developed for Assignment 4, create a gymnasium environment
- Choose a few RL algorithms from the rllib implementation

### Spectrum Allocation
- Use a reasonable heuristic algorithm 
- A simple example was the index-based allocation in Assignment 4. You can modify it or come up with a new algorithm to improve the performance.
- (You can use a complex algorithm to optimize it as well.)

## Simulation Settings
- Use ```nsfnet.gml``` as the optical network topology
- Set the link capacity to 10 for all edges
- Generate 100 (=num_requests) requests that
   - (Case I) All requests have the same source and destination pair (```San Diego Supercomputer Center``` to ```Jon Von Neumann Center, Princeton, NJ```)
   - (Case II) The source and destination nodes are selected uniform-randomly among all nodes. (Make sure $s \neq d$)
   - with a uniformly randomly generated holding time
     - You should generate a different holding time for each request by
     - ```np.random.randint(min_ht, max_ht)```
     - Use ```min_ht = 10``` and ```max_ht = 20```
     - For simplicity, you can terminate the simulation after accommodating (or blocking) the last ($T$-th) request. You do not need to wait for all residing requests to leave. We only care about the utilization until the handing of the last request.

## Evaluation
- Show the learning curve (reward vs episode)
- Show the increase of the objective function over time (the objective vs episode) by an RL algorithm
- Compare the values of the objective function obtained by at least two RL methods and the values of the objective obtained by simple heuristics, which we used in Assignment 4 (shortest path + index-based allocation)

## Paper Template
- Use the LaTeX template ```s258-final-report-template.zip``` 
- You can write the report on [Overleaf](https://www.overleaf.com/)