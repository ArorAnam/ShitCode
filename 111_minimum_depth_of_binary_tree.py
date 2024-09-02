class Depth_of_Binary_Tree:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return

        min_depth = float('int')
        stack = [(root, False, 1)]

        while len(stack) != 0:
            node, visited, depth = stack.pop()

            if node is not None and visited  == True:
                if node.left is None and node.right is None:
                    if depth < min_depth:
                        min_depth = depth
            else:
                stack.append((node, True, depth))

                if node.right is not None:
                    stack.append((node.right, False, depth + 1))

                if node.left is not None:
                    stack.append((node.left, False, depth + 1))

        return min_depth

        # Time: O(n)
        # Space: O(n)