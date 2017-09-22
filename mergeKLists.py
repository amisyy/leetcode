# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        newList_head = ListNode(0)
        newList = newList_head
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
        if list1 is not None:
            newList.next = list1
            return newList_head.next
        if list2 is not None:
            newList.next = list2
            return newList_head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return lists
        if length == 1:
            return lists[0]
        list_local = lists[0]

        i = 1
        while i < length:
            list_local = self.mergeTwoLists(list_local, lists[i])
            i+=1
        return list_local


u = Solution()
n1 = ListNode(1)
n2 = ListNode(3)
n1.next = n2

n3 = ListNode(2)
n4 = ListNode(4)
n3.next = n4
print(ListNode(None) is None)
print(u.mergeKLists([n1,n3]).next.next.next.val)
