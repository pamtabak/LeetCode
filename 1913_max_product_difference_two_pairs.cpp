#include <iostream>
#include <vector>

class Solution {
public:
    int maxProductDifference(std::vector<int>& nums) {
        // what if we get the 2 smallest nums and the 2 largest ones?
        sort(nums.begin(), nums.end()); // this implies a n log n complexity
        // there is probably a way of doing this faster, trading memory for time (in n time complexity.)
        
        return (nums[nums.size() - 1] * nums[nums.size() - 2]) - (nums[0] * nums[1]);
    }
};