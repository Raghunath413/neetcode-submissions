# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prive=None;
        if head ==None:
            return head;
        
        current=head;
        nextnode=head.next;
        while current:
            nextnode=current.next;
            current.next=prive;
            prive=current;
            current=nextnode;
        return prive;    

        