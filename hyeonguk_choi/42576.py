def solution(participant, completion):
    answer = ''
    completion.sort()
    participant.sort()
    for b in range(0,len(participant)):
        try:
            aa = (hash(participant[b]) != hash(completion[b]))
            if aa == True:
                answer = participant[b]
                break
        except:
            answer = participant[b]
            break
    return answer