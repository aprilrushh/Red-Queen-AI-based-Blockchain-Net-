import random

# Example Node class: each node has a stake and performance metrics.
class Node:
    def __init__(self, node_id, stake, metrics):
        self.node_id = node_id
        self.stake = stake  # Example: number of tokens held
        self.metrics = metrics  # Example: {'uptime': 0.98, 'latency': 40, 'throughput': 12}
        self.trust_score = 0

# Simplified AI model: a function that calculates the trust score based on input metrics
def calculate_trust_score(metrics):
    # Example: 50% weight for uptime, 30% weight for the inverse of latency, and 20% for throughput
    score = (metrics['uptime'] * 0.5 +
             (1 / metrics['latency']) * 0.3 +
             metrics['throughput'] * 0.2)
    return score

# List of nodes in the network
nodes = [
    Node(1, 100, {'uptime': 0.99, 'latency': 50, 'throughput': 10}),
    Node(2, 150, {'uptime': 0.95, 'latency': 40, 'throughput': 12}),
    Node(3, 120, {'uptime': 0.97, 'latency': 45, 'throughput': 11})
]

# Calculate the trust score for each node
for node in nodes:
    node.trust_score = calculate_trust_score(node.metrics)

# Weighted random selection for the block proposer: combining stake and trust score
total_weight = sum(node.stake * node.trust_score for node in nodes)
rand_val = random.uniform(0, total_weight)
cumulative = 0

selected_node = None
for node in nodes:
    cumulative += node.stake * node.trust_score
    if cumulative >= rand_val:
        selected_node = node
        break

print("Selected block proposer node:", selected_node.node_id)
