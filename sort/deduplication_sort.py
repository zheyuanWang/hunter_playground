# 多行多组输入需要搭配while, try, except进行持续接收

while True:
    try:  #用try，当检测到没有输入，直接抛出异常，程序结束
        a =int(input())  #range()中的参数要为int整型
        res = set()
        for i in range(a):   # 没有输入了，range(a)就会报错, 就跳出循环了
            res.add(int(input()))
        # 列式输出
        for i in sorted(res):  # 用集合去重之后，里面的元素可能会减少, 所以用新range(res)
            print(i)
    except:
        break