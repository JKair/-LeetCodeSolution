Longest Substring Without Repeating Characters
========================

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

这道题让我们找出没有重复的连续字符串的长度，暴力搜索肯定是不能过的，所以我没试。这里的最佳解法是滑窗，

假设我们有一个窗，这个窗左边和右边都可以伸缩，以`pwwkew`为例，一开始，窗的长度为1，只有一个字符，然后右边窗口继续向右边拉长，当窗口覆盖`pww`的时候，由于最后一个字符已经出现过了，所以左边的窗口往右跑一个，也就是上次w出现的地方+1格，也就是左边窗口直接缩到第二个w的地方，这样窗口的场地又变回1了，然后我们维护一个最大值，最后字符跑完的时候，最大值则为所求。

具体到程序写法，我们用一个leftSide来记录左边边界，用一个长度为256的数组去记录字符上次出现的地方，res记录最大长度。开始循环字符串，当遇到这个字符没有出现过，或者记录的出现的位置，小于当前leftSide的位置的时候，则维护res。否则，则让leftSide跳到记录的位置+1。


```
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int flag[256] = {0}, leftSide = 0, res = 0;

        for (int i = 0; i < s.size(); i++) {
            if (flag[s[i]] == 0 || leftSide > flag[s[i]]) {
                res = max(i - leftSide + 1, res);
            } else {
                leftSide = flag[s[i]];
            }

            flag[s[i]] = i + 1;
        }

        return res;
    }
};
```


还有其他的写法，但是思想基本都差不多，也是滑窗，只是用set去记录字符来判断重复，[官方给的解答](https://leetcode.com/articles/longest-substring-without-repeating-characters/)就是这种写法，具体可以参照。
