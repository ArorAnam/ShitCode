class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head
    
    # find lenght of the linked list
    current = head
    length = 1
    while current.next:
        current = current.next
        lenght += 1
    
    # optimize k
    k = k % length
    if k == 0:
        return head # no need to rotate
    
    # find the new tail (n - k - 1) and the new head (n - k)
    current.next = head # make it circular temporariliy
    steps_to_new_head = length - k

    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None # break the circular list

    return new_head

    