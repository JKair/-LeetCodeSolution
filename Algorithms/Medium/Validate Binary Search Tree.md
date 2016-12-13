Validate Binary Search Tree
==================
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

这道题让我们验证是不是搜索

解法：验证树最方便的就是使用递归了，但是我们验证之前需要知道搜索树的特性，就是根节点必须大于他所有左子树的值且小于他所有右子树的值。所以我们在递归的时候，多传入一个值来代表当前根节点的值，从而判断是否是搜索树。由于树的值可能是`INT_MAX`，我们用`LONG_MAX`来解决这个问题。

```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root, long maxNum, long minNum) {
        if (!root) return true;
        if (root->val <= minNum || root->val >= maxNum) return false;
        return isValidBST(root->left, root->val, minNum) && isValidBST(root->right, maxNum, root->val);
    }
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, LONG_MAX, LONG_MIN);
    }
};
```
