Binary Tree Zigzag Level Order Traversal
==========
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

这道题还是让我们按照深度去生成数组，只不过不同的是，一行是从左往右，一行则要从右往左。

递归解法：这道题的递归解法其实和`Binary Tree Level Order Traversal`是差不多的，只是不同地方在于，我们要做深度判断，如果是单数的话，那么直接插入到末尾，如果是双数的话，那么要插入到第一个。

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
    void zigzagLevelOrder(TreeNode* root, int deep, vector<vector<int>> &res) {
        if (root) {
            if (deep < res.size()) {
                if (deep % 2 != 0) res[deep].push_back(root->val);
                else res[deep].insert(res[deep].begin(), root->val);
            } else {
                res.push_back({root->val});
            }
        } else {
            return;
        }

        if (root->left) zigzagLevelOrder(root->left, deep+1, res);
        if (root->right) zigzagLevelOrder(root->right, deep+1, res);

    }

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        zigzagLevelOrder(root, 1, res);

        return res;
    }
};
```


非递归解法：本质上还是一样的

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<TreeNode*> que;
        que.push(root);
        int deep = 1;
        while (!que.empty()) {
            vector<int> temp;
            int size = que.size();
            for (int i = 0; i < size; i++) {
                TreeNode *j = que.front();
                que.pop();
                if (deep % 2 != 0) temp.push_back(j->val);
                else temp.insert(temp.begin(), j->val);
                if (j->left) que.push(j->left);
                if (j->right) que.push(j->right);
            }
            deep++;
            res.push_back(temp);
        }
        return res;
    }
};
```

相似题目[Binary Tree Level Order Traversal](./Binary Tree Level Order Traversal.md)
