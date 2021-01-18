"""
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。


输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
"""

items, volume = map(int,input().split())
costs = list(map(int,input().split()))
items, volume = 3,10
costs = [1,2,4]


def dfs(costs,remain_volumen,count=0):
    if remain_volumen==0 or costs==[]:
        return 1
    if costs[0]<=remain_volumen:
        return dfs(costs[1:],remain_volumen) + dfs(costs[1:],remain_volumen-costs[0])
    else:
        return dfs(costs[1:],remain_volumen)
if sum(costs)<=volume:
    print (2**(len(costs)))  # 全都可以放进背包的情况直接输出
else:
    print(dfs(costs,volume,0))


#f(i,v) = f(i-1,v) + f(i-1,v-costs[i])


