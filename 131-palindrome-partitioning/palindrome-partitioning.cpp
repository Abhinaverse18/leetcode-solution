class Solution {
public:
    vector<vector<string>> partition(string s) {
        int n = s.size();
        // isPal[i][j] = true if s[i..j] is a palindrome
        vector<vector<bool>> isPal(n, vector<bool>(n, false));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j] && (j - i < 2 || isPal[i + 1][j - 1])) {
                    isPal[i][j] = true;
                }
            }
        }

        vector<vector<string>> res;
        vector<string> path;

        function<void(int)> dfs = [&](int start) {
            if (start == n) {
                res.push_back(path);
                return;
            }
            for (int end = start; end < n; ++end) {
                if (isPal[start][end]) {
                    path.push_back(s.substr(start, end - start + 1));
                    dfs(end + 1);
                    path.pop_back();
                }
            }
        };

        dfs(0);
        return res;
    }
};