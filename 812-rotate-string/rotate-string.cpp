class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.size();
        if (n != (int)goal.size()) return false;
        string t = s + s;

        
        vector<int> lps(n, 0);
        for (int i = 1, k = 0; i < n; i++) {
            while (k > 0 && goal[i] != goal[k]) k = lps[k - 1];
            if (goal[i] == goal[k]) k++;
            lps[i] = k;
        }

        
        for (int i = 0, k = 0; i < (int)t.size(); i++) {
            while (k > 0 && t[i] != goal[k]) k = lps[k - 1];
            if (t[i] == goal[k]) k++;
            if (k == n) return true;
        }
        return false;
    }
};