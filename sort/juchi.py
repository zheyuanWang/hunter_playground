# -*- coding: utf-8 -*-
# @File  : 大小大小排序.py

in_data = input()
data = in_data.split(',')
out = []  # 输出列表


def compare(num1, num2):  # 比较函数
    if num1 > num2:
        return 0
    if num1 < num2:
        return 1
    if num1 == num2:
        return 2


for k in range(len(data)):

    if (k - 1) < 0:  # 存入首位
        out.append(int(data[0]))
    else:
        num1 = int(data[k - 1])
        num2 = int(data[k])

        if (k % 2) == 0:  # 区分基数还是偶数，也其实就是为了相邻的符号判断不同而已
            if compare(num1, num2) == 1:
                out.append(num2)
                out[k - 1], out[k] = out[k], out[k - 1]  # 元素交换
            else:
                out.append(num2)
        else:
            if compare(num1, num2) == 0:
                out.append(num2)

                out[k - 1], out[k] = out[k], out[k - 1]  # 元素交换
            else:
                out.append(num2)

print(out)


# 算法需要以排序后的输入为前提; 否则需解决bug:
# 输入 3,1,2
# 输出[1, 2, 3]