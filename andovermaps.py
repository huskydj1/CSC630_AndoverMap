from scipy.stats import poisson
import numpy as np 
import matplotlib.pyplot as plt
from collections import defaultdict
import heapq 
from tqdm import tqdm

from tqdm import tqdm

from collections import defaultdict
import heapq 

def dijkstraAlgorithm(adj, startingNode):
  visited = set()
  parentsMap = {}
  pq = [] # priority queue: sorts unvisited nodes by weight 
  nodeCosts = defaultdict(lambda : float('inf'))
  nodeCosts[startingNode] = 0
  heapq.heappush(pq, (0, startingNode))

  while pq:
    _, cur = heapq.heappop(pq)
    visited.add(cur)

    for (neigh, weight) in adj[cur]:
      if neigh in visited:
        continue
      
      newCost = nodeCosts[cur] + weight
      if nodeCosts[neigh] > newCost:
        parentsMap[neigh] = cur
        nodeCosts[neigh] = newCost
        heapq.heappush(pq, (newCost, neigh))

  return nodeCosts, parentsMap # returning 1) the costs to visit each node 2) the most recent node you used to get to the destination node

def backtrackDijkstra(parentsMap, start, end):
  path = []

  cur = end
  while(cur!=start):
    path.append(cur)
    cur = parentsMap[cur]
  
  path.append(start)

  path = path[::-1]

  return path

class simulation:
    def __init__(self, edge_information, NUM_NODES):
        self.edge_information = edge_information
        self.NUM_NODES = NUM_NODES

    def sampleGraph(self):
        sampledPaths = []

        for (start, end, mu, len) in self.edge_information:
            path_congestion = np.random.poisson(lam = mu)

            path_weight = 0.5 * path_congestion + 0.5 * len # TODO: Normalize 

            sampledPaths.append((start, end, path_weight))

        return sampledPaths

    def simulate(self, STARTING_NODE, ENDING_NODE):
        votes = dict() # tallying up the simulation's votes for different paths

        for step_z in tqdm(range(10000)):
            
            edge_list = self.sampleGraph()

            # Build Adjacency List

            adj = [[] for i in range(0, self.NUM_NODES+1)]
            
            for (start, end, weight) in edge_list:
                adj[start].append((end, weight))
                adj[end].append((start, weight))
            
            # Run Dijkstra's Algorithm

            _, parentsMap = dijkstraAlgorithm(adj, STARTING_NODE)

            # Backtrack for Shortest Path

            path = backtrackDijkstra(parentsMap, STARTING_NODE, ENDING_NODE)
            path = tuple(path)

            # Voting

            if path in votes:
                votes[path] += 1
            else:
                votes[path] = 1

        # Choose Path with the Most Votes

        return max(votes, key = votes.get)