# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        #find the end the first half and reverse second half
        first_half_end = self.end_of_first_half(head)
     
        second_half_start = self.reverse_list(first_half_end.next)

        #check if it is Palindrome
        result = True
        first_position = head
 
        second_position = second_half_start

        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        #restore the orininal list
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self,head:ListNode) ->ListNode():
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

        #help function to reverse linked list

    def reverse_list(self,head:ListNode) ->ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
