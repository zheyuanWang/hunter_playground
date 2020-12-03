
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def insert_random_pointer(self,node):
        self.random = node
    def info(self):
        print("info:")
        print(self.val)
        if self.next:
            print(self.next.val)
        else: print("no next")
        if self.random:
            print(self.random.val)
        else:
            print("no random")
# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tailNode = None

    # # insertion method for the linked list
    # def insert(self, val):
    #     newNode = Node(val)
    #     if (self.head):
    #         current = self.head
    #         while (current.next):
    #             current = current.next
    #         current.next = newNode
    #     else:
    #         self.head = newNode

    def insert_tail(self,val):
        newNode= Node(val)
        if self.head:
            self.tailNode.next = newNode
            self.tailNode = newNode
        else:
            self.head = newNode
            self.tailNode= newNode


    # print method for the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.val)
            current = current.next

    def massive_init(self,val_list):
        for val in val_list:
            self.insert_tail(val)



class Solution:
    """
    copy: 1->1'->2->2'
    then spilt it into two linked lists
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            origin_head = head
            while head:  # new chain
                new = Node(head.val)
                new.next = head.next
                head.next = new
                head = new.next

            head = origin_head
            while head:  # random chain
                if head.random:
                    head.next.random = head.random.next
                head = head.next.next

            head = origin_head
            result_head = origin_head.next
            pointer = result_head
            while head:  # split chain
                    tmp1 = head
                    head = pointer.next
                    tmp1.next = head

                    tmp2 = pointer
                    if head:
                        pointer = head.next
                    else: #head=None case
                        pointer = None
                    tmp2.next = pointer

            return result_head
        else:  # None input
            return None


    def copyRandomList_2(self, head: 'Node') -> 'Node':
        """
            use a dict to save the nodes, so that in the second loop of "random" the nodes could be found quickly
            it's superior to going through the linked list when dealing with "random",
            but slower than the method of splitting the linked list
            """
        if head:
            result_head = None
            origin_head = head
            tmp = Node(0)
            dic = {}
            while head:  # copy next-part
                new = Node(head.val)
                dic[head] = new
                head = head.next
                if result_head:
                    tmp.next =new
                    tmp = new
                else: # no head jet
                    result_head = new
                    tmp = new

            head = origin_head
            while head:  # copy random-part
                if head.random:
                    dic[head].random = dic[head.random]
                else:
                    dic[head].random = None
                head = head.next
            # attention: None random case
            return result_head
        else:
            return None



# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert_tail(1)
LL.insert_tail(2)
LL.tailNode.insert_random_pointer(LL.tailNode)
LL.insert_tail(3)
#LL.massive_init([4,5,6])
LL.head.insert_random_pointer(LL.tailNode)
#LL.printLL()

solution = Solution()
result = solution.copyRandomList(LL.head)
result.info()
result.next.info()
result.next.next.info()
