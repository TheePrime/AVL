from AVL import AVLTree
class Cart:
    #initialize the Cart as the AVLTree
    def __init__(self):
        self.tree = AVLTree()

    def remove_item(self, key):
        self.tree.root = self.tree.delete(self.tree.root, key)

    #Function to add items to cart
    def add_item(self, key, price):
        self.tree.root = self.tree.insert(self.tree.root, key, price)
    #Functions to get total items and price in cart
    def total_items(self):
        return self.tree.get_total_items(self.tree.root)

    def total_price(self):
        return self.tree.get_total_price(self.tree.root)

    def search_item(self, key):
        node = self.tree.search(self.tree.root, key)
        if node:
            return (node.key, node.price)
        return None
