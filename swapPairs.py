# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        point = ListNode(0)
        save = point
        point.next = head
        while point.next is not None and point.next.next is not None:
            temp1 = point.next.next.next
            temp2 = point.next.next
            point.next.next.next = point.next
            point.next.next = temp1
            point.next = temp2
            point = point.next.next
        return save.next




n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2

n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
u = Solution()
print(u.swapPairs(n1).next.next.next.val)
