#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> path;
        dfs(candidates, 0, target, path, res);
        return res;
    }

private:
    void dfs(const vector<int>& candidates, int start, int remaining,
             vector<int>& path, vector<vector<int>>& res) {
        if (remaining == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < (int)candidates.size(); ++i) {
            int c = candidates[i];
            if (c > remaining) break;   
            path.push_back(c);
            dfs(candidates, i, remaining - c, path, res);
            path.pop_back();
        }
    }
};