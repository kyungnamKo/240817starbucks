def solution(clothes):
    answer = 0
    c_dict = {}
    for i in clothes:
        c_dict[i[1]] = []
    for i in clothes:
        c_dict[i[1]].append(i[0])
        
    rr = []
    
    for j in c_dict.values():
        rr.append(len(j))
        
    fig = 1
    
    for x in rr:
        fig = fig * (x+1)
        
    answer = fig -1
    
    return answer