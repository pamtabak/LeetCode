/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> quadraticSolution(ListNode* head) {
        std::vector<int> result;
        
        while (head != NULL) {
            int currentVal = head->val;
            int nextLargestNode = 0;
            ListNode* restOfList = head->next;
            while (restOfList != NULL){ 
                if (restOfList-> val > currentVal){
                    nextLargestNode = restOfList->val;
                    break;
                }
                restOfList = restOfList->next;
            }
            result.push_back(nextLargestNode);
            
            head = head->next;
        }
        
        return result;
    }
    
    vector<int> nextLargerNodes(ListNode* head) {
        return quadraticSolution(head);
    }
};