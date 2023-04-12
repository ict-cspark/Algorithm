import heapq


def solution(jobs):
    answer = 0
    start = -1
    end = 0
    idx = 0
    heap = []

    while idx < len(jobs):
        for j in jobs:
            if start < j[0] <= end:
                heapq.heappush(heap, (j[1], j[0]))

        if heap:
            work, request = heapq.heappop(heap)
            start = end
            end += work
            answer += end - request
            idx += 1
        else:
            end += 1

    return answer // idx