"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

def addTwoNumbers(l1, l2):
    soma1 = ""
    soma2 = ""
    for i in range(len(l1)-1,-1,-1):
        soma1 += str(l1[i])
    for i in range(len(l2)-1,-1,-1):
        soma2 += str(l2[i])

    somaTotal = int(soma1)+int(soma2)
    print(somaTotal)
    output = []

    while(somaTotal):
        print(somaTotal%10)
        output.append(somaTotal%10)
        somaTotal = somaTotal//10

    return output

print(addTwoNumbers([0],[0]))