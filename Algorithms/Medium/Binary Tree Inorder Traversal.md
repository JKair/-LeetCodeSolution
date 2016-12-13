Binary Tree Inorder Traversal
======================

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

这道题让我们对树进行中序遍历。

首先我们要明白中序遍历的特点，前中后序遍历，实际上是相对于根节点来说的，中序遍历则是将中间节点放在中间遍历，有左节点的时候先输出左节点

递归：
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
    void inorder(TreeNode* root, vector<int> &res) {
        if (!root) return ;
        if (root->left) inorder(root->left, res);
        res.push_back(root->val);
        if (root->right) inorder(root->right,res);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> temp;

        while (root || !temp.empty()) {
            while (root) {
                temp.push(root);
                root = root->left;
            }
            root = temp.top();
            temp.pop();
            res.push_back(root->val);
            root = root->right;
        }

        return res;
    }
};
```
