class ASTNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (conditions)
        self.left = left       # Reference to left child node
        self.right = right     # Reference to right child node
        self.value = value     # Value for operand nodes, e.g., age > 30

    def __repr__(self):
        return f'ASTNode({self.type}, {self.left}, {self.right}, {self.value})'
