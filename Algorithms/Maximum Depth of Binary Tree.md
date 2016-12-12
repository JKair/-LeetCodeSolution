Maximum Depth of Binary Tree
===========
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

这道题让我们计算出一棵树的深度是多少。

解法：我们可以使用递归，分别计算左子树和右子树的深度，然后再加1就好了。

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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```
