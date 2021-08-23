# Route Planning
## Problem statement
Imagine a delivery executive called Aman standing idle in Koramangala somewhere when suddenly his phone rings and notifies that he’s just been assigned a batch of 2 orders meant to be delivered in the shortest possible timeframe.

![route graph](https://github.com/abhaikollara/route-planning/blob/master/assets/graph.png)

All the circles in the figure above represent geo-locations :
- C1​ : Consumer 1
- C2​ : Consumer 2
- R1​ : Restaurant C1​ has ordered from. Average time it takes to prepare a meal is pt1
- R2​ : Restaurant C2​ has ordered from. Average time it takes to prepare a meal is pt2

Since there are multiple ways to go about delivering these orders, your task is to help Aman figure out the best way to finish the batch in the shortest possible time.

_For the sake of simplicity, you can assume that Aman, R1 and R2 were informed about these orders at the exact same time and all of them confirm on doing it immediately. Also, for travel time between any two geo-locations, you can use the haversine formula with an average speed of 20km/hr ( basically ignore actual road distance or confirmation delays everywhere although the real world is hardly that simple ;)_

## Solution(incomplete)
The problem is best represented as an weighted undirected graph where the locations are the nodes, edges being the roads and travel time is the weights.

- The locations will be represented in coordinates
- The distance and time to travel will be calculated using Haversine formula as suggested
- The actual locations are assumed to be inputs

A naive solution would be to generate all possible paths and check which has the minimum sum of weights.
Ideally, the path will be a minimum spanning tree generated under the condition that no customer node is visited before corresponding restaurant node is visited

The naive solution will work for a case with only two orders. The possible combinations are few and can be easily generated
- R1 -> C1 -> R2 -> C2
- R1 -> R2 -> C1 -> C2
- R1 -> R2 -> C2 -> C1

## Code
The example code is in `main.py`. Run using

```
python3 main.py
```

No external dependencies other than Python3 required.
