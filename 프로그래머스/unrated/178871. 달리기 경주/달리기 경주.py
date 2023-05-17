def solution(players, callings):
    players_dic = dict()
    rank_dic = dict()
    
    for i in range(len(players)):
        players_dic[players[i]] = i + 1
        rank_dic[i + 1] = players[i]
        
    for cal in callings:
        rk = players_dic[cal]
        pl = rank_dic[rk - 1]
        
        players_dic[cal] = rk - 1
        players_dic[pl] = rk
        
        rank_dic[rk] = pl
        rank_dic[rk - 1] = cal
        
    answer = []
    for key, value in rank_dic.items():
        answer.append(value)
        
    return answer