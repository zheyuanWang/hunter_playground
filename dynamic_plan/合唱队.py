#合唱队形
0
while True:
    try:
        n = int(input())
        dp_left = [1] * n
        dp_right = [1] * n
        a = list(map(int,input().split()))

        for i in range(n):
            for j in range(i):
                if a[j] < a[i] and dp_left[j]+1 > dp_left[i]:
                    dp_left[i] = dp_left[j] + 1
        #for i in range(n)[::-1]:
        for i in range(len(a) - 1, -1, -1):
            #for j in range(len(a) - 1, i, -1):
            for j in range(i+1,n):
                if a[i] > a[j] and dp_right[j] +1 > dp_right[i]:  # BUG:不一定需要连续递增, 可以跳位的
                    dp_right[i] = dp_right[j] + 1
        #print(dp_left)
        #print(dp_right)
        for i in range(n):
            dp_left[i] = dp_left[i] + dp_right[i]
        #print(dp_left)
        print(n - max(dp_left) + 1)
    except:
        break



def left_max(list):
    """计算出i这个人，包含自己，在左边符合人数的个数"""
    res = [1] * len(list)
    for i in range(len(list)):
        for j in range(i):
            if list[j] < list[i] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    return res


def right_max(list):
    """计算出i这个人，包含自己，在右边符合人数的个数"""
    res = [1] * len(list)
    for i in range(len(list))[::-1]:
        for j in range(i + 1, len(list)):
            if list[j] < list[i] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    return res


while True:
    try:
        n = int(input())
        result = list(map(int, input().split()))
        left = left_max(result)
        right = right_max(result)
        sum_list = []
        for i in range(len(left)):
            sum_list.append(left[i] + right[i])
        print(n - (max(sum_list) - 1))

    except:
        break
