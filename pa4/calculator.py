# assignment: PA4
# author: Sebastian Avila
# date: March 6, 2023
# file: calculator.py is a program that calculates an expression given by the user
# input: mathmatical expression
# output: float value and user prompts

from stack import Stack
from tree import *

def infix_to_postfix(infix):
    operators = {'^':3,'*':2,'/':2,'+':1,'-':1}
    s = Stack()
    postfix = ''
    num = ''
    for i in infix:
        if i == '.' or i.isdigit():
            num += i
        else:
            postfix += num + ' ' if num != '' else num
            num = ''  

        if i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix += s.pop() + ' '
            s.pop()
        elif i in operators:
            while s.size() > 0 and s.peek() != '(' and operators[i]<=operators[s.peek()]:
                postfix += s.pop() + ' '
            s.push(i)
    
    postfix += num + ' '
    while s.size() > 0:
        postfix += s.pop() if s.size() == 1 else s.pop() + ' '
    return postfix

def calculate(infix):
    postfix = infix_to_postfix(infix)
    t = ExpTree.make_tree(postfix.split())
    return ExpTree.evaluate(t)


if __name__ == '__main__':
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
     # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    
    print('Welcome to Calculator Program!')    
    while True:
        try:
            userInput  = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
            if userInput == 'quit' or userInput == 'q':
                print('Goodbye!')
                break
            else:
                print(calculate(userInput))
        except:
            print('Please enter a valid expression.')