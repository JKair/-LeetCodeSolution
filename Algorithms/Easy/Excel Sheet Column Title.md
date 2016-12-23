Excel Sheet Column Title
=======
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

这里让我们像Excel那样，弄一个行数表示出来，用过excel应该知道，就是行标题那里那种方式。

解法：这个就是一直取余然后除以就好了，注意的点在于每次循环开始的时候，要减去一，因为我们要计算的是第几个，从0开始的。

```
class Solution {
public:
    string convertToTitle(int n) {
        string res = "";

        while (n > 0) {
            n -= 1;
            res = char((n % 26) + 'A') + res;
            n /= 26;
        }

        return res;
    }
};
```

相似题目[Excel Sheet Column Number](./Excel Sheet Column Number.md)
