Balanced Binary Tree
==============
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

判断是不是平衡树。

解法：比较简单，用递归解决就好了，要解这道题，必须先弄清楚什么是平衡树。

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
    int depth(TreeNode* root) {
        if (root == NULL) return 0;

        return 1 + max(depth(root->left), depth(root->right));
    }
    bool isBalanced(TreeNode* root) {
        if (root == NULL) {
            return true;
        }
        return abs(depth(root->left) - depth(root->right)) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }
};
```
