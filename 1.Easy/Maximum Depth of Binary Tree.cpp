class Solution {
public:
	int depth = 0;
	int maxDepth(TreeNode *root) 
	{
		if (!root) return 0;
		traverse(root, 0);
		return depth+1;
	}

	void traverse(TreeNode *root, int depthNow)
	{
		if (!root) return;
		else
		{
			traverse(root->left, depthNow + 1);
			traverse(root->right, depthNow + 1);
		}
		if (depth < depthNow) depth = depthNow;
	}
};