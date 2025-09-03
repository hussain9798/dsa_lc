# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Swap every two adjacent nodes in the linked list.
        """
        # Dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Traverse while there are at least two nodes to swap
        while head and head.next:
            # Identify the two nodes to be swapped
            first = head
            second = head.next

            # Perform the swap
            prev.next = second        # Previous points to second
            first.next = second.next  # First points to node after second
            second.next = first       # Second points back to first

            # Move prev and head forward for the next pair
            prev = first
            head = first.next

        # Return the new head
        return dummy.next

# Helper function to convert list to linked list
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to convert linked list back to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main function to test the solution
if __name__ == "__main__":
    # Example input
    values = [1, 2, 3, 4]
    head = build_linked_list(values)

    # Run the solution
    solution = Solution()
    new_head = solution.swapPairs(head)

    # Print output as list
    print("Output:", linked_list_to_list(new_head))
