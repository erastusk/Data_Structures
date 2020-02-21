"""Binary Tree Traversal """
class Node():
    """ Node definition """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree():
    """ Binary Tree definition """
    def __init__(self, data):
        self.root = Node(data)
        self.pre = ""
        self.ino = ""
        self.post = ""
    def preorder(self, start):
        """Root->Left->Right
        Node->Left->Right"""
        if start:
            self.pre += str(start.data) + "->"
            self.preorder(start.left)
            self.preorder(start.right)
    def inorder(self, start):
        """Left->Root->Right
        Left->Node->Right"""
        if start:
            self.inorder(start.left)
            self.ino += str(start.data) + "->"
            self.inorder(start.right)
    def postorder(self, start):
        """Left->Right->Root
        Left->Right->Node"""
        if start:
            self.postorder(start.left)
            self.postorder(start.right)
            self.post += str(start.data) + "->"
