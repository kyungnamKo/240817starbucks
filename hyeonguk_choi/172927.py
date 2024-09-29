def solution(picks, minerals):
    answer = []
    tired = [[1, 1, 1],
             [5, 1, 1],
             [25, 5, 1]]
    tools = {"diamond" : 1, "iron": 2, "stone": 3}
    
    def dfs(minerals, picks, tired_rate):
        if sum(picks) == 0 or minerals == []:
            answer.append(tired_rate)
            return
        m = minerals[:5]
        for t in range(3):
            if picks[t] > 0:
                picks[t] -= 1
                tired_rate_val = tired_rate_calculate(t, m)
                dfs(minerals[5:], picks, tired_rate+tired_rate_val)
                picks[t] += 1

    def tired_rate_calculate(t, minerals):
        tired_rate = 0
        for m in minerals:
            tired_rate += tired[t][tools[m]-1]

        return tired_rate
    dfs(minerals, picks, 0)
    answer.sort()
    return answer[0]