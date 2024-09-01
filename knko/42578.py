def solution(clothes):
    answer = {}
    
    for i in clothes:
        answer[i[1]] = ["없음"]
        
    for i in clothes:
        answer[i[1]].append(i[0])
    
    cnt = 1
    for i in answer.values():
        cnt *= len(i)
        
    return cnt - 1