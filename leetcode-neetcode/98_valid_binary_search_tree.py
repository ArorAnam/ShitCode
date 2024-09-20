
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def helper(node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
    
    return helper(root)

# Test cases
# Test case 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert isValidBST(root) == True

# comprehensive test case:
# Test case 2
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
assert isValidBST(root) == False

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(n), where n is the number of nodes in the tree

# Alternate solution, using inorder traversal
def isValidBST(root: TreeNode) -> bool:
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return