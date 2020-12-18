# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        mem = None
        if head is None: return None
        while head.next != None:
            point = head.next
            head.next = mem
            head,mem = point,head

        point = head.next
        head.next = mem
        return head

class Solution:
    """
    执行用时：
52 ms
, 在所有 Python3 提交中击败了
24.34%
的用户
内存消耗：
14.5 MB
, 在所有 Python3 提交中击败了
30.16%
的用户
    """
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre= head, None
        while cur:
             cur.next, pre, cur, = pre, cur, cur.next
        return pre