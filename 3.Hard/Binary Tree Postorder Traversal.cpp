.class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> res;
        stack<TreeNode*> node_stack;
        if(root==NULL)
            return res;
        node_stack.push(root);
        TreeNode* cur=root;
        TreeNode* pre=NULL;
        while(!node_stack.empty()){
            cur=node_stack.top();
            if((cur->left==NULL&&cur->right==NULL)||((pre!=NULL)&&(pre==cur->left||pre==cur->right))) {
                res.push_back(cur->val);
                node_stack.pop();
                pre=cur; 
            }else{
                if(cur->right!=NULL)
                    node_stack.push(cur->right);
                if(cur->left!=NULL)
                    node_stack.push(cur->left);
            }
        }
        return res;
    }
};