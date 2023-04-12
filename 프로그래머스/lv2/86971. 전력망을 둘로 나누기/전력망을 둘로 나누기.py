def BFS(v, n, graph):
    cnt = 0
    queue = [v]

    visited = [0 for _ in range(n + 1)]
    visited[v] = 1

    while queue:
        vq = queue.pop(0)

        for g in graph[vq]:
            if visited[g] == 0:
                visited[g] = 1
                queue.append(g)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = 999
    graph = [[] for _ in range(n + 1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        cnt_v1 = BFS(v1, n, graph)
        cnt_v2 = BFS(v2, n, graph)

        answer = min(answer, abs(cnt_v1 - cnt_v2))

        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer