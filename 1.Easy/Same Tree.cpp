class Solution {
public:
	bool isSameTree(TreeNode *p, TreeNode *q) {
		if (!((p && q && q->val == p->val) || (p == NULL &&  q == NULL))) return false;
		if (p == NULL &&  q == NULL) return true;
		return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
	}
};