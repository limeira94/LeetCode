"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList2(self, head):
        new_list = None
        current = head
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list

def reverseList(head):
    if len(head) == 0:
        return []
    return head[::-1]


def test_reverse():
    assert reverseList([1,2,3,4,5]) == [5,4,3,2,1]
    assert reverseList([1,2]) == [2,1]
    
def test_empty():
    assert reverseList([]) == []
    