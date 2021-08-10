/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        std::queue<TreeNode*> nodes;
        nodes.push(root);
        
        while (!nodes.empty()){
             TreeNode* currentNode = nodes.front();
             nodes.pop(); // removing the element
            
            if (currentNode->val == val){
                return currentNode;
            }
            
            if (currentNode->val > val && currentNode->left != NULL){
                nodes.push(currentNode->left);
            }
            else if (currentNode->val < val && currentNode->right != NULL) {
                nodes.push(currentNode->right);
            }
        }
        
        return NULL;
    }
};