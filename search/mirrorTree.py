class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def exchange(node): #内置一个函数用来递归
            if not node: return
            node.left, node.right = exchange(node.right),exchange(node.left)
            return node
        return exchange(root)


    def mirrorTree_official(self, root: TreeNode) -> TreeNode:
        #直接用本函数进行递归
        if not root: return
        #需要前缀self.来调用本函数
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

    def mirrorTree(self,root): # 执行用时： 28 ms , 在所有 Python3 提交中击败了 98.62% 的用户 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 9.21% 的用户
        # 迭代比上述递归方法速度快
        if not root: return
        stack = [root]
        while stack!=[]:
            node = stack.pop()
            node.right, node.left = node.left, node.right
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root

