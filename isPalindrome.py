class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        
        return True


