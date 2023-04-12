def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans = []
        for j in range(len(arr1[0])):
            ans += [arr1[i][j]+arr2[i][j]]
            #ans = [4]
            #[4,6] [[7,9]]
            #[4] [6] 
        answer += [ans]
        #[[4,6]]+[[7,9]]
        #[[4]]+[[6]]
        #[[4,6],[7,9]]
        #[[4],[6]]
    return answer