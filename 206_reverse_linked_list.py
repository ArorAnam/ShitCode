# given the head of a single linked list
# reverse the linked list

class Revering:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

        # Time: O(N)
        # Space: O(1)