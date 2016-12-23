Excel Sheet Column Number
==========
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

这道题让我们把Excel的字母行转换成数字。

解法：这道题和进制转换差不多，把它当做26进制来算就好了。

```
class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            res = res * 26 + s[i] - 'A' + 1;
        }

        return res;
    }
};
```

相似题目[Excel Sheet Column Title](./Excel Sheet Column Title.md)
