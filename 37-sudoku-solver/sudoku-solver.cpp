class Solution {
public:
    int row[9], col[9], box[9];
    vector<pair<int,int>> empties;

    void flip(int r, int c, int d) {
        int bit = 1 << d;
        row[r] ^= bit;
        col[c] ^= bit;
        box[(r / 3) * 3 + c / 3] ^= bit;
    }

    bool dfs(vector<vector<char>>& board, int cnt) {
        if (cnt == (int)empties.size()) return true;

        // pick the empty cell with the fewest candidates (MRV)
        int best = cnt, bestMask = 0, bestCount = 10;
        for (int i = cnt; i < (int)empties.size(); i++) {
            auto [r, c] = empties[i];
            int mask = ~(row[r] | col[c] | box[(r / 3) * 3 + c / 3]) & 0x1FF;
            int k = __builtin_popcount(mask);
            if (k < bestCount) {
                bestCount = k;
                best = i;
                bestMask = mask;
                if (k <= 1) break;
            }
        }
        if (bestCount == 0) return false;

        swap(empties[cnt], empties[best]);
        auto [r, c] = empties[cnt];

        while (bestMask) {
            int d = __builtin_ctz(bestMask);
            bestMask &= bestMask - 1;
            flip(r, c, d);
            board[r][c] = '1' + d;
            if (dfs(board, cnt + 1)) return true;
            flip(r, c, d);
        }
        board[r][c] = '.';
        swap(empties[cnt], empties[best]);
        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        memset(row, 0, sizeof row);
        memset(col, 0, sizeof col);
        memset(box, 0, sizeof box);
        empties.clear();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') empties.push_back({r, c});
                else flip(r, c, board[r][c] - '1');
            }
        }
        dfs(board, 0);
    }
};