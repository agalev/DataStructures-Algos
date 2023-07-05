# https://leetcode.com/problems/add-two-numbers/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{str(self.val)} -> {str(self.next)}"
    
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    int1 = 0
    int2 = 0
    multiplier = 1
    while l1 or l2:
        if l1:
            int1 += multiplier * l1.val
            l1 = l1.next
        if l2:
            int2 += multiplier * l2.val
            l2 = l2.next
        multiplier *= 10
    result = list(str(int1+int2))
    prev = None
    while len(result) > 0:
        head = ListNode(result[0], prev)
        prev = head
        result.pop(0)
    return head

print(addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))) # 7 -> 0 -> 8
print(addTwoNumbers(ListNode(0), ListNode(0))) # 0
print(addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))) # 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1