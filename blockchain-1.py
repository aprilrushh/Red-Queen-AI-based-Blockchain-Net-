import random

# 예시 노드 클래스: 각 노드는 스테이크와 성능 메트릭을 가짐.
class Node:
    def __init__(self, node_id, stake, metrics):
        self.node_id = node_id
        self.stake = stake  # 예: 보유 토큰 수량
        self.metrics = metrics  # 예: {'uptime': 0.98, 'latency': 40, 'throughput': 12}
        self.trust_score = 0

# 단순화된 AI 모델: 입력 메트릭에 따라 신뢰 점수를 산출하는 함수
def calculate_trust_score(metrics):
    # 예시: uptime에 50%, latency(역수)에 30%, throughput에 20% 가중치를 부여
    score = (metrics['uptime'] * 0.5 +
             (1 / metrics['latency']) * 0.3 +
             metrics['throughput'] * 0.2)
    return score


# 네트워크에 있는 노드들의 리스트
nodes = [
    Node(1, 100, {'uptime': 0.99, 'latency': 50, 'throughput': 10}),
    Node(2, 150, {'uptime': 0.95, 'latency': 40, 'throughput': 12}),
    Node(3, 120, {'uptime': 0.97, 'latency': 45, 'throughput': 11})
]

# 각 노드의 신뢰 점수 계산
for node in nodes:
    node.trust_score = calculate_trust_score(node.metrics)

# 가중치 기반 블록 제안자 선택: 스테이크와 신뢰 점수를 결합
total_weight = sum(node.stake * node.trust_score for node in nodes)
rand_val = random.uniform(0, total_weight)
cumulative = 0

selected_node = None
for node in nodes:
    cumulative += node.stake * node.trust_score
    if cumulative >= rand_val:
        selected_node = node
        break

print("블록 제안자로 선택된 노드:", selected_node.node_id)
