from andovermaps import simulation

# This is a DEMO of Andover Maps using a map of Andover's Main Campus

# (start, end, mu, len)
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

map_simulation = simulation(edge_information, NUM_NODES)

STARTING_NODE = 6
ENDING_NODE = 16

optimal_path = map_simulation.simulate(STARTING_NODE, ENDING_NODE)
print(optimal_path)