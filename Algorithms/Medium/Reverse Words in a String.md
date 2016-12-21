Reverse Words in a String
========
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

这道题让我们把字符串的单词翻转，而且空间限制为O(1)

解法一：用`issteamstring`，根据空格去读取字符串，然后往前插入则可以

```
class Solution {
public:
    void reverseWords(string &s) {
        istringstream iss(s);
        s = "";
        string temp = "";
        while (getline(iss, temp, ' ')) {
            if (temp.empty()) continue;
            s = s.empty() ? temp : temp + " " + s;
        }
    }
};
```

解法二：将整个字符串都翻转，然后再将每个单词都翻转。

```
class Solution {
public:
    void reverseWords(string &s) {
        int storeIndex = 0, n = s.size();
        reverse(s.begin(), s.end());
        for (int i = 0; i < n; ++i) {
            if (s[i] != ' ') {
                if (storeIndex != 0) s[storeIndex++] = ' ';
                int j = i;
                while (j < n && s[j] != ' ') s[storeIndex++] = s[j++];
                reverse(s.begin() + storeIndex - (j - i), s.begin() + storeIndex);
                i = j;
            }
        }
        s.resize(storeIndex);
    }
};
```
