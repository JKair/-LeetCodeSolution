class Solution {
public:
	bool isSymmetric(TreeNode *root) {
		if (!root) return true;
		return isSame(root->left, root->right);
	}

	bool isSame(TreeNode *p, TreeNode *q)
	{
		if (!((q && p && q->val == p->val) || (p == NULL && q == NULL))) return false;
		if (p == NULL && q == NULL) return true;
		return isSame(p->right, q->left) && isSame(p->left, q->right);
	}
};