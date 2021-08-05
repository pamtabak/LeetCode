class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int longestSubarray = 0;
        
        //first, lets implement it in n**2
        for (int i = 0; i < arr.size(); i++) {
            if ((longestSubarray > arr.size() - i) || (arr.size() - i < 3)){
                break;
            }
            
            // we assume the mountain starts at i
            int currentSubarray = 1; // arr[i]
            int lastIndex = 0;
            for (int j = i; j < arr.size() - 1; j++){
                if (arr[j] >= arr[j + 1]){
                    lastIndex = j;
                    break;
                }
                currentSubarray += 1;
            }
            if (currentSubarray == 1){
                continue;
            }
            
            bool isValid = false;
            for (int j = lastIndex + 1; j < arr.size(); j++){
                if (arr[j - 1] <= arr[j]){
                    break;
                }
                currentSubarray += 1;
                isValid = true;
            }
            
            if (!isValid) {
                continue;
            }
            
            if (currentSubarray > longestSubarray) {
                longestSubarray = currentSubarray;
            }
        }
        
        return longestSubarray;
    }
};