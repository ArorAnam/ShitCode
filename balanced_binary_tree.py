from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> bool:
        self.val = val
        self.left = left
        self.right = right

class Soultion:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # helper function to calculate the height of the binary tree rooted at 'node'
        def calculate_height(node):
            # base case: if the node is None, the height is 0.
            if node is None:
                return 0
            
            # Recursively find the height of the left and right subtrees.
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            # If either subtree is unbalanced (indicated by a height of -1).
            # or the difference in heights is greater than 1, then the tree is unbalanced
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # If the tree is balanced, return the height of the tree
            return 1 + max(left_height, right_height)
        
        # The tree is balanced if calculate_height does not return -1.
        return calculate_height(root) >= 0
