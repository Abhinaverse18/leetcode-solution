class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        if ((int)word.size() > m * n) return false;

        // 1. Frequency check
        int cnt[128] = {0};
        for (auto& row : board)
            for (char c : row) cnt[c]++;
        for (char c : word)
            if (--cnt[c] < 0) return false;

        // 2. Start from the rarer end of the word
        int first = 0, last = 0;
        for (auto& row : board)
            for (char c : row) {
                if (c == word.front()) first++;
                if (c == word.back()) last++;
            }
        if (first > last) reverse(word.begin(), word.end());

        // 3. DFS from every cell
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (dfs(board, word, i, j, 0)) return true;
        return false;
    }

private:
    bool dfs(vector<vector<char>>& board, const string& word, int i, int j, int k) {
        if (board[i][j] != word[k]) return false;
        if (k == (int)word.size() - 1) return true;

        char tmp = board[i][j];
        board[i][j] = '#';  // mark visited

        static const int dx[4] = {1, -1, 0, 0};
        static const int dy[4] = {0, 0, 1, -1};
        for (int d = 0; d < 4; d++) {
            int x = i + dx[d], y = j + dy[d];
            if (x >= 0 && x < (int)board.size() && y >= 0 && y < (int)board[0].size()
                && board[x][y] != '#' && dfs(board, word, x, y, k + 1)) {
                board[i][j] = tmp;
                return true;
            }
        }

        board[i][j] = tmp;  // backtrack
        return false;
    }
};