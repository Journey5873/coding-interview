# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head

        for i in range(n + 1):
            fast = fast.next
            if not fast:
                return head.next

        while fast:
            fast = fast.next 
            slow = slow.next
        slow.next = slow.next.next
        return head

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

sol = Solution()
newHead = sol.removeNthFromEnd(node1, 5)

current = newHead
while current:
    print(current.val)
    current = current.next
