class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        # ʹ��int��·�������ж�,������Я��path�Ǽ���·�����ȿ�
        def way(node, target:int):
            if not node: # rootΪ�յ��ж�Ҳ����������
                return
            path.append(node.val)
            target -= node.val
            # Ҷ�ӽڵ�û���ӽڵ�, ����1->2���е�1�ڵ� �Ͳ���Ҷ�ӽڵ�
            # �ж�ΪҶ�ӽڵ��ǰ������֤·������:
            if not node.left and not node.right and target ==0:
                res.append(path[:])
            else:
                way(node.left,target)
                way(node.right,target)
            path.pop() #�ָ��ֳ�, path���������ȫ��ͳһ����

        way(root,targetSum)
        return res