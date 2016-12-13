Path Sum II
===========
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

这道题让我们给出总和为sum的树的路径。

解法：这道题我们可以深度优先遍历去解决这个问题，当我们遍历到叶子节点的时候，如果sum相等，那么就将当前记录的路径放进结果集。

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
    void pathSum(TreeNode* root, vector<vector<int>> &res, vector<int> &temp,int sum) {
        if (root && !root->left && !root->right) {
              if (sum == 0) res.push_back(temp);

              return;
        }

        if (root->left) {
            temp.push_back(root->left->val);
            pathSum(root->left, res, temp, sum - root->left->val);
            temp.pop_back();
        }
        if (root->right) {
            temp.push_back(root->right->val);
            pathSum(root->right, res, temp, sum - root->right->val);
            temp.pop_back();
        }
    }

    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        if (!root) return {};

        vector<vector<int>> res;
        vector<int> temp;
        temp.push_back(root->val);
        pathSum(root, res, temp, sum - root->val);

        return res;
    }
};
```
