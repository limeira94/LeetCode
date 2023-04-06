""" Dada uma matriz de inteiros nums, calcule o índice pivô dessa matriz.
    O índice pivô é o índice onde a soma de todos os números estritamente à esquerda do índice 
    é igual à soma de todos os números estritamente à direita do índice.
    Se o índice estiver na borda esquerda da matriz, a soma esquerda é 0porque não há elementos à esquerda. 
    Isso também se aplica à borda direita da matriz.
    Retorna o índice de pivô mais à esquerda . Se tal índice não existir, retorne -1.

Exemplo 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explicação:
        O índice 3 é o pivô.
        Soma esquerda = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
        Soma direita = nums[4] + nums[5] = 5 + 6 = 11
Exemplo 2:
    Input: nums = [1,2,3]
    Output: -1
    Explicação:
        Não há índice que satisfaça as condições do índice pivô.
Exemplo 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explicação:
        O índice 0 é o pivô.
        Somas esquerda = 0 (não há elementos à esquerda)
        Soma direita = nums[1] + nums[2] = 1 + -1 = 0
"""

def pivotIndex(nums):
    total = sum(nums) # O(n)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        print(f"leftSum: {leftSum} rightSum: {rightSum} total: {total} nums[i]: {nums[i]}")
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1
            

    
def test_1():
    assert pivotIndex([1,7,3,6,5,6]) == 3

def test_2():
    assert pivotIndex([1,2,3]) == -1

def test_3():
    assert pivotIndex([2,1,-1]) == 0
    
print(pivotIndex([1,7,3,6,5,6]))

