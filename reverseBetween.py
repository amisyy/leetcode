# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head
        Node0 = ListNode(0)
        Node0.next = head
        temp1 = Node0
        for i in range(m-1):
            temp1 = temp1.next
        cur = temp1.next
        reverse = None
        for i in range(n-m+1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = nex49
        temp1.next.next = cur
        temp1.next = reverse
        return Node0.next





u = Solution()



test = [
"1001",
"101",
"1234",
"1326",
"1226",
"3416352693542631413"
]

for x in test:
    print(u.numDecodings(x))




