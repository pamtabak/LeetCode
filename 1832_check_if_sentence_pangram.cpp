#include <iostream>
#include <unordered_set>

class Solution {
public:
    const std::string alfabet{"abcdefghijklmnopqrstuvwxyz"};
    
    bool checkIfPangram(std::string sentence) {
        std::unordered_set<char> seenLetters;
        for(char& c : sentence) {
            if (seenLetters.find (c) == seenLetters.end()) {
                seenLetters.insert(c);
            }
        }
        
        return seenLetters.size() == alfabet.size();
    }
};

int main() {
    Solution s;
    bool isPangram = s.checkIfPangram("teste");
    std::cout << isPangram << "\n";
    return 0;
}