#a=int(input())

a = 64577
res = ''
for i in [2,3,5,7,11,13]:
    while a%i==0:
        a = a/i
        res =res + str(i)+" "

if a!=1 and a>=17:
    for i in range(17,10790,2):
        if i%3==0: continue
        while a%i==0:
            a = a/i
            res =res + str(i)+" "
if a>4000:
    res = res + str(a) + " "
print(res)

