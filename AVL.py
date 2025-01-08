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
    
    #Get Height
    #Get the height of the three from the root Node
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    #Gets the balance factor(Height of left subtree - Height of right subtree)
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    #Tree Rotations
    #Left Rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    #Right Rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y