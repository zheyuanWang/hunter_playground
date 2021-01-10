#data_in = input()
data_in = "cbbcbbcbcca"

def drawer(data_in):
    """用一个抽屉有序保存检测到的字母"""
    dr = [""]*26
    for i in data_in:
        index = ord(i) - ord("a")
        if not dr[index]:
            dr[index] = chr(ord("a")+index)
    print("".join(dr))

drawer(data_in)

def tranverse_all(data_in):
    """先遍历再排序的笨方法"""
    l = []
    for i in data_in:
        if i not in l:
            l.append(i)
    l=sorted(l)
    print("".join(l))

