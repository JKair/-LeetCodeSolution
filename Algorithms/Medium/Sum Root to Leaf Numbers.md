Sum Root to Leaf Numbers
================
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

这道题让我们算从根节点到叶子节点路径权重的总和，注意，并不是直接加，父节点要*10。

解法一：我们可以用递归来解决这道题，因为每次，我们都需要知道父节点的权重是多少，所以我们需要额外的传一个结果过去。

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
    int sumNumbers(TreeNode* root, int res) {
        if (!root) return 0;
        res = res * 10 + root->val;
        if (!root->left && !root->right) return res;
        return sumNumbers(root->left, res) + sumNumbers(root->right, res);
    }
    int sumNumbers(TreeNode* root) {
        return sumNumbers(root, 0);
    }
};
```

解法二：迭代写法，我们需要使用队列去写这道题，由于我们本身并不关注遍历过的节点的值，只关注当前节点的值，所以我们可以将每次算得的值更新到当前节点，最后我们需要将叶子节点的值加起来。我们只要进行前序遍历，并把每次节点的值加上去后赋值给原来的节点，最后判断是不是叶子节点加起来就好了。

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
    int sumNumbers(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> temp;
        int res = 0, last = 0;
        temp.push(root);
        while (!temp.empty()) {
            TreeNode *t = temp.front();
            temp.pop();
            if (!t->left && !t->right) {
                res += t->val;
            }

            if (t->left) {
                t->left->val += t->val * 10;
                temp.push(t->left);
            }

            if (t->right) {
                t->right->val += t->val * 10;
                temp.push(t->right);
            }
        }

        return res;
    }
};
```
