class ListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

n = int(input())

for _ in range(n):
    pwdList = ListNode()
    head = pwdList
    pwd = list(input())

    for char in pwd:
        if char == "<":
            if pwdList.prev:
                pwdList = pwdList.prev
        elif char == ">":
            if pwdList.next:
                pwdList = pwdList.next
        elif char == "-":
            if pwdList.prev:
                prevNode = pwdList.prev
                nextNode = pwdList.next

                prevNode.next = nextNode
                if nextNode:
                    nextNode.prev = prevNode
                pwdList = prevNode
        else:
            newNode = ListNode(char)
            nextNode = pwdList.next

            # If there is a nextNode
            if nextNode:
                nextNode.prev = newNode
            newNode.next = nextNode

            pwdList.next = newNode
            newNode.prev = pwdList
            pwdList = newNode
        
    current = head.next
    while current:
        print(current.val, end="")
        current = current.next
    print()