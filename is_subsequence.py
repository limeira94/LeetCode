
"""
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
    of the characters without disturbing the relative positions of the remaining characters. 
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Exemplo 1:
        Input: s = "abc", t = "ahbgdc"
        Output: true
        
    Exemplo 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false
"""

def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    count = 0
    if s == "":
        return True
    for i in range(len(s)):
        if s[i] in t:
            count += 1
            t = t[t.index(s[i])+1:]
            if count == len(s):
                return True
        else:
            return False

def isSubsequence2(s, t):
    if not s:
        return True
    last_index = -1
    for letter in s:
        last_index = t.find(letter, last_index + 1)
        print(letter, last_index)
        if last_index == -1:
            return False
    return True


def test_abc():
    assert isSubsequence("abc", "ahbgdc") == True
    
def test_axc():
    assert isSubsequence("axc", "ahbgdc") == False

def test_aec():
    assert isSubsequence("aec", "abcde") == False

def test_vazio():
    assert isSubsequence("", "abcde") == True