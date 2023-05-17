def solution(keymap, targets):
    key_dict = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] in key_dict:
                key_dict[key[i]] = min(key_dict[key[i]], i + 1)
            else:
                key_dict[key[i]] = i + 1
    
    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            if t in key_dict:
                cnt += key_dict[t]
            else:
                cnt = -1
                break
        answer.append(cnt)
        
    return answer