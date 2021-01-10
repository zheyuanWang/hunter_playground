import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:  # 我写的代码处理的是list,其中的null需要""双引号括起成string
    def serialize(self, root):
        #Encodes a tree to a single string.

        if not root:return
        que = [root]
        res=[]
        while(que):
            node = que.pop(0)  #注意pop默认是pop尾巴的, 要队列先进先出 需要pop(0)指定index
            if not node:
                res.append("null")
                continue
            res.append(node.val)
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        return res

    def deserialize(self, data):
        #Decodes your encoded data to tree.

        
        if not data: return

        data = str(data)[1:-1].split(",")
        print(data)
        root = TreeNode(data[0])
        que = [root]
        i = 1
        while(que):
            if i>=len(data): break
            node = que.pop(0)
            print(node.val)
            node.left = TreeNode(data[i])
            if data[i] != "null":
                que.append(node.left)
            i+=1
            node.right = TreeNode(data[i])
            if data[i] != "null":
                que.append(node.right)
            i+=1
        return root
"""

class Codec:  # 官方给的代码input是一串长得像list的string "[1,2,null]"
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            if i >= len(vals)-1: break
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

null='null'
#data = [5,2,3,null,null,2,4,3,1]
data="[1,2,3,null,null,4,5]"
codec = Codec()
print(codec.serialize(codec.deserialize(data)))


# #codec.deserialize(codec.serialize(root))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))