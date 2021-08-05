class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascal;
        vector<int> firstRow = { 1 };
        pascal.push_back(firstRow);
        
        for (int row = 1; row < numRows; row++) {
            vector<int> lastRow = pascal[row - 1];
            vector<int> currentRow;
            currentRow.push_back(1); // first element is always 1
            for (int element = 0; element < lastRow.size() - 1; element++){
                currentRow.push_back(lastRow[element] + lastRow[element + 1]);
            }
            currentRow.push_back(1); // last element is always 1
            pascal.push_back(currentRow);
        }
        
        return pascal;
    }
};