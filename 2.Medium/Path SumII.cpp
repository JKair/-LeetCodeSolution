class Solution {
public:
	vector<vector<int> > pathSum(TreeNode *root, int sum) {
		vector<vector<int>> result;
		vector<int> path;
		hasPathSum(root, sum, path, result);
		return result;
	}
	void hasPathSum(TreeNode *root, int sum,vector<int> path,vector<vector<int>> & result)
	{
		if (!root) return;
		if (!root->left && !root->right)
		{
			if (root->val == sum)
			{
				path.push_back(root->val);
				result.push_back(path);
			}
		}
		path.push_back(root->val);
		if (root->left)
		{
			hasPathSum(root->left, sum-root->val, path, result);
		}
		if (root->right)
		{
			hasPathSum(root->right, sum-root->val, path, result);
		}
	}
};