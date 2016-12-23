Binary Search Tree Iterator
============
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

这道题让我们一个BST的迭代器，要实现三个功能。

解法：我们可以利用栈，由于BST的中序遍历可以按照从小到大输出，我们将树的左节点都放进栈里面，就可以按照顺序输出了。

```
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
private:
    stack<TreeNode*> res;
public:
    BSTIterator(TreeNode *root) {
        while (root) {
            res.push(root);
            root = root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !res.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *temp = res.top();
        res.pop();
        int last = temp->val;
        if (temp->right) {
            temp = temp->right;
            while (temp) {
                res.push(temp);
                temp = temp->left;
            }
        }
        return last;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
```
