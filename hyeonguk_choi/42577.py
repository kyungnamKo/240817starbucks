def solution(phone_book):
    answer = True
    phone_book.sort()
    tag = 1
    for i in phone_book:
        len_val = len(i)
        for j in phone_book[tag:tag+1]:
            if hash(j[0:len_val]) == hash(i):
                answer = False
                break
            tag += 1
        if answer == False:
            break
    return answer