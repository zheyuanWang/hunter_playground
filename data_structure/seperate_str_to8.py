def prt8(st):
    """转换为list处理"""
    l_st = list(st)
    res =[]
    while l_st:  # 遍历
        res.append(l_st.pop(0))
        if len(res)==8: #满8发车
            print("".join(res))
            res =[]
    if res:  #剩下的补全到8位
        add=8-len(res)
        res= res + ['0'] * add
        print("".join(res))

def prt8_st(st):
    """利用字符串切片"""
    res =''
    while st:
        res += st[0]
        st = st[1:]
        if len(res) == 8:  # 满8发车
            print(res)
            res = ''
    if res:
        res = res + '0'*(8-len(res))
        print(res)



while True:  #应对多轮输入
    try:
        prt8_st(input())
    except:
        break
