Add Binary
==========
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

这道题让我们进行二进制的加法。

这道题的难度并不高，这里写一种比较常规的解法，我们小时候做加法的时候是先把位对齐之后，进行加法，然后看进位不,在进行下一轮的加法。

我们实际上有三个任务要进行。
第一个是先判断哪个字符串比较长，第二个则是对齐，第三个才进行加法。

代码如下：
```
class Solution {
public:
    string addBinary(string a, string b) {
        if (a.size() < b.size()) return addBinary(b, a);
        string res = "";
        int plus = 0;
        for (int i = a.size() - b.size(); i > 0 ; i--) {
            b = '0' +  b;
        }

        for (int i = b.size() - 1; i >= 0; i--) {
            int temp = a[i] + b[i] - '0' - '0' + plus;
            if (temp == 2) {
                res += '0';
                plus = 1;
            } else if (temp == 3) {
                res += '1';
                plus = 1;
            } else {
                res += temp + '0';
                plus = 0;
            }
        }

        if (plus == 1) {
            res += '1';
        }

        reverse(res.begin(), res.end());

        return res;
    }
};
```
