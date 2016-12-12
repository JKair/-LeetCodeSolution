Symmetric Tree
===============
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

这道题让我们判断是不是镜像树。

解法：镜像树的特点就是以根节点为对称。

递归解法：
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
    bool isSymmetric(TreeNode* left, TreeNode* right) {
        if (!((left && right && left->val == right->val) || (!left) && (!right))) return false;
        if (!left && !right) return true;

        return isSymmetric(left->left, right->right) && isSymmetric(left->right, right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;

        return isSymmetric(root->left, root->right);
    }
};
```

非递归解法：
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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        stack<TreeNode*> left,right;
        left.push(root);right.push(root);

        while (!left.empty() && !right.empty()) {
            TreeNode *l = left.top();
            TreeNode *r = right.top();
            if (l->val != r->val) return false;
            left.pop();right.pop();

            if (l->left) left.push(l->left);
            if (r->right) right.push(r->right);
            if (left.size() != right.size()) return false;

            if (l->right) left.push(l->right);
            if (r->left) right.push(r->left);
            if (left.size() != right.size()) return false;
        }

        return left.size() == right.size();
    }
};
```
