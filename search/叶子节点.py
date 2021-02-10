class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        # 使用int做路径长度判定,比随身携带path们计算路径长度快
        def way(node, target:int):
            if not node: # root为空的判断也在里面做了
                return
            path.append(node.val)
            target -= node.val
            # 叶子节点没有子节点, 比如1->2树中的1节点 就不是叶子节点
            # 判定为叶子节点的前提下验证路径长度:
            if not node.left and not node.right and target ==0:
                res.append(path[:])
            else:
                way(node.left,target)
                way(node.right,target)
            path.pop() #恢复现场, path这个变量在全局统一处理

        way(root,targetSum)
        return res