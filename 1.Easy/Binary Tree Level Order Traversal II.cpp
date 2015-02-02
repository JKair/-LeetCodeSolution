class Solution {
public:
	vector<vector<int>> result;
	vector<vector<int> > levelOrderBottom(TreeNode *root)
	{
		insertData(root, 0);
		std:reverse(result.begin(), result.end());
		return result;
	}

	void insertData(TreeNode *root, int depth)
	{
		if (!root)
		{
			return;
		}
		if (result.size() == depth)
		{
			result.push_back(vector<int>());
		}
		result[depth].push_back(root->val);
		insertData(root->left, depth + 1);
		insertData(root->right, depth + 1);
	}
};