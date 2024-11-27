class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return "DONE"
        else:
            return self._add_recursive(self.root, value)
    
    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return "DONE"
            else:
                return self._add_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
                return "DONE"
            else:
                return self._add_recursive(node.right, value)
        else:
            return "ALREADY"
    
    def search(self, value):
        return "YES" if self._search_recursive(self.root, value) else "NO"
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def print_tree(self):
        self._print_recursive(self.root, 0)
    
    def _print_recursive(self, node, depth):
        if node is None:
            return
        self._print_recursive(node.left, depth + 1)
        print("." * depth + str(node.value))
        self._print_recursive(node.right, depth + 1)


bst = BinarySearchTree()
while True:
    try:
        query = input().strip()
    except EOFError:
        break
    
    if query.startswith("ADD"):
        _, value = query.split()
        value = int(value)
        print(bst.add(value))
    elif query.startswith("SEARCH"):
        _, value = query.split()
        value = int(value)
        print(bst.search(value))
    elif query == "PRINTTREE":
        bst.print_tree()

