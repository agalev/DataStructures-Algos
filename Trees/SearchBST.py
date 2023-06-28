# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"{str(self.val)} -> {str(self.left)} -> {str(self.right)}"

def searchBST(root: TreeNode, val: int) -> TreeNode:
        
        if root == None or root.val == val:
            return root

        return searchBST(root.left, val) if root.val > val else searchBST(root.right, val)

# Test Cases
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 7))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 4))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 1))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 3))
print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 6))