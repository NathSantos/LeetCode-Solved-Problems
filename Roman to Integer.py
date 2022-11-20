"""
Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.


Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
"""

def romanToInt(s):
    dic_valores = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    numero = 0
    i = 0

    while(i < len(s)):
        if(i == len(s)-1):  # tratando o caso do último elemento da string (evitando IndexError)
            numero += dic_valores[s[i]]
            i+=1
        else:
            if(dic_valores[s[i]] >= dic_valores[s[i+1]]):   # se o valor da letra atual for maior ou igual ao valor da próxima letra
                numero += dic_valores[s[i]]                 # adiciona o valor da letra atual e soma +1 pulando para a próxima
                i+=1
            else:                                                   # caso contrário,
                numero += (dic_valores[s[i+1]] - dic_valores[s[i]]) # adiciona a diferença do valor da próxima letra pelo valor da atual
                i+=2                                                # e soma +2, pulando as duas letras lidas
    return numero

print(romanToInt("LVIII"))