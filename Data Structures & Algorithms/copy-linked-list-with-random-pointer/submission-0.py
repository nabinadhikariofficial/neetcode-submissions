"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}

        curr=head
        while curr:
            tmp=Node(curr.val)
            oldToCopy[curr]=tmp
            curr=curr.next
        
        curr=head
        while curr:
            next=curr.next
            random=curr.random
            oldToCopy[curr].next=oldToCopy[next]
            oldToCopy[curr].random=oldToCopy[random]
            curr=curr.next
        
        return oldToCopy[head]