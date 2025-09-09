# Define a Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data        # store node value
        self.next = None        # pointer to the next node (default None)

# Function to detect if a linked list has a cycle
def cycle(head):
    slow = fast = head          # initialize both slow and fast pointers at head
    while fast and fast.next:   # loop until fast reaches end (no cycle) or detects one
        slow = slow.next        # move slow pointer one step
        fast = fast.next.next   # move fast pointer two steps
        if slow == fast:        # if they meet → cycle detected
            return True
    return False                # if loop ends, no cycle found

if __name__ == "__main__":
    # Create linked list: 2 → 3 → 0 → -4 → None
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    
    # Detect cycle
    res = cycle(head)
    print(res)   # Output: False (no cycle)
