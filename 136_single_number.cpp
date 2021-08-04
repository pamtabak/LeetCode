class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::map<int, int> numsCount;
        for (const int n : nums) {
            if (numsCount.find(n) == numsCount.end()){
                numsCount[n] = 0;
            }
            numsCount[n] += 1;
        }
        for (auto const& n : numsCount){
            if (n.second == 1) {
                return n.first;
            }
        }
        return -1;
    }
};