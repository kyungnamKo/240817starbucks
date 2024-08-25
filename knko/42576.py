def solution(participant, completion):
    a = sorted(participant)
    b = sorted(completion)
    
    for i in range(len(b)):
        if a[i] != b[i]:
            if a[i+1] == b[i]:
                return a[i]
    return a[-1]