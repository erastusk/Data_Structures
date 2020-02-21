""" Binary Tree Insert and Search """

class Node():
    """ Node definition """
    def __init__(self,data):
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
        
    def search_BTS(self, data):
        """Search Function"""
        root_node = self.root
        if data > root_node.data:
            """ if greater then root right else left"""
            return self.search(data, root_node, "right")
        return self.search(data, root_node, "left")
    
    def search(self, data, root_node, direction):
        """Search Helper Function"""
        if direction == "right":
            if root_node is None:
                return False
            if root_node.data == data:
                return True
            return self.search(data, root_node.right, "right")
        elif direction == "left":
            if root_node is None:
                return False
            if root_node.data == data:
                return True
            return self.search(data, root_node.left, "left")
        return False
    
    def insert_BTS(self, data):
        """ Insert node """
        insert_node = Node(data)
        if not self.root:
            self.root = insert_node
            return
        self.insert_(insert_node, self.root)
        
    def insert_(self, insert_node, root_node):
        """ recursion insert method """
        if root_node.right is None:
            root_node.right = insert_node
        elif insert_node.data == root_node.data:
            print "Node already exists"
        elif root_node.left is None:
            root_node.left = insert_node
        elif insert_node.data > root_node.data:
            return self.insert_(insert_node, root_node.right)
        elif insert_node.data < root_node.data:
            return self.insert_(insert_node, root_node.left)
        
    def print_preorder(self):
        """Print Binary Tree using Preorder traversal"""
        print(self.print_order(self.root, ""))
        
    def print_order(self, curr_node, traverse):
        """Print helper function"""
        if curr_node:
            traverse += str(curr_node.data) + "->"
            traverse = self.print_order(curr_node.left, traverse)
            traverse = self.print_order(curr_node.right, traverse)
        return traverse   
