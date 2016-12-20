Binary Tree Preorder Traversal
=======
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

这道题是让我们做先序遍历，然后要我们使用迭代，别用递归。

解法一：虽然题目不让我们用递归，但是我们还是要写一下的，表示自己理解先序遍历，先序遍历的遍历顺序为`根->左->右`

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
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res,temp;
        res.push_back(root->val);
        if (root->left) temp = preorderTraversal(root->left);
        res.insert(res.end(), temp.begin(), temp.end());
        temp.clear();
        if (root->right) temp = preorderTraversal(root->right);
        res.insert(res.end(), temp.begin(), temp.end());

        return res;
    }
};
```

解法二：迭代解法，我们利用栈来解决这个问题。

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
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        stack<TreeNode*> temp;
        temp.push(root);
        while (!temp.empty()) {
            TreeNode *flag = temp.top();
            temp.pop();
            res.push_back(flag->val);
            if (flag->right) temp.push(flag->right);
            if (flag->left) temp.push(flag->left);
        }

        return res;
    }
};
```

相似题目[Binary Tree Postorder Traversal](../Hard/Binary Tree Postorder Traversal.md)
