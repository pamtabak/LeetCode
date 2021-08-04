#include <iostream>
#include <map>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int maxDepth(TreeNode* root) {
        std::map<TreeNode*, int> depths; // key is the node and value is its depth
        int largestDepth = 0;
        
        if (root == NULL) {
            return 0;
        }
        
        // BFS
        std::queue<TreeNode*> nodes;
        nodes.push(root);
        
        depths[root] = 1;
        largestDepth = 1;
        
        while (!nodes.empty()){
             TreeNode* currentNode = nodes.front();
             nodes.pop(); // removing the element
             if (currentNode->left != NULL) {
                nodes.push(currentNode->left);
                depths[currentNode->left] = depths[currentNode] + 1;
                if (depths[currentNode->left] > largestDepth){
                    largestDepth = depths[currentNode->left];
                }
            }
            if (currentNode->right != NULL) {
                nodes.push(currentNode->right);
                depths[currentNode->right] = depths[currentNode] + 1;
                if (depths[currentNode->right] > largestDepth){
                    largestDepth = depths[currentNode->right];
                }
            }
        }
        
        // for(map<int, int>::const_iterator it = depths.begin(); it != depths.end(); ++it) {
        //     std::cout << it->first << " " << it->second << "\n";
        // }
        
        return largestDepth;
    }
};

int main() {
    TreeNode node = TreeNode(0);
    Solution s;
    int maxDepth = s.maxDepth(&node);
    std::cout << maxDepth << "\n";
    return maxDepth;
}