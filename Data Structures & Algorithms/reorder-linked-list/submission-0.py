# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        index = 0
        step = 1
        temp = head
        n = len(arr)

        while temp:
            if step % 2 == 0:
                temp.val = arr[n - index - 1]
                index +=1
            else:
                temp.val = arr[index]

            step += 1
            temp = temp.next
    


        