Populating Next Right Pointers in Each Node
=============
Given a binary tree
```
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL


这道题就是让我们把一棵完全二叉树的左右节点连接起来。

解法：这道题其实就是层级遍历。我们用递归，把问题简化到只有一个小三角形的时候，这时候我们只要将左右节点连接起来就可以了，再将问题向更大的三角形，如例子里面的例子，我们将4->5连接之后怎么让5->6连接呢，我们实际上可以发现，我们已经处理完`1,2,3`这个小三角形了，所以我们只要用2->next就能直接到达3，然后连接5->6，到边界的时候，只要判断3有没有next节点，直接赋值为NULL就可以了。

```
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (!root) return ;
        if (root->left) root->left->next = root->right;
        if (root->right) root->right->next = root->next ? root->next->left : NULL;
        connect(root->left);
        connect(root->right);
    }
};
```
