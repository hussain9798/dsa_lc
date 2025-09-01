# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Function to add two numbers represented by linked lists.
        Each node contains a single digit, and digits are stored in reverse order.
        Returns the sum as a new linked list.
        """

        ls1 = []  # store digits of first number
        ls2 = []  # store digits of second number

        # Traverse the first linked list and collect digits
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
        
        # Traverse the second linked list and collect digits
        while l2:
            ls2.append(l2.val)
            l2 = l2.next

        # Reverse and convert list of digits to integer
        ls1 = int(''.join(map(str, ls1[::-1])))
        ls2 = int(''.join(map(str, ls2[::-1])))

        # Add the two numbers
        res = ls1 + ls2

        # Convert sum into list of digits (reversed)
        res = [int(d) for d in str(res)]
        res.reverse()

        # Build resulting linked list
        head = ListNode(res[0])
        curr = head
        for i in res[1:]:
            curr.next = ListNode(i)
            curr = curr.next

        return head


# ---------- Main Function for Testing ----------
def printLinkedList(node):
    """Helper function to print linked list."""
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

def main():
    # Create first number: 342 (represented as 2 -> 4 -> 3)
    l1 = ListNode(2, ListNode(4, ListNode(3)))

    # Create second number: 465 (represented as 5 -> 6 -> 4)
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    # Add the two numbers
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print result: expected 807 (7 -> 0 -> 8)
    print("Resultant Linked List:")
    printLinkedList(result)


# Run main function
if __name__ == "__main__":
    main()
