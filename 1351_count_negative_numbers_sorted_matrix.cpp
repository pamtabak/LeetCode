#include<iostream>
#include<vector>

class Solution {
public:
    int quadraticSolution(std::vector<std::vector<int>>& grid){
        int negatives = 0;
        for (int m = 0; m < grid.size(); m++){
            for (int n = 0; n < grid[m].size(); n++){
                if (grid[m][n] < 0){
                    negatives ++;
                }
            }
        }
        
        return negatives;
    }
    
    int nPlusMSolution (std::vector<std::vector<int>>& grid){
        // we need to use the sort in our favour
        int negatives = 0;
        
        int row = grid.size() - 1; // this is the last row
        int column = 0;
        
        while (row >= 0 and column < grid[row].size()){
            if (grid[row][column] < 0){
                // this means the entire row from the current column to the end of it is negative
                negatives += grid[row].size() - column;
                row--; // we started from the last row and are going up
            } else{
                column += 1; // there might still be a negative number in this row
            }
        }
        
        return negatives;
    }
    
    int countNegatives(std::vector<std::vector<int>>& grid) {
        //return quadraticSolution (grid);
        return nPlusMSolution(grid);
    }
};

int main()
{
    Solution s;
    std::vector<std::vector<int>> grid = {{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}};
    std::cout << s.countNegatives(grid) << std::endl;
}