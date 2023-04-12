import heapq


def dijkstra(distance, adj):
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            cost_sum = cost + c
            if cost_sum < distance[n]:
                distance[n] = cost_sum
                heapq.heappush(heap, (cost_sum, n))

    return


def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    distance[1] = 0

    adj = [[] for _ in range(N + 1)]
    for x, y, r in road:
        adj[x].append((r, y))
        adj[y].append((r, x))

    dijkstra(distance, adj)

    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
            
    return answer