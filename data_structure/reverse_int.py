"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0
"""

in_int =input()
# 我这个方法用了一个set和一个list,
# 分别用来判定重复 & 储存数据
check = set([])
res = []

for i in list(in_int)[::-1]:
    if i not in check:
        res.append(i)
        check.add(i)
print(int("".join(res)))


# 优化: 纯string操作, 其实没必要用list存储数据
# (set判重 在数据量大的情况下有优势)
out = ""
for i in in_int[::-1]:
    if i not in out:
        out+=i
print(out)