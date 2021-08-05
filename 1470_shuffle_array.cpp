#include<iostream>
#include<vector>

class Solution {
public:
    std::vector<int> shuffle(std::vector<int>& nums, int n) {
        std::vector<int> x(nums.begin(), nums.begin() + n);
        std::vector<int> y(nums.begin() + n, nums.end());
        
        std::vector<int> newVector;
        for (int i = 0; i < n; i++){
            newVector.push_back(x[i]);
            newVector.push_back(y[i]);
        }
        
        return newVector;
    }
};