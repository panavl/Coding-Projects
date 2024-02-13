

#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import sys


class Node():
    # constructor
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):

        if self.lchild != None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild != None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        if self.lchild != None and self.rchild != None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        elif self.lchild != None:
            return 1 + self.lchild.get_height()
        elif self.rchild != None:
            return 1 + self.rchild.get_height()
        else:
            return 1


class Tree():
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.get_height() == 1:
            return 0
        elif self.root == None:
            return None
        else:
            parent = self.root
            curr = self.root
            while curr != None:
                parent = curr
                curr = curr.rchild
            max_num = parent.data
            parent = self.root
            curr = self.root
            while curr != None:
                parent = currS
                curr = curr.lchild
            min_num = parent.data
        return max_num-min_num


    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        level_nodes = []
        if level <= self.get_height():
            self._get_level_nodes(self.root, level, level_nodes)
        else:
            return []
        return level_nodes
    
    def _get_level_nodes(self, node, curr_level, list_nodes):
        if node == None:
            return
        if curr_level == 0:
            list_nodes.append(node.data)
        else:
            self._get_level_nodes(node.lchild, curr_level-1, list_nodes)
            self._get_level_nodes(node.rchild, curr_level-1, list_nodes)


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        left_nodes = []
        self._get_left_side_view(self.root.lchild,left_nodes)
        return left_nodes

    def _get_left_side_view(self,node,list_nodes):
        if node != None:
            list_nodes.append(node.data)
            self._get_left_side_view(node.lchild,list_nodes)
            self._get_left_side_view(node.rchild,list_nodes)
            



    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        return self._get_sum_leaf_nodes(self.root)
    
    def _get_sum_leaf_nodes(self,node):
        if node == None:
            return 0
        if node.lchild == None and node.rchild == None:
            return node.data
        return self._get_sum_leaf_nodes(node.lchild) + self._get_sum_leaf_nodes(node.rchild)
        


  





def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())


    print("Tree range is: ",   t1.range())
    print('level :',   t1.get_level(3))
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
