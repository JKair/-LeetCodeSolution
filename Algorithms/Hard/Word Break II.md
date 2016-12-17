Word Break II
========
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

这道题和`Word Break`解决的思路差不多，我们可以用深度遍历解决，但是直接遍历完是不行的，必须去掉一些特殊情况，我们可以用一个flag数组去记录，如果不能这样分解，就直接跳过

```
class Solution {
public:
    void wordBreak(string s, unordered_set<string>& wordDict, vector<bool> &flag, vector<string> &res,string &temp, int start) {
        if (start == s.size()) {
            res.push_back(temp.substr(0, temp.size() - 1));
            return;
        }

        for (int i = start; i < s.size() ;i++) {
            string word = s.substr(start, i - start + 1);

            if (wordDict.find(word) != wordDict.end() && flag[i + 1]) {
                temp.append(word).append(" ");
                int beforeSize = res.size();
                wordBreak(s, wordDict, flag, res, temp, i+1);
                if (res.size() == beforeSize) flag[i + 1] = false;
                temp.resize(temp.size() - word.size() - 1);
            }
        }
    }

    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
        vector<bool> flag(s.size() + 1, true);
        vector<string> res;
        string temp = "";
        wordBreak(s,wordDict,flag,res,temp,0);

        return res;
    }
};
```

相似题目[Word Break](../Medium/Word Break.md)
