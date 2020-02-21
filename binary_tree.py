""" 
Binary Tree Traversals
Depth First Search - Pre, In and Postorder
Using notation n-node, l-left and r-right,
pre - nlr
in - lnr
post - lrn

On each node perform each check, eg post - lrn
starting from root node 10
do l, to 2, do l on 2 to 11
on 11 do l, is null next do r is null next is n, print node
go back to 2, l done do r to 12, l and r are null print node
go back to 2, l and r done, n left, print node go back to 10
l done do r, etc

Pre
10->2->11->12->6->2->20->

In
11->2->12->10->2->6->20->

Post
11->12->2->2->20->6->10->
        
            10
     /               \  
    2                 6
 /     \          /         \
 11     12        2         20 
"""
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, data):
        self.root = Node(data)
        self.pre = ""
        self.ino = ""
        self.post = ""
    
    def preorder(self, start):
        """Root->Left->Right"""
        """Node->Left->Right"""
        if start:
            self.pre += str(start.data) + "->"
            self.preorder(start.left)
            self.preorder(start.right)

    def inorder(self, start):
        """Left->Root->Right"""
        """Left->Node->Right"""
        if start:
            self.inorder(start.left)
            self.ino += str(start.data) + "->"
            self.inorder(start.right)

    def postorder(self, start):
        """Left->Right->Root"""
        """Left->Right->Node"""
        if start:
            self.postorder(start.left)
            self.postorder(start.right)
            self.post += str(start.data) + "->"
