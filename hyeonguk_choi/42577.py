def solution(phone_book):
    answer = True
    lens = []
    for i in phone_book:
        lens.append(len(i))
    lens = list(set(lens))
    for j in lens:
        l_dict = {}
        for x in phone_book:
            l_dict[x] = hash(x[0:j])
        if (len(list(set(l_dict.values())))) < len(phone_book):
            for y in phone_book:
                l_dict.pop(y)
                if hash(y) in list(l_dict.values()):
                    answer = False
                    break
                else:
                    l_dict[y] = hash(y[0:j])
    return answer