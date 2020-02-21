""" 
Binary Tree Search
        
            8
     /               \  
    3                 10
 /     \          /         \
 1      6        9          11 
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
   
    def search_BTS(self, data):
        root_node = self.root
        
        if data > root_node.data:
            """ if greater then root right else left"""
            return self.search(data, root_node, "right")
        else:
            return self.search(data, root_node, "left")
        
    def search(self, data, root_node, direction):
        if direction == "right":
            if root_node == None:
                return False
            if root_node.data == data:
                return True
            else:
                return self.search(data, root_node.right, "right")

        elif direction == "left":
            if root_node == None:
                return False
            if root_node.data == data:
                return True
            else:
                return self.search(data, root_node.left, "left")
        else:
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
        if root_node.right == None:
            root_node.right = insert_node
            return
        if insert_node.data == root_node.data:
            print "Node already exists"
            return 
        if root_node.left == None:
            root_node.left = insert_node
            return
        if insert_node.data > root_node.data:
            return self.insert_(insert_node, root_node.right)
        elif insert_node.data < root_node.data:
            return self.insert_(insert_node, root_node.left)
    
    def print_preorder(self):
        print(self.print_order(self.root, ""))
    def print_order(self, curr_node, traverse):
        if curr_node:
            traverse += str(curr_node.data) + "->"
            traverse = self.print_order(curr_node.left, traverse)
            traverse = self.print_order(curr_node.right, traverse)
        return traverse   

