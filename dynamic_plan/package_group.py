"""
王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
    设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
    请你帮助王强设计一个满足要求的购物单。

（其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q

（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
"""


N, m = map(int, input().split())
N = int(N / 10) # tip: 既然是整10倍就赶紧//10 吧, 不然后面list就算range跳过了中间也会有很多0

price = [[0] * (m+1) for i in range(4)]  #参考答案有直接按照题目的最大可能内存初始化的, 比较省心,没有越界的问题
value = [[0] * (m+1) for i in range(4)]

for ii in range(1,m+1):
    p, importance, fujian = map(int, input().split())
    p= p//10  # tip 在这里就//10 比后面一行一行//10好多了
    if fujian == 0:
        for k in range(4):  # BUG: 原本保持其他cost为初始值0,价格为0的情况可能导致bug
            price[k][ii] = p
            value[k][ii] = p * importance
    else:
        if price[1][fujian] == price[0][fujian]:
            price[1][fujian] = p + price[0][fujian]
            value[1][fujian] = p * importance + value[0][fujian]
        else:
            price[2][fujian] = p + price[0][fujian]
            value[2][fujian] = p * importance + value[0][fujian]
            # BUG: p3=p2+p1, 后两者都包含p0, p0被重复加了两遍!
            price[3][fujian] = price[1][fujian] + price[2][fujian]-price[0][fujian]  # both fujian
            value[3][fujian] = value[1][fujian] + value[2][fujian]-value[0][fujian]

res = [0] * (N+1)
for i in range(1,m+1):  # price list
    for j in range(N, -1, -1):  # money
            for k in range(4): # 遍历group内, 要防止group内重复
                if price[k][i] <= j:  # 保证钱还够
                    res[j] = max(res[j - price[k][i]] + value[k][i], res[j])
                    # 以剩下的钱j(行)为idx, res(j)里记录的是value
                    # 物品单价price以及价值value的查询都紧跟price list的i (列)

print(10 * res[-1]) # 若定长初始化则应取res[n]


#https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&&tqId=21239&rp=1&ru=/ta/huawei&qru=/ta/huawei/question-ranking