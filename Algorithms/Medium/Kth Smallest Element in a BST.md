Kth Smallest Element in a BST
=======
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

这个让我们找一下搜索树的第k大的数字。

解法：搜索树只要进行中序遍历就可以按照顺序大小输出了。

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
    int dfs(TreeNode* root, int &k) {
        if (!root) return -1;
        int val = dfs(root->left, k);
        if (k == 0) return val;
        k--;
        if (k == 0) return root->val;
        return dfs(root->right, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        return dfs(root, k);
    }
};
```
