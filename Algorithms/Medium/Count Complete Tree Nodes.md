Count Complete Tree Nodes
=======
Given a complete binary tree, count the number of nodes.

这道题让我们数一下，[完全二叉树](http://baike.baidu.com/link?url=bXp6Zs6HThTK5ChVAgACd4klnlMIt9nFfbQs_XaWxQLcrcPQjwqD_GXnMKRaLmrLgdOSPrch5kDMi2q_aHp_ANkFt8TsREdiK24LwR3BHWpLrekAT9Xqa97BlOxPa9h84hvc_cWgUvA1LYmov9xqX_)有多少个节点。

解法：如果我们按照普通的递归，有左右节点就+1的方式，是完全没办法解决问题的，因为最后会超时！那么我们应该找可以快速计算的通项公式，完全二叉树有个性质，就是左右节点是一定满的，那么当二叉树的左右节点高度平衡的时候，可以二叉树的节点的个数就等于`2的n次方-1`。利用这个性质，我们可以快速得到完全二叉树的节点数。

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
    int countNodes(TreeNode* root) {
        if (!root) return NULL;

        int hl = 0, hr = 0;
        TreeNode *pLeft = root, *pRight = root;
        while (pLeft) {
            pLeft = pLeft->left;
            hl++;
        }
        while (pRight) {
            pRight = pRight->right;
            hr++;
        }
        if (hl == hr) return pow(2, hl) - 1;
        return  countNodes(root->left) + countNodes(root->right) + 1;
    }
};
```
