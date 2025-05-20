import heapq
from building_data import graph  # 건물 정보 모듈에서 그래프 데이터 불러오기

def find_entrance(location):
    """ 현재 위치가 특정 건물 내부라면 해당 건물의 입구를 반환하는 함수 """
    if "본관" in location:
        return "본관_입구"
    elif "도서관" in location:
        return "도서관_입구"
    elif "체육관" in location:
        return "체육관_입구"
    return location  # 이미 입구라면 그대로 반환

def dijkstra(graph):
    # 사용자 입력 받기
    start = input("출발지를 입력하세요: ")
    end = input("도착지를 입력하세요: ")

    # 출입구를 거쳐 이동하도록 변경
    start_entrance = find_entrance(start)
    end_entrance = find_entrance(end)

    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # 최단 경로를 리스트에 저장 (순서 거꾸로 저장됨)
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]

    # 출입구를 경로에 포함
    if start_entrance != start:
        path.insert(1, start_entrance)  # 출발 위치 다음에 입구 추가
    if end_entrance != end:
        path.insert(-1, end_entrance)  # 도착 위치 전에 입구 추가

    return path[::-1]  # 최종 출력 시 거꾸로 정렬하여 올바른 순서로 반환

# 함수 실행
path = dijkstra(graph)
print(f"최단 경로 리스트: {path}")