# --------------------
# HASH MAP APPROACH
# -------------------- 

class Node:
    def __init__(self, node_val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(node_val)
        self.next = next
        self.random = random

# Time: O(N) -> twice pass
# Space: O(n) - extra for the map in dictionary
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None
    dummy = new = Node(-1)
    curr = head
    old_new = {}

    # Genrate a new list / hash old -> new
    while curr:
        new.next = Node(curr.val)
        old_new[curr] = new.next
        curr = curr.next
        new = new.next

    # Now we have a new list with dummy.next pointed to the head of new

    curr = head
    new = dummy.next

    # Update new list with new nodes for random
    while curr:
        if curr.random:
            new.random = old_new[curr.random]
        curr = curr.next
        new = new.next
    
    return dummy.next


# -----------------------------
# LIST INTERWAEVING APPROACH
# -----------------------------

# Time: O(N) -> once pass
# Space: O(1)
def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None
    dummy = Node(-1)
    dummy.next = head
    curr = head

    # stage one: interweave
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = temp.next

    curr = head
    # stage two: update random
    while curr:
        if curr.random:
            curr.next.random = curr.random.next # random.next is thew new node
        curr = curr.next.next   # mode to next and the next

    curr = dummy    # dummy is head of new list at the moment
    old = head
    # stage three, remove old nodes 
    while old:
        curr.next = old.next    # head next will be new list
        curr = old
        old = curr.next

    return dummy.next


# -----------------------------
# RECURSIVE HASHMAP APPROACH
# Clever way of avoiding creating new nodes
# -----------------------------

# Time: O(N) -> once pass
# Space: O(n) - extra for the map in dictionary
class LinkedListOperations:
    map = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.map:
            return self.map[head]

        newNode = Node(head.val)
        self.map[head] = newNode
        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)
        return newNode
