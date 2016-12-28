Binary Tree Right Side View
=======
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
```
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
You should return [1, 3, 4].

这道题让我们输出一棵树的最右边的节点。

解法：因为我们要让这棵树输出最右边的节点，所以，我们要做到一层一层遍历，并且放在最后的肯定是最右边的节点。利用队列就可以做到，我们每次都按照先放进左节点再放进右节点的情况，这样永远都能输出最右边的节点了。

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
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};
        vector<int> res;
        queue<TreeNode*> temp;
        temp.push(root);
        while (!temp.empty()) {
            int size = temp.size();
            for (int i = 0; i < size; i++) {
                TreeNode *flag = temp.front();
                if (i == size - 1) {
                    res.push_back(flag->val);
                }
                if (flag->left) temp.push(flag->left);
                if (flag->right) temp.push(flag->right);
                temp.pop();
            }
        }

        return res;
    }
};
```
