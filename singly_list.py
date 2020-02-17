""" Singly link list """
#from __future__ import print_function


class _Node():
    """
    Node Instantiation with a value and pointer
    """
    def __init__(self, val):
        self.val = val
        self.next = None
class Linkedlist():
    """
    Linked instantiation with a head
    """
    data = []
    def __init__(self):
        self.head = None
    def append(self, val):
        """
        Add a node to the end of a linked list
        """
        if val in self.data:
            print("{} already exixts".format(val))
            return
        self.data.append(val)
        node = _Node(val)
        if self.head is None:
            self.head = node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node
    def prepend(self, val):
        """
        Add a node to the beginning of a linked list
        """
        node = _Node(val)
        node.next = self.head
        self.head = node
        return
    def insert(self, insval, befval):
        """
        Insert a node before a given node
        """
        node = _Node(insval)
        curr_node = self.head
        if befval not in self.data:
            print("Given insert before node with a value of {} doesn't not exist".format(befval))
            return
        while curr_node.next:
            if curr_node.val == befval:
                before_node = curr_node
                after_node = curr_node.next
                break
            curr_node = curr_node.next
        if not curr_node.next:
            curr_node.next = node
            return
        before_node.next = node
        node.next = after_node
    def delete(self, val):
        """
        Delete a node
        """
        if val not in self.data:
            print("Node with value {} is Not in list".format(val))
            return
        curr_node = self.head
        if curr_node.val == val:
            self.head = curr_node.next
            curr_node = None
            return
        next_node = prev_node = None
        while curr_node:
            if curr_node.next.val == val:
                prev_node = curr_node
                curr_node = curr_node.next
                next_node = curr_node.next
                prev_node.next = next_node
                return
            curr_node = curr_node.next
    def node_swap(self, val1, val2):
        """
        a->b->c->d->e->f
        If swapping b and d:
        4 Items will need to be swapped.
            b.next and d.next --- pointers to node instances
            b.prev and d.prev --- pointers to pointers
        """
        if val1 == val2:
            print("Same nodes, nothing to swap")
            return
        if val1 not in self.data:
            print("Node {} is not in the linked lists".format(val1))
            return
        if val2 not in self.data:
            print("Node {} is not in the linked lists".format(val2))
            return
        prev1 = curr1 = prev2 = curr2 = None
        curr_node = self.head
        while curr_node:
            if curr_node.next and curr_node.next.val == val1:
                prev1 = curr_node
                curr1 = curr_node.next
            if curr_node.val == val1:
                curr1 = curr_node
            curr_node = curr_node.next
        curr_node = self.head
        while curr_node:
            if curr_node.next and curr_node.next.val == val2:
                prev2 = curr_node
                curr2 = curr_node.next
            curr_node = curr_node.next
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next
    def reverse_list_iterative(self):
        """reverse a link list using iteration """
        prev = nextnode = None
        curr_node = self.head
        while curr_node:
            nextnode = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nextnode
        self.head = prev
    def reverse_list_recursive(self):
        """reverse a link list using recursion """
        prev = None
        curr_node = self.head
        def rev_rec(curr_node, prev):
            """ recursive method """
            if not curr_node:
                return prev
            nextnode = curr_node.next
            curr_node.next = prev
            prev = curr_node
            return rev_rec(nextnode, prev)
        self.head = rev_rec(curr_node, prev)
    def print_list(self):
        """
        Print values of linked lists
        """
        curr_node = self.head
        while curr_node:
            print curr_node.val, "->",
            curr_node = curr_node.next
