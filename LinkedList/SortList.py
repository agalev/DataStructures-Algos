# https://leetcode.com/problems/sort-list/description/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{str(self.val)} -> {str(self.next)}"
    
def sortList(head: ListNode) -> ListNode:
    hash_map = {}
    index = 0

    while head:
        hash_map[head.val, index] = head
        head = head.next
        index += 1
    sorted_keys = sorted(list(hash_map.keys()))

    for i in range(len(sorted_keys)):
        if i != len(sorted_keys)-1:
            hash_map[sorted_keys[i]].next = hash_map[sorted_keys[i+1]]
        else:
            hash_map[sorted_keys[i]].next = None
            
    if hash_map:
        return hash_map[sorted_keys[0]]
    else:
        return None
    
print(sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))) # 1 -> 2 -> 3 -> 4
print(sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))))) # -1 -> 0 -> 3 -> 4 -> 5
print(sortList(ListNode())) # None