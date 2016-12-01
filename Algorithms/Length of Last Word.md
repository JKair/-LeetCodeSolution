Length of Last Word
===================
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

这道题让我们数一下，倒数第一个单词的长度是多少。

这道题的难度并不高，我们只要从后面往前遍历，是字母的时候，就开始数字母的个数，当遇到不是字母的时候，就直接返回就好了。

```
class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0, n = s.size();
        if (n == 0) return 0;
        if (!((s[n - 1] >= 'a' && s[n - 1] <= 'z') || (s[n - 1] >= 'A' && s[n - 1] <= 'Z'))) {
            return lengthOfLastWord(s.substr(0, n-1));
        }


        for (int i = s.size() - 1; i >= 0; i--) {
            if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
                res++;
                continue;
            } else {
                return res;
            }
        }

        return res;
    }
};
```
