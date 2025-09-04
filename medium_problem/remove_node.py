# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # store value of node
        self.next = next      # pointer to next node

class Solution:
    def removeNthFromEnd(self, head, n: int):
        # Create a dummy node that points to the head (helps handle edge cases easily)
        dummy = ListNode(0, head)

        # Step 1: Find the total length of the linked list
        length = 0
        temp = head
        while temp is not None:
            length += 1
            temp = temp.next

        # Step 2: Traverse again until reaching the node before the one to delete
        curr = dummy
        for _ in range(length - n):  # move (length-n) steps
            curr = curr.next

        # Step 3: Remove the nth node from end by skipping it
        curr.next = curr.next.next

        # Step 4: Return the new head (dummy.next handles edge case of deleting first node)
        return dummy.next


# --------------------- MAIN FUNCTION ---------------------
if __name__ == "__main__":
    # Helper function to create linked list from Python list
    def create_linked_list(values):
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Helper function to print linked list
    def print_linked_list(head):
        while head:
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next

    # Example Usage
    values = [1, 2, 3, 4, 5]   # input linked list
    n = 2                      # remove 2nd node from end

    head = create_linked_list(values)
    print("Original List:")
    print_linked_list(head)

    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)

    print(f"List after removing {n}th node from end:")
    print_linked_list(new_head)
