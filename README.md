# Welcome to Andover Maps!

This project was created to understand what the optimal paths look at between buildings in Phillips Academy Andover. By observing the occupancy of paths at the start of the day, we've weighted paths based on congestion and length, to give a weight of how long a path might take. We run 10,000 different simulations of potential congestions to give what we think the optimal path between two paths is. Take a look!

## 1. Install Requirements
`conda create --name <environment_name> --file requirements.txt`

## 2. Place AndoverMaps.py in the root of your project
To test our example, you can simply keep andovermaps.py in the same folder as demo.py

## 3. Convert your map into a graph
<img src = "https://i.ibb.co/kyRBhxK/FINAL-Andover-Map.jpg" width="40%" height=auto>

```
# Each item in the list represents an edge in the map, given by the starting node, ending node, mu value (occupancy per minute), and length (in m)
edge_information = [
  (2,	1,	9.3,	43),
  (2,	3,	7.2,	30),
  (2,	4,	4.5,	58),
  (2,	6,	9.8,	44),
  (1,	4,	2.4,	46),
  (4,	5,	0.2,	15),
  (5,	6,	0.2,	24),
  (6,	7,	3.7,	24),
  (3,	6,	1.3,	28),
  (3,	7,	5.2,	22),
  (6,	10,	8.1,	24),
  (4,	8,	5.9,	24),
  (8,	9,	2.3,	15),
  (9,	10,	2.2,	26),
  (10,	11,	1.8,	23),
  (9,	12,	0.4,	34),
  (10,	12,	9.7,	19),
  (8,	13,	8.6,	64),
  (13,	15,	4.6,	21),
  (15,	16,	5.1,	53),
  (16,	17,	3.6,	30),
  (17,	18,	2.1,	31),
  (11,	14,	1.3,	77),
  (12,	14,	10.1,	62),
  (13,	14,	1.9,	69),
  (15,	14,	0.7,	69),
  (17,	14,	1.2,	74),
  (18,	14,	1.2,	66),  
]

NUM_NODES = 18
```

4. Run the Simulation to find the optimal paths!
```
# Instantiating an object of andovermaps
map_simulation = simulation(edge_information, NUM_NODES)

# Our starting and ending locations, as notated in our graph
STARTING_NODE = 6
ENDING_NODE = 16

#Run the simulation
optimal_path = map_simulation.simulate(STARTING_NODE, ENDING_NODE)
print(optimal_path)
```