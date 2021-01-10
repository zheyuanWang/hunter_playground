# 给定一棵二叉搜索树，请找出其中第k大的节点。

class Solution:
    def kthLargest_fool(self, root: TreeNode, k: int) -> int:
        """
        二叉搜索树的 中序遍历倒序 为 递减序列
        先中序,再求第k大
        -> 没有必要遍历完整棵树, 到第k大即可
        """
        if not root: return
        def mid_tran(node:TreeNode):
            if node:
                return mid_tran(node.left)+ [node.val] + mid_tran(node.right) if node else []
            else:
                return []
        res = mid_tran(root)
        return res[-k]

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        优化: stack实现反向中序遍历, 到k即止
        """
        #if not root: return
        node = root
        stack = []
        count = 0
        while stack or node:
            while node:
                stack.append(node)
                node=node.right
            node = stack.pop()
            #res.append(node.val)
            count +=1
            if count==k:
                return node.val
            node = node.left
