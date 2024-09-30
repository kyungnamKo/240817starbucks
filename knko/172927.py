def solution(picks, minerals):    
    answer = 0
    l = int(len(minerals) / 5) + 1
    
    case = []
    t=0
    for i in range(1, l+1):
        mine = minerals[t:i*5]
        dia=0
        iron=0
        stone=0
        for j in mine:
            if j == "diamond":
                dia += 1
            elif j == "iron":
                iron += 1
            else:
                stone += 1
        case.append([dia, iron, stone])
        t+=5
        
    case = case[:sum(picks)]
                
    case = sorted(case, key = lambda x: (-x[0], -x[1], -x[2]))
        
    for i in case:
        if picks[0]>0:
            picks[0] -= 1
            answer += i[0]
            answer += i[1]
            answer += i[2]
        elif picks[1]>0:
            picks[1] -= 1
            answer += i[0]*5
            answer += i[1]
            answer += i[2]
        elif picks[2]>0:
            picks[2] -= 1
            answer += i[0]*25
            answer += i[1]*5
            answer += i[2]

    return answer

