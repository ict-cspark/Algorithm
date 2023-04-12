def solution(number, k):
    num_list = list(number)
    result = []

    start = 0
    while k > 0:
        max_num = -1
        max_idx = 0
        for i in range(start, start + k + 1):
            if num_list[i] == '9':
                max_idx = i
                break
            if max_num < int(num_list[i]):
                max_num = int(num_list[i])
                max_idx = i

        result.append(num_list[max_idx])
        k -= (max_idx - start)
        start = max_idx + 1

        if (len(num_list) - start) == k:
            start += k
            break

    if start < len(num_list):
        result = result + num_list[start:]
    answer = "".join(result)
    return answer