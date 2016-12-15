Palindrome Partitioning
===========
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

给一个字符串，让我们列出它的所有子字符串是回文的情况。

解法：我们还是可以用dfs去解决问题，但是有一个点，就是我们需要判断当前的子字符串是不是回文，所以我们需要加多一个函数判断。

```
class Solution {
public:
    bool isPalindrome(string s,int start,int end) {
        while (start < end){
            if (s[start] != s[end]) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    void dfs(string s,int start,vector<string> &temp, vector<vector<string>> &res) {
        if (start == s.size()) {
            res.push_back(temp);
            return;
        }

        for (int i = start; i < s.size();i++) {
            if (isPalindrome(s, start, i)) {
                temp.push_back(s.substr(start, i - start + 1));
                dfs(s, i+1, temp, res);
                temp.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<string> temp;
        vector<vector<string>> res;
        dfs(s,0,temp,res);
        return res;
    }
};
```
