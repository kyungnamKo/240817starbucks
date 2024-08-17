def solution(phone_book):
#     cnt = [len(i) for i in phone_book]
#     dic = {a:b for a,b in enumerate(phone_book)}
    
    # for i in range(len(phone_book)):
    #     for j in range(1, )
    #     if dic[i] 

    while phone_book:
        a = phone_book.pop(0)
        k = [i[:len(a)] for i in phone_book if len(i) >= len(a)]
        if a in k:
            return False
    
    return True