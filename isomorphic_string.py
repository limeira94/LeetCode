"""
    Isomorphic Strings
    Dados dois strings 's' e 't', determine se eles são isomórficos .
    Duas strings 's' e 't' são isomórficas se os caracteres em 's' puderem ser substituídos para obter t.
    Todas as ocorrências de um caractere devem ser substituídas por outro caractere, preservando a ordem dos caracteres. 
    Dois caracteres não podem mapear para o mesmo caractere, mas um caractere pode mapear para si mesmo

    Exemplo 1:
        Input: s = "egg", t = "add"
        Output: true
    Exemplo 2:
        Input: s = "foo", t = "bar"
        output: false
    Exemplo 3:
        Input: s = "paper", t = "title"
        output: true
"""

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d = {}
    e = set()
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                return False
            print(d[s[i]], t[i])
        else:
            if t[i] in e:
                return False
            d[s[i]] = t[i]
            e.add(t[i])
            print(d[s[i]], t[i])
    return True

# Com a função zip
def isIsomorphic2(s, t):
    if len(s) != len(t):
        return False
    d = {}
    for x, y in zip(s, t):
        if x in d and d[x] != y:
            return False
        elif x not in d and y in d.values():
            return False
        d[x] = y
    return True

# Essa função está mais concisa, mas é mais lenta devido a função index()
def isIsomorphic3(s, t):
    return len(s) == len(t) and all(s.index(s[i]) == t.index(t[i]) for i in range(len(s)))


# Funções de Testes
def test_tamanho_dif():
    assert isIsomorphic("egg", "adda") == False


def test_tres_letras():
    assert isIsomorphic("egg", "add") == True
    assert isIsomorphic("foo", "bar") == False
    
def test_quatro_letras(): 
    assert isIsomorphic("paper", "title") == True
    

