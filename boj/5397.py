import sys

class ListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

n = int(sys.stdin.readline())

for _ in range(n):
    pwd = list(input())
    pwd_list = ListNode()
    dummy_head = pwd_list

    for char in pwd:
        if char == "<":
            if pwd_list.prev:
                pwd_list = pwd_list.prev
        elif char == ">":
            if pwd_list.next:
                pwd_list = pwd_list.next
        elif char == "-":
            if pwd_list.prev:
                prev_node = pwd_list.prev
                next_node = pwd_list.next

                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                pwd_list = prev_node
        else:
            new_node = ListNode(char)
            next_node = pwd_list.next

            new_node.next = next_node
            new_node.prev = pwd_list
            if next_node:
                next_node.prev = new_node

            pwd_list.next = new_node
            pwd_list = new_node

    current = dummy_head.next
    while current:
        print(current.val, end="")
        current = current.next
    print()

