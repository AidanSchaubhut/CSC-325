# The implementation of some functions were from the help
# of Trisha Carter. She helped with the logic behind some functions

import sys

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance = 0, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def getBalance(self):
            return self.balance
        def setBalance(self, balance):
            self.balance = balance
        def __repr__(self):
            return f"AVLNode({repr(self.item)}, balance = {repr(self.balance)}, left = {repr(self.left)}, right = {repr(self.right)})"

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
                    
        def _getLeaves(self):
            # trivial case
            if self == None:
                return
            ### WRITE YOUR CODE HERE ###
            # If no children -> print item
            if self.left == None and self.right == None:
                print(self.item, end=" ")
                return

            # If left child -> go left
            if self.left != None:
                self.left._getLeaves()

            # If right child -> go right
            if self.right != None:
                self.right._getLeaves()

    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            ### WRITE YOUR CODE HERE ###
            temp = AVLTree.AVLNode(pivot.item)
            temp.right = pivot.right
            temp.left = leftChild.right
            pivot = leftChild
            leftChild.right = temp
            
            # return bad child
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            ### WRITE YOUR CODE HERE ###
            temp = AVLTree.AVLNode(pivot.item)
            temp.left = pivot.left

            temp.right = rightChild.left

            pivot = rightChild

            rightChild.left = temp
            
            # return bad child
            return rightChild
        
        # Helper function that calculates and sets the balance of a node
        def __setBalance(node):
            # Helper function to find the height of a node
            def height(n):
                if n is None:
                    return 0
                else:
                    return max(height(n.left), height(n.right)) + 1

            # Calculates the height of each sub tree
            rightHeight = height(node.right)
            leftHeight = height(node.left)
            # Calculates and set the balance of the node
            node.setBalance(rightHeight - leftHeight)
        
        
        def __insert(root, item):
            # if empty tree, create a node with given item
            if root == None:
                return AVLTree.AVLNode(item)

            # item to be inserted is smaller than root
            # inserting into left subtree with specific rules to handle
            if item < root.item:
                root.left = __insert(root.left, item)
                
                # If the balance of the root is 0, 1, or -1 then that means we are in case 1 or 2
                if root.getBalance() in [0, 1, -1]:
                    __setBalance(root)
                    
                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == -2:
                    # bad child must be left child, since we are in the left subtree
                    badChild = root.left

                    # Subcase A - Single Rotation
                    # Rotate to the right
                    if badChild.getBalance() == -1:
                        root = rotateRight(root)
                        # update the balance
                        __setBalance(root)
                    
                    # Subcase B - Double Rotation
                    # Trisha helped with the logic behind subcase B
                    elif badChild.getBalance() == 1:

                        # Rotate the bad child and pivot
                        badChild = rotateLeft(badChild)
                        root.left = badChild
                        __setBalance(badChild.left)

                        # Double rotation
                        root = rotateRight(root)
                        __setBalance(root)

            # item to be inserted is larger than root
            # inserting into right subtree with specific rules to handle
            elif item > root.item:
                root.right = __insert(root.right, item)

                # If the balance of the root is 0, 1, or -1 then that means we are in case 1 or 2
                if root.getBalance() in [0, 1, -1]:
                    # Just update the balance
                    __setBalance(root)
                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == 2:
                    # bad child must be right child, since we are in the right subtree
                    badChild = root.right

                    # Subcase A - Single Rotation
                    if badChild.getBalance() == 1:
                        root = rotateLeft(root)
                        __setBalance(root)
                    # Subcase B - Double Rotation
                    elif badChild.getBalance() == -1:
                        # Rotate the bad child and the pivot
                        badChild = rotateRight(badChild)
                        root.right = badChild
                        __setBalance(badChild.right)
                        # Double rotation
                        root = rotateLeft(root)
                        __setBalance(root)   
                        
            # check if inserting duplicated value
            else:
                print(f"Insering duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
            return root
        
        # once done inserting update pivotFound value
        # and assign root with __insert return
        self.pivotFound = False
        self.root = __insert(self.root, item)

    # repr on tree calls repr on root node
    def __repr__(self):
        return f"AVLTree: {repr(self.root)}"

    # iter on tree calls iter on root node
    def __iter__(self):
        return iter(self.root)

    def __lookup(node, item):
        # returns True if value is in tree and False otherwise

        ### WRITE YOUR CODE HERE ###
        # trivial case
        if node == None:
            return False
        
        # If reached node with lookup item -> return True
        if node.item == item:
            return True
        
        # If item is larger than node -> go right
        if item > node.item:
            return AVLTree.__lookup(node.right, item)
        # returns True or False
        return AVLTree.__lookup(node.left, item)

    def __contains__(self, item):
        # checks if item is in the tree
        # runs __lookup on the tree root
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves
        self.root._getLeaves()  

def main():
    tree = AVLTree()

    # get values from input file
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()

    print(f"Values to be inserted: {values}")
    print()
    
    # insert values into the AVL tree
    for v in values:
        tree.insert(int(v))
        print(f"Value {v} is inserted.")
    print()

    # print out the tree
    print(repr(tree))
    print()
    
    # print out tree in-order traversal
    print("In-order traversal: ", end = "")
    for node in tree:
        print(node, end = " ")    
    print()

    # print out tree leaves
    print("\nLeaves: ", end = "")
    tree.leaves()
    print()
    
    # check if given values are in the tree
    print()
    for val in [10, 17, 35, 38, 40]:
        if (val in tree):
            print(f"Value {val} is in tree")
        else:
            print(f"Value {val} is not in tree")  

main()
