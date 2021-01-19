#质数因子

#输入一个正整数，按照从小到大的顺序输出它的所有质数因子
# （重复的也要列举）（如180的质因子为2 2 3 3 5 ）

#-----法一: 优化:
# 遍历步长=2 跳过所有偶数 (第一个偶数2特殊处理)
# 只从2 遍历到根号n
a = int(input())
res = ''
while a % 2 == 0:
    a = a / 2
    res = res + str(2) + " "
for i in range(3, int(a ** 0.5) + 1, 2):
    while a % i == 0:
        a = a / i
        res = res + str(i) + " "
if a != 1:
    res = res + str(int(a)) + " "

print(res)


#------法二 筛选法
def ouLaShai(n):
    lis = [True for  i in range(n + 1)]
    #  用于筛选记录合数
    lis2 = []
    #  存质数
    for i in  range(2, n + 1):
        if lis[i]:
            #  如果没有被筛选就加到Lis2
             lis2.append(i)
        for prime  in lis2:
            if i *  prime > n:
                #  保证小于n，不能超出范围
                 break
            lis[i *  prime] = False
            #  记录合数
            if i %  prime == 0:
                 #  关键步骤，确保每个合数只被筛选一次
                 break
    return lis2

m = int(input())
res = ""
m_oula = int(m**0.5)+1
o = ouLaShai(m_oula)
for k in o:
    while m%k==0:
        m = m/k
        res= res+ str(k) + " "
if m!=1:
    res= res+ str(int(m)) + " "
print(res)