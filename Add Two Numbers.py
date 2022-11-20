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

class Node:
    def __init__(self, atual):
        self.atual = atual
        self.proximo = None
        return

    def add_prox(self, prox):
        self.proximo = prox
        return

class LinkedList:
    def __init__(self):       
        self.head = None
        self.tail = None
        return

    def add_node(self, no):
        novo_no = Node(no)
        
        if self.head == None:
            self.head = novo_no
            novo_no.add_prox(None)
        else:
            self.tail.proximo = novo_no
        self.tail = novo_no
        

def addTwoNumbers(l1, l2):
    # criando a lista encadeada
    linked1 = LinkedList.__init__
    linked2 = LinkedList.__init__
    print(linked1)
    print(linked2)

    for i in range(len(l1)-1,-1,-1):
        linked1.add_node(l1[i])
    for i in range(len(l2)-1,-1,-1):
        linked2.add_node(l2[i])
    print(linked1)
    print(linked2)
    return


'''def addTwoNumbers(l1, l2):
    soma1 = ""
    soma2 = ""
    for i in range(len(l1)-1,-1,-1):
        soma1 += str(l1[i])
    for i in range(len(l2)-1,-1,-1):
        soma2 += str(l2[i])

    somaTotal = int(soma1)+int(soma2)
    output = []

    while(somaTotal):
        output.append(somaTotal%10)
        somaTotal = somaTotal//10

    return output'''

print(addTwoNumbers([2,4,3],[5,6,4]))