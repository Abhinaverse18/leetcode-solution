class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> cur;
        backtrack(1, k, n, cur, res);
        return res;
    }

private:
    void backtrack(int start, int k, int remain, vector<int>& cur, vector<vector<int>>& res) {
        if (cur.size() == k) {
            if (remain == 0) res.push_back(cur);
            return;
        }
        for (int i = start; i <= 9; i++) {
            if (i > remain) break;              
            cur.push_back(i);
            backtrack(i + 1, k, remain - i, cur, res);
            cur.pop_back();
        }
    }
};