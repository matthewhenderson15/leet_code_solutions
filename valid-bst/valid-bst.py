# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # A valid binary search tree is a binary tree where the left node value
    # is less than the root node value, and the right node value is greater
    # than the root node value.
    
    # Main function which calls helper function. Passes in current node, min
    # node value, and max node value.
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isBST(root, -(2**31)-1, (2**31))
    
    # Recursive helper function to compare each node in tree to see if it is
    # a valid BST
    def isBST(self, root, minValue, maxValue):    
        # Edge case to check if no root node exists
        if root == None:
            return True
        
        # Edge case to check if value of root node is less than the min value
        # or greater than the max value
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        # Check each node in the tree; if checking left node, min value remains
        # unchanged and new maximum value is the root node value; if checking
        # right node, the new min is the root node value and the maximum value 
        # is the maximum value provided for the problem; in each check, it will 
        # return true if the node value is in the acceptable range and false if not
        return self.isBST(root.left, minValue, root.val) and
        self.isBST(root.right, root.val, maxValue)

# Since each node is compared one at a time to the root node, the time 
# complexity is O(n)
