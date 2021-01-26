n = int(input())
x = int(input())
in_list = list(map(int,input().split()))
plan = [-1]*n

def check_match(plan, in_list):
    for i in range(len(in_list)):
        if plan[i]==in_list[i]:
            return in_list[i]
    return None

i=x
count = 0
while 1:
    plan[i]=count
    i-=1
    count+=1
    if i<0:
        i = n-1
        out = check_match(plan,in_list)
        if out != None:
            print(out)
            break
    print(plan)

