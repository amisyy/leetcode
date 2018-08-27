class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        temp = ListNode(0)
        head = temp

        while pHead1 is not None or pHead2 is not None:
            if pHead1 is not None and pHead2 is not None:
                if pHead1.val < pHead2.val:
                    tmp_node = ListNode(pHead1.val)
                    pHead1 = pHead1.next
                else:
                    tmp_node = ListNode(pHead2.val)
                    pHead2 = pHead2.next
            elif pHead1 is not None:
                tmp_node = ListNode(pHead1.val)
                pHead1 = pHead1.next
            else:
                tmp_node = ListNode(pHead2.val)
                pHead2 = pHead2.next
            temp.next = tmp_node
            temp = temp.next
        return head

pHead1 = ListNode(1)
p2 = ListNode(3)
p3 = ListNode(5)
pHead1.next = p2
pHead1.next.next = p3

pHead2 = ListNode(2)
p2 = ListNode(4)
p3 = ListNode(6)
pHead2.next = p2
pHead2.next.next = p3

u = Solution()
print(u.Merge(pHead1,pHead2))
