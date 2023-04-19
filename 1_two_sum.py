"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
    
"""

def twoSum(nums, target):
    
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d: return [d[r], i]
        d[j] = i



def twoSum2(nums, target):
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

twoSum([2,7,11,15, 22, 4], 33)

def test_1():
    assert twoSum([2,7,11,15], 9) == [0,1]
    
def test_2():
    assert twoSum([3,2,4], 6) == [1,2]
    
def test_3():
    assert twoSum([3,3], 6) == [0,1]

def test_4():
    assert twoSum([3,2,1,5], 6) == [2,3]
    
def test_5():
    assert twoSum([3,2,3], 6) == [0,2]
    
def test_6():
    assert twoSum([2,7,11,15, 22, 4], 33) == [2,4]