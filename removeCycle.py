# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None or head.next is None:
            return
        fast = head
        slow = head
        flag = False
        while fast.next is not None and fast.next.next is not None :
            fast = fast.next.next
            slow = slow.next
            if (fast==slow):
                flag = True
                break
        point1 = fast
        point2 = head
        if flag:
            while not point1==point2:
                point1 = point1.next
                point2 = point2.next
            return point1
        return


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2

n3 = ListNode(3)
n2.next = n3
n4 = ListNode(4)
n3.next = n4
u = Solution()
print(u.hasCycle(n1))
