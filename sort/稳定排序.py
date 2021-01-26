while True:
    try:
        st= input()
        letter = []
        res = [False]*len(st)
        for idx,i in enumerate(st):
            if i.isupper() or i.islower():
                letter.append(i)
            else:
                res[idx] = i
        letter.sort(key=lambda c: c.lower())  #精华! 暂时忽视大小写的稳定排序
        counter = 0
        for idx, i in enumerate(res):
            if not i:
                res[idx]= letter[counter]
                counter+=1
        print("".join(res))
    except:
        break