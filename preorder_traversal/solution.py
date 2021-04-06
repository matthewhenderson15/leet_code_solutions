# For this problem there are two ways of approaching: iteratively and recursively.

# First create definition for the binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
# First step is recursive solution. We have the base case and the recursive case.
# Base case: tree could be empty, and if so return an empty array.
        if root is None:
            return []

# Recursive case, where we do root, left, and right.
        result = [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return result

# Step two is the iterative solution. In this case a stack is implemented and values are popped off in order
# of root, left, and right. Stack initialized with the root value.
        stack = [root]
        result = []

        if root is None:
            return []

# Condition is that stack is not empty. We continue to add values right and then left, so when they are popped
# off they maintain the proper order of root, left, and then right.
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        
        return result
        