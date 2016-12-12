Binary Tree Level Order Traversal
===========
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

这道题让我们按照树的深度去生成一个二维数组。

解法一：递归解法的话比较简单，我们创建好容器，然后再加一个深度标识，判断当前深度是否超过了结果容器，如果操过了，就再插入多一个，如果没超过，就放到对应容器就可以了。

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
    void levelOrder(TreeNode* root, int deep, vector<vector<int>> &res) {
        if (root) {
            if (deep < res.size()) {
                res[deep].push_back(root->val);
            } else {
                res.push_back({root->val});
            }
        } else {
            return;
        }

        if (root->left) levelOrder(root->left, deep+1, res);
        if (root->right) levelOrder(root->right, deep+1, res);

    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        levelOrder(root, 0, res);

        return res;
    }
};
```

解法二：非递归解法，利用队列先进先出的特性，就能够实现一层一层遍历了。

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
    vector<vector<int>> levelOrder(TreeNode* root) {
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
            res.push_back(temp);
        }
        return res;
    }
};
```

[Binary Tree Zigzag Level Order Traversal](./Binary Tree Zigzag Level Order Traversal.md)
