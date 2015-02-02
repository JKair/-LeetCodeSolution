class Solution {
public:
	vector<vector<int>> result;
	vector<vector<int>> zigzagLevelOrder(TreeNode *root)
	{
		insertData(root, 0);
		for (int i = 1; i < result.size(); i += 2)
		{
			vector<int>* v = &result[i];
			std:reverse(v->begin(), v->end());
		}
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