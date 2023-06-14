# https://leetcode.com/problems/reverse-linked-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{str(self.val)} -> {str(self.next)}"
def reverseList(head: ListNode) -> ListNode:
    if not head:
        return None
    previous = ListNode(head.val)

    while head.next != None:
        head = head.next
        previous = ListNode(head.val, previous)
    return previous

print(reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))) # 5
print(reverseList(ListNode(1, ListNode(2)))) # 2