Basic Calculator II
=======
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
```
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
```

这道题让我们计算一条等式的结果，但是只有加减乘除。

解法：我们把解题分成两个过程，一个是去掉非法字符，另外一个是计算。计算的话，我们利用栈，如果是加法，那么直接入栈，如果是减法，那么就入栈这个数的反数，如果是乘法就用当前数和栈顶相乘放回去，除法亦然。

```
class Solution {
public:
    int cal(string s) {
        stack<int> temp;
        int flag = 0;
        char last = '+';
        for (int i = 0; i < s.size(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                flag = flag * 10 + s[i] - '0';
            }
            if (i == s.size() - 1 || s[i] < '0'){
                if (last == '+') temp.push(flag);
                else if (last == '-') temp.push(-flag);
                else if (last == '*') {
                    int topNum = temp.top();
                    temp.pop();
                    temp.push(topNum * flag);
                } else {
                    int topNum = temp.top();
                    temp.pop();
                    temp.push(topNum / flag);
                }

                last = s[i];
                flag = 0;
            }
        }
        int res = 0;
        while (!temp.empty()) {
            res += temp.top();
            temp.pop();
        }

        return res;
    }

    int calculate(string s) {
        string temp = "";

        for (int i = 0; i < s.size(); i++) {
            if ((s[i] >= '0' && s[i] <= '9') || s[i] == '+' || s[i] == '/' || s[i] == '*' || s[i] == '-') {
                temp += s[i];
            }
        }

        return cal(temp);
    }
};
```
