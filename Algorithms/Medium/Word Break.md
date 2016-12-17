Word Break
======
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

这道题给我们一个字典，然后问我们能不能用字典里面的单词组成给定的字符。

解法：这道题我们要反着思考，我们需要验证的并不是拿着字典里面的字符反向验证字符串，而是将字符串拆解来验证字典，但是直接暴力搜索就太不科学了，所以我们应该做到减少计算的数量。我们用一个数组表示，从0开始到i这个位置的字符串是否存在于字典，这样我们就只要关注j循环到的次数的剩下的字符串，如果那一段也匹配了，就代表整段字符串都成功了。

```
class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        if (wordDict.size() == 0) return false;

        vector<bool> res(s.size() + 1, false);
        res[0] = true;

        for (int i = 1; i <= s.size(); i++) {
            for (int j = 0; j < i ; j++) {
                if (res[j] && wordDict.find(s.substr(j, i-j)) != wordDict.end()) {
                    res[i] = true;
                    break;
                }
            }
        }

        return res[s.size()];
    }
};
```

相似题目[Word Break II](../Hard/Word Break II.md)
