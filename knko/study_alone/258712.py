def solution(friends, gifts):    
    x = [[0] * len(friends) for i in range(len(friends))]
    for i in gifts:
        give = i.split()[0]
        take = i.split()[1]
        give_i = friends.index(give)
        take_i = friends.index(take)
        x[give_i][take_i] += 1
        
    y = []
    for i in range(len(friends)):
        gift_j = sum(x[i])
        for j in range(len(friends)):
            gift_j -= x[j][i]
        
        y.append(gift_j)
    
    answer = []
    for i in range(len(friends)):
        present = 0
        for j in range(len(friends)):
            if i == j:
                continue
            
            if x[i][j] == x[j][i]:
                if y[i] > y[j]:
                    present += 1
            elif x[i][j] > x[j][i]:
                present += 1
        answer.append(present)
        
    return max(answer)