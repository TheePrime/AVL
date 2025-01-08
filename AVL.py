class AVLNode:
    def __init__(self, key, price):
        self.key = key
        self.price = price
        self.height = 1
        self.left = None
        self.right = None