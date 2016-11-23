Letter Combinations of a Phone Number
======================

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

这道题是让我们列出，我们按手机的按键，有多少种组合的可能性。

关于这种题目，一般只要深度优先遍历则可以解决问题了。

```
class Solution {
public:
    void dfs(string digits, vector<string> &res, string dict[], string &temp, int now) {
        if (temp.size() == digits.size()) {
            res.push_back(temp);
            return;
        }

        string tempDict = dict[digits[now] - '2'];
        for (int j = 0; j < tempDict.size(); j++) {
            temp.push_back(tempDict[j]);
            dfs(digits,res,dict,temp,now+1);
            temp.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits == "") return {};
        vector<string> res;
        string temp;
        string dict[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        dfs(digits, res, dict, temp, 0);

        return res;
    }
};
```
