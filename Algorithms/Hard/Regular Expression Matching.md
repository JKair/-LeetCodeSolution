Regular Expression Matching
=========
```
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```

这道题让我们写一个正则表达式匹配器，但是我们只要处理`.`和`*`的情况

解法：这道题，啊。。。。。还是没想出来，然后看了别人的解法。利用递归可以解决这道题，分四种情况。

1. 如果p为空，那么s为空则返回true
1. 如果p的长度为1，那么s也必须为1而且要么相等要么p为`.`
1. 如果第二个不是`*`，那么必须满足上相等或者p[0]为`.`，如果匹配上了，那么就递归去掉p和s的第一个字符，如果s为空，那么返回false。
1. 如果第二个是`*`，那么只要前面（0~1）的匹配式匹配的上则去掉s的第一个字符，匹配到匹配不上这个匹配式则退出。


```
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty()) return s.empty();
        if (p.size() == 1) return s.size() == 1 && (s[0] == p[0] || p[0] == '.');
        if (p[1] != '*') {
            if (s.empty()) return false;
            else return (p[0] == s[0] || p[0] == '.') && isMatch(s.substr(1), p.substr(1));
        }
        while (!s.empty() && (p[0] == s[0] || p[0] == '.')) {
            if (isMatch(s, p.substr(2))) return true;
            s = s.substr(1);
        }

        return isMatch(s, p.substr(2));
    }
};
```
