Decode Ways
===========
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

这道题给我们一串数字，让我们技术出可以解码的次数。

解法：这道题整体感觉有点和爬楼梯相似，但是多了一些条件限制，就是只有26个字母，只要处理好就行了

```
class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || (s.size() > 1 && s[0] == '0')) return 0;
        vector<int> dp(s.size() + 1, 0);
        dp[0] = 1;

        for (int i = 1; i <= s.size(); i++) {
            dp[i] = s[i - 1] == '0' ? 0 : dp[i - 1];
            if (i > 1 && (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6'))) {
                dp[i] += dp[i - 2];
            }
        }

        return dp.back();
    }
};
```
