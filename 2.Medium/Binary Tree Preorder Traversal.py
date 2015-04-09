# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if not root:
            return []
        res,temp = [],[]
        temp.append(root)
        while temp:
            flag = temp.pop()
            res.append(flag.val)
            if flag.right:
                temp.append(flag.right)
            if flag.left:
                temp.append(flag.left)
        return res