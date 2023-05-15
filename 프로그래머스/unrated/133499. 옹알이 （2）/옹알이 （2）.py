def solution(babbling):
    
    answer = 0
    for bab in babbling:
        bab_list = list(bab)
        
        temp = ""
        while bab_list:
            if bab_list[0] == 'a':
                word = "".join(bab_list[:3])
                if temp != "aya" and word == "aya":
                    temp = "aya"
                    bab_list = bab_list[3:]
                else:
                    break

            elif bab_list[0] == 'y':
                word = "".join(bab_list[:2])
                if temp != "ye" and word == "ye":
                    temp = "ye"
                    bab_list = bab_list[2:]
                else:
                    break

            elif bab_list[0] == 'w':
                word = "".join(bab_list[:3])
                if temp != "woo" and word == "woo":
                    temp = "woo"
                    bab_list = bab_list[3:]
                else:
                    break

            elif bab_list[0] == 'm':
                word = "".join(bab_list[:2])
                if temp != "ma" and word == "ma":
                    temp = "ma"
                    bab_list = bab_list[2:]
                else:
                    break
                    
            else:
                break

        if bab_list == []:
            answer += 1

    return answer