Binary Tree Postorder Traversal
========
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

这道题让我们后序遍历，同样是让我们使用迭代。

解法一：我们还是先用递归说明一下后序遍历的顺序，`左->右->根`

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
    vector<int> postorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res,temp;
        if (root->left) temp = postorderTraversal(root->left);
        res.insert(res.end(), temp.begin(), temp.end());
        temp.clear();
        if (root->right) temp = postorderTraversal(root->right);
        res.insert(res.end(), temp.begin(), temp.end());

        res.push_back(root->val);
        return res;
    }
};
```

解法二：迭代解法，我们知道根节点是不能直接输出的，那么能输出的情况是什么，就是当这个节点是叶子节点的时候，或者它的左节点或者右节点已经输出过的情况，才可以输出当前这个节点，控制好这个条件，然后就能解决这个问题了。

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
    vector<int> postorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        stack<TreeNode*> temp;
        temp.push(root);
        TreeNode *pre = root;
        while (!temp.empty()) {
            TreeNode *flag = temp.top();
            if ((!flag->right && !flag->left) || pre == flag->right || pre == flag->left) {
                res.push_back(flag->val);
                temp.pop();
                pre = flag;
            } else {
                if (flag->right) temp.push(flag->right);
                if (flag->left) temp.push(flag->left);
            }
        }

        return res;
    }
};
```

相似题目[Binary Tree Preorder Traversal](../Medium/Binary Tree Preorder Traversal.md)
