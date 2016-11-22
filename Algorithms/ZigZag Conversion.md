ZigZag Conversion
==================

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

这道题最主要就是弄懂排序，究竟是怎么排序的，用数字来表示`01234567890`，如果numRows是3的话，那么排列的顺序如下：
```
0   4   8
1 3 5 7 9
2   6   0
```
如果是4的话，那么则是
```
0   7
1 6 8
2 5 9
4   0
```
这道题其实并不需要考虑得太复杂，我们只要建立一个容器，或者数组都行，然后模拟排序的过程就好了，时间复杂度为O(N)

代码如下：
```
class Solution {
public:
    string convert(string s, int numRows) {
        if (s.size() <= numRows || numRows == 1) {
            return s;
        }

        vector<string> res(numRows, "");
        int temp = 1, now = 0;
        string last = "";
        for (int i = 0; i < s.size(); i++) {
            res[now] += s[i];
            if (now == numRows - 1) {
                temp = -1;
            }
            if (now == 0) {
                temp = 1;
            }

            now += temp;
        }

        for (int i = 0; i < res.size(); i++) {
            last += res[i];
        }

        return last;
    }
};
```
