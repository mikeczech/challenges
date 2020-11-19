
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        length = 0
        current = head
        while current: # O(N) time, O(1) space
            length += 1
            current = current.next 

        if length == 1:
            return True

        mid = math.floor(length / 2)
        i = mid
        current = head
        while i > 1:
            i -= 1
            current = current.next

        if length % 2 == 1:
            current = current.next

        tail = current.next
        while tail and tail.next:
            q = current.next
            current.next = tail.next
            n = tail.next.next 
            tail.next.next = q
            tail.next = n

        p = head
        q = current.next
        i = mid
        while i > 0:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
            i -= 1

        return True




assert Solution().isPalindrome(ListNode(1))
assert Solution().isPalindrome(ListNode(0, ListNode(0)))
assert not Solution().isPalindrome(ListNode(1, ListNode(2)))
assert Solution().isPalindrome(ListNode(1, ListNode(1)))
assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(1))))
assert not Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(1, ListNode(2)))))
assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(1))))))
assert Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))))

