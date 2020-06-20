#-*- coding:utf-8 -*-
#Author:李明洲
#@Time:2020/6/3 10:13

#二叉树基本实现

from pybst.bstree import BSTree
from pybst.draw import plot_tree
from linear_structure_Stack import Stack
import operator

# class Node:
#     def __init__(self, value=-1, left=None, right=None):
#         self.value = value
#         self.lchild = left  # 左子树
#         self.rchild = right  # 右子树
#
# class Tree:
#     """树类"""
#     def __init__(self):
#         self.root = Node()
#         self.myQueue=[]
#
#     def add(self, elem):
#         node = Node(elem)
#         if self.root.value==-1:
#             self.root=node
#             self.myQueue.append(self.root)
#         else:
#             treeNode=self.myQueue[0]
#             if treeNode.lchild==None:
#                 treeNode.lchild=node
#                 self.myQueue.append(treeNode.lchild)
#             else:
#                 treeNode.rchild=node
#                 self.myQueue.append(treeNode.rchild)
#                 self.myQueue.pop(0)
#
# def front_stack(root):
#     if root ==None:
#         return
#     myQueue=[]
#     node=root
#     myQueue.append(node)
#     while(myQueue):
#         checknode=myQueue.pop(0)
#         print(checknode.value)
#         if checknode.lchild !=None:
#             myQueue.append(checknode.lchild)
#         if checknode.rchild != None:
#             myQueue.append(checknode.rchild)

##############################################
###############################################
#二叉树的可视化
# if __name__ == '__main__':
#     # elems=range(10)
#     # tree=Tree()
#     # for elem in elems:
#     #     tree.add(elem)
#     #
#     # front_stack(tree.root)
#     tree=BSTree()
#     tree.insert(90, '')
#     node_90 = tree.get_node(90)
#     tree.insert(50, '', node_90)
#     tree.insert(150, '', node_90)
#
#     node_50 = tree.get_node(50)
#     tree.insert(20, '', node_50)
#     tree.insert(75, '', node_50)
#
#     node_20 = tree.get_node(20)
#     tree.insert(5, '', node_20)
#     tree.insert(25, '', node_20)
#
#     node_75 = tree.get_node(75)
#     tree.insert(66, '', node_75)
#     tree.insert(88, '', node_75)
#     tree.insert(98, '', node_75)
#     plot_tree(tree)

##################################################
##################################################
#树的嵌套列表实现
# def BinaryTree(r):
#     return [r,[],[]]
#
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch,[],[]])
#     return root
#
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2, [newBranch, [], t])
#     else:
#         root.insert(2, [newBranch, [], []])
#
#     return root
#
# def getRootVal(root):
#     return root[0]
#
# def setRootVal(root,newVal):
#     root[0] = newVal
#
# def getLeftChild(root):
#     return root[1]
#
# def getRightChild(root):
#     return root[2]
#
# r = BinaryTree(3)
# insertLeft(r,4)
# insertLeft(r,5)
# insertRight(r,6)
# insertRight(r,7)
# l = getLeftChild(r)
# print(l)
#
# setRootVal(l,9)
# print(r)
# insertLeft(l,11)
# print(r)
# print(getRightChild(getRightChild(r)))

##############################################
##############################################
#二叉树的链表实现
class BinatryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinatryTree(newNode)
        else:
            t = BinatryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRootVal(self):
        return self.key

    def setRootVal(self,obj):
        self.key = obj

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
    #前序
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
#前序
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
#后序
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
#中序
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())



#######################################
#######################################
#二叉树的应用
#解析树（语法树）
#表达式解析

def buildParseTree(fpexp):
    fplist = fpexp
    pStack = Stack()
    eTree = BinatryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add,'-':operator.sub,
             '*':operator.mul,'/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return  parseTree.getRootVal()

#基于后序遍历来求值
def postevaluate(tree):
    opers = {'+':operator.add,'-':operator.sub,
             '*':operator.mul,'/':operator.truediv}

    res1 = None
    res2 = None
    if tree:
        res1 = postevaluate(tree.getLeftChild())
        res2 = postevaluate(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()


fpexp = ['(','3','+','(','4','*','5',')',')']
parseTree = buildParseTree(fpexp)
print(evaluate(parseTree))