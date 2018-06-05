# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        pointer = head
        num = 1
        while not pointer.next is None:
            pointer = pointer.next
            num += 1
        pointer.next = head
        # temp_num = 10
        # while temp_num>0:
        #     print(pointer.val)
        #     pointer = pointer.next
        #     temp_num -= 1
        # return
        num -= k%num
        while num > 0:
            pointer = pointer.next
            num -= 1
        result = pointer.next
        pointer.next = None
        return result

u = Solution()

test = [
    1


]
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p4.next = p5
p3.next = p4
p2.next = p3
p1.next = p2
for x in test:
    print(u.rotateRight(p1,2))
a = u.rotateRight(p1,2)
print("a")
while not a.next is None:
    print(a.val)
    a = a.next
