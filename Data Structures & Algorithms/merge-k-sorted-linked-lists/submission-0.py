# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwolists(self, l1, l2):
        dummy = ListNode()
        curr=dummy
        while l1 and l2:
            if l1.val>l2.val:
                curr.next=l2
                l2=l2.next
            else:
                curr.next=l1
                l1=l1.next
            curr=curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range(1,len(lists)):
            lists[i]=self.mergeTwolists(lists[i],lists[i-1])
        return lists[len(lists)-1]