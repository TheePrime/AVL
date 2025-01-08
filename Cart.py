from AVL import AVLTree
class Cart:
    #initialize the Cart as the AVLTree
    def __init__(self):
        self.tree = AVLTree()

    #Function to add items to cart
    def add_item(self, key, price):
        self.tree.root = self.tree.insert(self.tree.root, key, price)
