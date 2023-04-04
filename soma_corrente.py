"""
    Dado um array nums. Definimos uma soma corrente de uma matriz como  runningSum[i] = sum(nums[0]…nums[i]).
    Retorne a soma corrente de nums.
    
    Exemplo 1:
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
    
    Exemplo 2:
        Input: nums = [1,1,1,1,1]
        Output: [1,2,3,4,5]
        
    Exemplo 3:
        Input: nums = [3,1,2,10,1]
        Output: [3,4,6,16,17]
"""

class Solution():
 
    def runningSum(self, nums: list[int]) -> list[int]:
            lista = [nums[0]]
            for i in range(1, len(nums)):
                nums[i] += nums[i-1]
                lista.append(nums[i])
            return lista


    def test_dois_elementos(self):
        assert self.runningSum([1, 1]) == [1, 2]
        assert self.runningSum([1, 2]) == [1, 3]
        
    def test_tres_elementos(self):
        assert self.runningSum([1, 1, 1]) == [1, 2, 3]
        assert self.runningSum([1, 2, 3]) == [1, 3, 6]

    def test_quatro_elementos(self):
        assert Solution.runningSum([1, 1, 1, 1]) == [1, 2, 3, 4]
        assert Solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]

    def test_cinco_elementos(self):
        assert self.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
        assert self.runningSum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
