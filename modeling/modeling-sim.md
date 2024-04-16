# 2024sp-a4: Modeling Simulation

## Simulation Setup
1. Create a linear graph with 5 nodes:
```
(0)--(1)--(2)--(3)--(4)
```
2. Set the link capacity to 5 for all edges
3. Generate 40 (=num_requests) requests that
   - travel from node 0 to node 4
   - Note: there is one advanced task that requires to change the source and destination later
   - with a uniformly randomly-generated holding time
     - You should generate a different holding time for each request by
     - ```np.random.randint(min_ht, max_ht)```
     - As described below, you execute multiple simulations changing ```min_ht``` and ```max_ht``` and observe the difference in utilization and blocking
4. Use a shortest path algorithm for the routing (There is no impact in this assignment as the graph is linear.)
5. Use the greedy color selection (smaller index first). 
   - When you have 5 (=capacity) colors (namely, 0, 1, 2, 3, 4), 
   - Always select the smallest color index available (0 --> 1 --> 2 ...)
   - When there is no available space, block the request

## Performance Metrics
- Count the number of blocked requests at each time round throughout the simulation (=40 for-loop rounds)
- Save the utilization of each link at each round
$$u_t(e) = \dfrac{\text{the number of occupied colors on edge }e \text{ at time } t}{5}$$

## Simulation Tasks
**(Task 1)** For the following three scenarios (A, B, and C), record the aforementioned performance metrics.

- (Scenario A) ```min_ht = 2``` and ```max_ht = 3``` (All requests have a holding time of 2 time rounds.)
- (Scenario B) ```min_ht = 5``` and ```max_ht = 6``` (All requests have a holding time of 5 time rounds.)
- (Scenario C) ```min_ht = 4``` and ```max_ht = 10```
- (Scenario D) ```min_ht = 4``` and ```max_ht = 10```; ```source = 0``` and ```destination = np.random.randint(1,5)```: The destination is selected randomly between node 1 and node 4.

**(Task 2)** Plot the recoded performance metrics
- Plot the number of blocked requests (y-axis) vs time round (x-axis)
- Plot the utilization of link between node 0 and 1 (y-axis) vs time round (x-axis)
- *(Only for Scenario D)* Plot the utilization of link between node 3 and 4 (y-axis) vs time round (x-axis)

## Submission
- Submit the simulator codes and a PDF file that includes the **9** plots

