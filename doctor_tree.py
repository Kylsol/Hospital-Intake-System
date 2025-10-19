class DoctorNode:
    def __init__(self, name):
        self.name   = name
        self.left   = None
        self.right  = None

class DoctorTree:
    def __init__(self):
        self.root = None
    
    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result
    
    def inorder(self, node):
        if node is None:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result
    
    def postorder(self, node):
        if node is None:
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result
    
    def _find(self, node, target):
        if node is None:
            return None
        if node.name == target:
            return node
        left_hit = self._find(node.left, target)
        if left_hit:
            return left_hit
        return self._find(node.right, target)
    
    def insert(self, parent_name, child_name, side):
        parent = self._find(self.root, parent_name)
        if parent is None:
            raise ValueError(f'Parent "{parent_name}" not found in the tree.')

        side = side.lower()
        if side not in ("left", "right"):
            raise ValueError('Side must be "left" or "right".')

        new_node = DoctorNode(child_name)
        if side == "left":
            if parent.left is not None:
                raise ValueError(f'Parent "{parent_name}" already has a left child.')
            parent.left = new_node
        else:
            if parent.right is not None:
                raise ValueError(f'Parent "{parent_name}" already has a right child.')
            parent.right = new_node
            

if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
    print("")
    print("")
    print("Edge-case testing")
    print("")
    try:
        tree.insert("Dr. NotHere", "Dr. X", "left")
    except ValueError as e:
        print("Edge (missing parent):", e)

    try:    
        tree.insert("Dr. Croft", "Dr. Y", "middle")
    except ValueError as e:
        print("Edge (invalid side):", e)

    try:
        tree.insert("Dr. Croft", "Dr. Z", "left")
    except ValueError as e:
        print("Edge (occupied side):", e)



