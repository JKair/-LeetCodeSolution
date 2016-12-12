Binary Tree Level Order Traversal II
====================
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

这道题让我们按照树的深度来生成一个数组，但是有一个特别的处理，就是必须先插入叶子节点再一层一层往上。

解法：其实这道题和之前的那两道题目是差不多的，我们只要在之前的基础上，稍微改动一下就可以了。

递归：由于我们要插入正确的位置，所以我们需要知道当前这棵树的深度是多少，只要知道了深度，那么我们就很好解决插入于哪个地方的问题。

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

    void levelOrderBottom(TreeNode* root, int deep, vector<vector<int>> &res) {
        if (root && root->left) levelOrderBottom(root->left, deep - 1, res);
        if (root && root->right) levelOrderBottom(root->right, deep - 1, res);

        if (root) {
            res[deep].push_back(root->val);
        } else {
            return;
        }
    }

    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        int maxDeep = maxDepth(root);
        vector<vector<int>> res(maxDeep, vector<int>(0));
        levelOrderBottom(root, maxDeep - 1, res);

        return res;
    }
};
```


迭代：
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<TreeNode*> que;
        que.push(root);
        while (!que.empty()) {
            vector<int> temp;
            int size = que.size();
            for (int i = 0; i < size; i++) {
                TreeNode *j = que.front();
                que.pop();
                temp.push_back(j->val);
                if (j->left) que.push(j->left);
                if (j->right) que.push(j->right);
            }
            res.insert(res.begin(), temp);
        }
        return res;
    }
};
```


相似题目：[Binary Tree Level Order Traversal](./Binary Tree Level Order Traversal.md)、[Binary Tree Zigzag Level Order Traversal](Binary Tree Zigzag Level Order Traversal.md)
