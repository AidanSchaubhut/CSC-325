class AVLTree:

    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance, left = None, right = None):
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
        
        # This does an in order traversal
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
        
        # find leaves
        def _getLeaves(self):
            # empty tree
            if self == None:
                return
            
            # If no children -> print item

            # If left child -> go left

            # If right child -> go right

    def __repr__(self):
        return f"AVLTree({repr(self.root)})"
    
    def __iter__(self):
        return iter(self.root)
    
    def insert(self, item):

        def rotateRight(pivot):
            # The pivot becomes the right child of the bad child
            leftChild = pivot.left
            return leftChild
        
        def rotateLeft(pivot):
            # The pivot becomes 
            rightChild = pivot.right
            return rightChild
        
        def __insert(root, item):
            if root == None:
                return AVLTree.AVLNode(item)
            
            if item < root.item:
                root.left = __insert(root.left, item)

                # CASE 1 & CASE 2
                # Update balance

                # CASE 3
                if root.getBalance() == -2:
                    badChild = root.left

                    # Subcase A - Single rotation
                    # must be a right rotation

                    # Subcase B - Double rotation
                    # rotate at bad child & rotate at pivot
                    # based on where bad grandchild is

                        # adjust the balances

                        # If inserted at bad grandchild -> pivot, bad child balances = 0

                        # If inserted item smaller than bad grandchild (left subtree)
                        # pivot balance = 1, bad child balance = 0

                        # If inserted item larger than bad grandchild (right subtree)
                        # Pivot balance = 0, bad child balance = -1

            elif item > root.item:
                root.right = __insert(root.right, item)

                # CASE 1 & CASE 2
                # update balance

                # CASE 3
                if root.getBalance() == 2:
                    badChild = root.right

                    # Subcase A - Single rotation
                    # must be a left rotation

                    # Subcase B - Double rotation
                    # rotate at bad child & rotate at pivot
                    # based on where bad grandchild is

                        # adjust the balances

                        # If inserted at bad grandchild -> pivot, bad child balances = 0

                        # If inserted item smaller than bad grandchild (left subtree)
                        # pivot balance = 0, bad child balance = 1

                        # If inserted item larger than bad grandchild (right subtree)
                        # Pivot balance = -1, bad child balance = 0


            # If the item is equal to the root meaning we have a duplicate value
            else:
                print(f"Inserting duplicate: {item}")
                raise Exception("Duplicate value")
            
            return root
        
        self.pivotFound = False
        self.root = __insert(self.root, item)


    
    def __lookup(node, item):
        if node == None:
            return False
        
        # If reached node with lookup item -> return True 

        # If item larger than node item -> go right

        # If item smaller than node item -> go left
        return AVLTree.__lookup(node.left, item)
    
    # if item is in tree
    def __contains__(self, item):
        return AVLTree.__loockup(self.root, item)
    
    # get the leaves of the tree
    def leaves(self):
        self.root._getLeaves()
    
def main():
    tree = AVLTree()
    print(repr(tree.root))

main()