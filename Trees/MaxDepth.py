class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"{str(self.val)} -> {str(self.left)} -> {str(self.right)}"
    
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

print(maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))) # 3
print(maxDepth(TreeNode(1, None, TreeNode(2)))) # 2
print(maxDepth(None)) # 0
print(maxDepth(TreeNode(0))) # 1
