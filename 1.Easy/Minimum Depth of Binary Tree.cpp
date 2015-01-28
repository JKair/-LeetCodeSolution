class Solution {
public:
	int minDepth(TreeNode *root) 
	{
		if (!root) return 0;
		if (!root->left && !root->right) return 1;
		int LMin = INT_MAX;
		if (root->left) LMin = minDepth(root->left) + 1;
		int RMin = INT_MAX;
		if (root->right) RMin = minDepth(root->right) + 1;
		return LMin < RMin ? LMin : RMin;
	}
};