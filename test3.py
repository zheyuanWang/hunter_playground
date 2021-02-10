given = [i for i in range(6)]
n = 5
global res
res = []
def dfs(in_list, path,n):
    if len(path) == n:
        res.append(path[:])  # shallow copy
        return
    if in_list == []:
        return
    # two way: pick or don't pick
    path.append(in_list[0])
    dfs(in_list[1:], path,n)
    path.pop()
    dfs(in_list[1:], path,n)

dfs(given, [],n)
print(res)

