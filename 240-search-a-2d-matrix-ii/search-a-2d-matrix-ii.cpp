#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }

        for (int i = 0; i < (int)matrix.size(); i++) {
            for (int j = 0; j < (int)matrix[i].size(); j++) {
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }

        return false;
    }
};
