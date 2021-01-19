import bisect

#动态规划获得最大递增自序列，时间复杂度O(n*n)
# def ascMax(l, dp):
#     dp += [1]
#     for i in range(1, len(l)):
#         tmp = 0
#         for j in range(0, i):   #就是这第二个循环太慢了
#             if l[j] < l[i]:
#                 tmp = max(dp[j], tmp)
#         dp += [tmp + 1]

#二分法获取最大递增子序列，时间复杂度O(nlogn)
def ascMax(l, dp):
    dp += [1]
    b = [float('inf')]*len(l)  #初始化b数组为无穷大
    b[0] = l[0]#第一个元素自己就是最大递增子序列
    for i in range(1, len(l)): # 逐一添加元素, l[i]就是每次新加的元素
        pos = bisect.bisect_left(b, l[i]) #在 b 中找到 l[i] 合适的插入点以维持有序
        # 如果已存在相等元素, 插入点在它之前(左边); 插入后,左边val < l[i], 右边val>l[i]
        b[pos] = l[i]  # 既然找到了位置就插进入去
        dp += [pos + 1]  #pos表示这个数是递增序列b中第pos大的, 也就是说到此共pos个递增数字

while True:
    try:
        N = int(input())
        H = list(map(int, input().split()))
        dp_1, dp_2 = [], []
        ascMax(H, dp_1)
        ascMax(H[::-1], dp_2)
        dp = []
        for i in range(0, N):
            dp += [dp_1[i] + dp_2[N-i-1] - 1]
        print(N - max(dp))
    except:
        break
