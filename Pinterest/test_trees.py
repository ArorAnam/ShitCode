import unittest
from trees import TreeNode, invertBinaryTree, zigzagLevelOrder
from trees import Codec

class TestTreeFunctions(unittest.TestCase):
    def setUp(self):
        # Create common test trees that can be used across multiple tests
        self.empty_tree = None
        
        # Single node tree
        self.single_node = TreeNode(1)
        
        # Regular balanced tree
        self.balanced_tree = TreeNode(4)
        self.balanced_tree.left = TreeNode(2)
        self.balanced_tree.right = TreeNode(7)
        self.balanced_tree.left.left = TreeNode(1)
        self.balanced_tree.left.right = TreeNode(3)
        self.balanced_tree.right.left = TreeNode(6)
        self.balanced_tree.right.right = TreeNode(9)

    def test_invert_binary_tree(self):
        # Test empty tree
        self.assertIsNone(invertBinaryTree(self.empty_tree))
        
        # Test single node tree
        inverted_single = invertBinaryTree(self.single_node)
        self.assertEqual(inverted_single.val, 1)
        self.assertIsNone(inverted_single.left)
        self.assertIsNone(inverted_single.right)
        
        # Test balanced tree
        inverted = invertBinaryTree(self.balanced_tree)
        # Check root
        self.assertEqual(inverted.val, 4)
        # Check first level
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)
        # Check second level
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)

    def test_zigzag_level_order(self):
        # Test empty tree
        self.assertEqual(zigzagLevelOrder(self.empty_tree), [])
        
        # Test single node tree
        self.assertEqual(zigzagLevelOrder(self.single_node), [[1]])
        
        # Test balanced tree
        result = zigzagLevelOrder(self.balanced_tree)
        expected = [
            [4],           # Level 0: left to right
            [7, 2],       # Level 1: right to left
            [1, 3, 6, 9]  # Level 2: left to right
        ]
        self.assertEqual(result, expected)
        
        # Test unbalanced tree
        unbalanced_tree = TreeNode(1)
        unbalanced_tree.left = TreeNode(2)
        unbalanced_tree.right = TreeNode(3)
        unbalanced_tree.left.left = TreeNode(4)
        result = zigzagLevelOrder(unbalanced_tree)
        expected = [
            [1],          # Level 0: left to right
            [3, 2],       # Level 1: right to left
            [4]           # Level 2: left to right
        ]
        self.assertEqual(result, expected)

    def test_serialize_deserialize(self):
        codec = Codec()
        
        # Test empty tree
        self.assertEqual(codec.serialize(self.empty_tree), "[]")
        self.assertIsNone(codec.deserialize("[]"))
        
        # Test single node tree
        self.assertEqual(codec.serialize(self.single_node), "[1]")
        deserialized_single = codec.deserialize("[1]")
        self.assertEqual(deserialized_single.val, 1)
        self.assertIsNone(deserialized_single.left)
        self.assertIsNone(deserialized_single.right)
        
        # Test balanced tree
        serialized_balanced = codec.serialize(self.balanced_tree)
        deserialized_balanced = codec.deserialize(serialized_balanced)
        
        # Verify the structure matches original tree
        self.assertEqual(deserialized_balanced.val, 4)
        self.assertEqual(deserialized_balanced.left.val, 2)
        self.assertEqual(deserialized_balanced.right.val, 7)
        self.assertEqual(deserialized_balanced.left.left.val, 1)
        self.assertEqual(deserialized_balanced.left.right.val, 3)
        self.assertEqual(deserialized_balanced.right.left.val, 6)
        self.assertEqual(deserialized_balanced.right.right.val, 9)
        
        # Test unbalanced tree
        unbalanced_tree = TreeNode(1)
        unbalanced_tree.left = TreeNode(2)
        unbalanced_tree.right = TreeNode(3)
        unbalanced_tree.left.left = TreeNode(4)
        
        serialized_unbalanced = codec.serialize(unbalanced_tree)
        deserialized_unbalanced = codec.deserialize(serialized_unbalanced)
        
        self.assertEqual(deserialized_unbalanced.val, 1)
        self.assertEqual(deserialized_unbalanced.left.val, 2)
        self.assertEqual(deserialized_unbalanced.right.val, 3)
        self.assertEqual(deserialized_unbalanced.left.left.val, 4)
        self.assertIsNone(deserialized_unbalanced.left.right)
        self.assertIsNone(deserialized_unbalanced.right.left)
        self.assertIsNone(deserialized_unbalanced.right.right)

if __name__ == '__main__':
    unittest.main() 