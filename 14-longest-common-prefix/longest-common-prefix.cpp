class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        const string& first = strs[0];
        
        for (int i = 0; i < first.size(); ++i) {
            for (int j = 1; j < strs.size(); ++j) {
                if (i == strs[j].size() || strs[j][i] != first[i]) {

                    return first.substr(0, i);
                }
            }
        }
        return first;
    }
};