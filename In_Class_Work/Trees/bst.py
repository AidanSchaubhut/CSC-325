
class BinarySearchTree:
    class __Node:
        def __init__(self, val, left = None, right = None) -> None:
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val
        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left
        def setLeft(self, newLeft):
            self.left = newLeft

        def getRight(self):
            return self.right
        def setLeft(self, newRight):
            self.right = newRight
        
        # elem in tree
        # in-order traversal: left --> self --> right
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem
    
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        self.root = BinarySearchTree.__insert(self.root, val)
    
    def __insert(root, val):
        if root == None:
            return BinarySearchTree.__Node(val)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(), val))  
        
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(), val))

        return root