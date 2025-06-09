class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinaryTree(root):
    # Base case: if root is None, return None
    if not root:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right subtrees
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    
    return root

# Print the inverted tree
def printTree(root):
    if not root:
        return
    
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)

def reverseTreeExample():
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)
    print("Original tree:")
    printTree(tree)
    print("\nInverted tree:")
    inverted_tree = invertBinaryTree(tree)
    printTree(inverted_tree)

def zigzagLevelOrder(root):
    """
    Performs zigzag level order traversal of a binary tree.
    Returns a list of lists where each inner list represents a level,
    traversed alternately from left-to-right and right-to-left.
    """
    if not root:
        return []
    
    result = []
    queue = [root]
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add current level to result based on direction
        if not left_to_right:
            current_level.reverse()
        result.append(current_level)
        
        # Toggle direction for next level
        left_to_right = not left_to_right
    
    return result

def zigzagExample():
    # Create a sample tree
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    
    print("Zigzag traversal:")
    levels = zigzagLevelOrder(tree)
    for level in levels:
        print(level)


class Codec:
    def serialize(self, root):
        """
        Serializes a binary tree to a string representation.
        Uses level-order traversal with 'null' for empty nodes.
        """
        if not root:
            return "[]"
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        # Remove trailing nulls
        while result and result[-1] == "null":
            result.pop()
            
        return "[" + ",".join(result) + "]"

    def deserialize(self, data):
        """
        Deserializes a string representation back to a binary tree.
        """
        if data == "[]":
            return None
            
        # Parse the string into values
        values = data[1:-1].split(",")
        if not values:
            return None
            
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Left child
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
                
        return root

def serializeExample():
    # Create a sample tree
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.right = TreeNode(5)
    
    codec = Codec()
    print("Original tree serialized:")
    serialized = codec.serialize(tree)
    print(serialized)
    
    print("\nDeserialized back to tree and serialized again:")
    deserialized = codec.deserialize(serialized)
    print(codec.serialize(deserialized))


    

if __name__ == "__main__":
    # reverseTreeExample()
    # zigzagExample()
    serializeExample()