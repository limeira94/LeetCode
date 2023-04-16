"""
    You are given the heads of two sorted linked lists list1 and list2
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    Example1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
    Example2:
        Input: list1 = [], list2 = []
        Output: []
    Example3:
        Input: list1 = [], list2 = [0]
        Output: [0]
"""

def mergeTwoLists(list1, list2):
    return sorted(list1 + list2)

def mergeTwoLists2(list1, list2):
    mergeList = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            mergeList.append(list1[i])           
            i += 1
        else:
            mergeList.append(list2[j])
            j += 1
    while i < len(list1):
        mergeList.append(list1[i])
        i += 1
    while j < len(list2):
        mergeList.append(list2[j])
        j += 1
    return mergeList
    
    
def test_merge():
    assert mergeTwoLists([1,2,4], [1,3,4]) == [1,1,2,3,4,4]
    
def test_empty():
    assert mergeTwoLists([], []) == []

def test_empty2():
    assert mergeTwoLists([], [0]) == [0]