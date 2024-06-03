# assignment: PA4
# author: Sebastian Avila
# date: March 6, 2023
# file: tree.py is a program that implements a binary tree and an expression tree
# input: tree root object
# output: binary tree or expression tree

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNodeVal):
        if self.rightChild == '':
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s 

class ExpTree(BinaryTree):

    def make_tree(postfix):
        s = Stack()
        operators = ['^','*','/','+','-']
        for i in postfix:
            if i in operators:
                temp_tree = ExpTree(i)
                temp_tree.insertRight(s.pop())
                temp_tree.insertLeft(s.pop())
                s.push(temp_tree)
            else:
                s.push(ExpTree(i))
        return s.pop()

    def preorder(tree):
        s = ''
        if tree != None:
            s = str(tree.getRootVal())
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s 

    def inorder(tree):
        operators = ['^','*','/','+','-']
        s = ''
        if tree != None:
            if tree.getRootVal() in operators:
                s+='('
            s += ExpTree.inorder(tree.getLeftChild())
            s += str(tree.getRootVal())
            s += ExpTree.inorder(tree.getRightChild())
            if tree.getRootVal() in operators:
                s+=')'
        return s 
      
    def postorder(tree):
        s = ''
        if tree != None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += str(tree.getRootVal())
        return s 

    def evaluate(tree):
        if tree == None:
            return 0
        
        if tree.getLeftChild() == None and tree.getRightChild() == None:
            return float(str(tree.getRootVal()))
        
        x = ExpTree.evaluate(tree.getLeftChild().getRootVal())
        y = ExpTree.evaluate(tree.getRightChild().getRootVal())

        if str(tree.getRootVal()) == '+':
            return x + y
        elif str(tree.getRootVal()) == '-':
            return x - y
        elif str(tree.getRootVal()) == '*':
            return x * y
        elif str(tree.getRootVal()) == '/':
            return x / y
        elif str(tree.getRootVal()) == '^':
            return x ** y

    def __str__(self):
        return self.inorder()
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    print(postfix)
    print(tree)
    #print(ExpTree.postorder(tree))
    #print(ExpTree.preorder(tree))
    #assert str(tree) == '(5+(2*3))'
    print(ExpTree.evaluate(tree))
   # assert ExpTree.inorder(tree) == '(5+(2*3))'
   # assert ExpTree.postorder(tree) == '523*+'
   # assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    #assert str(tree) == '((5+2)*3)'
   # assert ExpTree.inorder(tree) == '((5+2)*3)'
    #assert ExpTree.postorder(tree) == '52+3*'
    #assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    
    
