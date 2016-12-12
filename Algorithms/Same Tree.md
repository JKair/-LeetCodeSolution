Same Tree
=========
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

这道题让我们判断是否两个树相同

解法：这道题可以用递归和非递归解法，递归解法思路比较简洁，非递归解法用栈解决，由于题目比较简单就不赘述了。

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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!((p && q && p->val == q->val) || !p && !q)) return false;
        if (!p && !q) return true;

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack<TreeNode*> ps,qs;
        if (p) ps.push(p);
        if (q) qs.push(q);
        while (!ps.empty() && !qs.empty()) {
            p = ps.top();q = qs.top();
            if (p->val != q->val) return false;
            ps.pop();qs.pop();
            if (p->left) ps.push(p->left);
            if (q->left) qs.push(q->left);
            if (ps.size() != qs.size()) return false;
            if (p->right) ps.push(p->right);
            if (q->right) qs.push(q->right);
            if (ps.size() != qs.size()) return false;
        }

        return ps.size() == qs.size();
    }
};
```

相似题目[Symmetric Tree](./Symmetric Tree.md)
