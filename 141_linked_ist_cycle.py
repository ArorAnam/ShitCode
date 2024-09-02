class Cycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if slow == fast:
                return True
            if fast is None and fast.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True


        # Time: O(N)
        # Space: O(1)