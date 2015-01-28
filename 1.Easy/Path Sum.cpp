class Solution {
public:
	bool hasPathSum(TreeNode *root, int sum) 
	{
		if (!root) return false;
		if (!root->left && !root->right) return (root->val == sum);
		if (root->left)
		{
			root->left->val += root->val;
			if (hasPathSum(root->left, sum))
			{
				return true;
			}
		}
		if (root->right)
		{
			root->right->val += root->val;
			if (hasPathSum(root->right, sum))
			{
				return true;
			}
		}
		return false;
	}
};