from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListLinerly(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None,  head
        # Time complexity: O(n), Memory complexity: O(1)
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverseListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity: O(n), Memory complexity: O(n)
        if not head:
            return None
    
        newHead = head
        if head.next:
            newHead = self.reverseListRecursively(head.next)
            head.next.next = head
        
        head.next= None

        return newHead
    

# Create a linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original:")
while node1:
    print(node1.val)
    node1 = node1.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
reversedList = s.reverseListLinerly(node1)
print("\nLinerly:")
while reversedList:
    print(reversedList.val)
    reversedList = reversedList.next

# reset the linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

reversedList2 = s.reverseListRecursively(node1)
print("\nRecursively:")
while reversedList2:
    print(reversedList2.val)
    reversedList2 = reversedList2.next