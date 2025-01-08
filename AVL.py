#AVL node for use in the AVL tree
class AVLNode:
    def __init__(self, key, price):
        self.key = key
        self.price = price
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None
    #Insert to the Tree while checking the balance factor
    def insert(self, root, key, price):
        if not root:
            return AVLNode(key, price)
        elif key < root.key:
            root.left = self.insert(root.left, key, price)
        else:
            root.right = self.insert(root.right, key, price)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
