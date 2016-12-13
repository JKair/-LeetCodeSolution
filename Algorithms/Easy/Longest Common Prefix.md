Longest Common Prefix
====================

Write a function to find the longest common prefix string amongst an array of strings.

这道题让我们查许多字符串中最长公共前缀，我一开始以为是查找最长上升子序列，以为dp下可以直接搞定。然而并不是啊，理解错题目了，题目只是单纯给很多字符串，然后找出这一堆字符串中，最长的公共前缀而已，这道题的解法没有想出什么特别好的技巧，就是直接遍历搜索，然后遇到特殊情况则直接退出。

这里需要处理的情况，就是当我们搜索的当前字符串的长度小于这一次我们需要比对的第n个字符，就是说当前字符串的长度不超过n，那么则直接返回当前字符串，还有一种情况则是，比对的时候，下一个字符串的比对字符和当前不同，则返回n-1个字符。具体看程序理解吧。

```
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        for (int i = 0; i < strs[0].size(); i++) {
            for (int j = 0; j < strs.size() - 1; j++) {
                if (i >= strs[j].size() || strs[j][i] != strs[j+1][i]) {
                    return strs[j].substr(0, i);
                }
            }
        }

        return strs[0];
    }
};
```
