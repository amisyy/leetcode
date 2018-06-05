# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp = head
        while temp is not None:
            if temp.next is None:
                break
            elif temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
u = Solution()
l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)

l2.next = l3
l1.next = l2
test = [
    1
]
for x in test:
    print(u.deleteDuplicates(l1))




