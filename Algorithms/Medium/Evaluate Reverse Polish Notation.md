Evaluate Reverse Polish Notation
======
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+, -, *, /.` Each operand may be an integer or another expression.
```
Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
```

这道题是让我们把[逆波兰式](http://baike.baidu.com/link?url=McQ_qEs45SyZhSOgRbu5q6zLHfteKe70S-OcuPX173Cm5vl8jSevn93bbdQMCSBL9TQcmz3XYQltHy1igpyzgFynxBpCEbeahfLm0mWd23Ih5eJ2AgvYJvRT37XIuak6)的结果计算出来

解法：关于计算器相关的，第一选择肯定是栈啦，我们从第一个遍历到最后一个，遇到数字就入栈，遇到字符就计算最后两个，再push回去，这样就能得到结果啦。

```
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> temp;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                temp.push(atoi(tokens[i].c_str()));
            } else {
                int b = temp.top();
                temp.pop();
                int a = temp.top();
                temp.pop();
                if (tokens[i] == "+") temp.push(a+b);
                else if (tokens[i] == "-") temp.push(a-b);
                else if (tokens[i] == "*") temp.push(a*b);
                else if(tokens[i] == "/") temp.push(a/b);
            }
        }

        return temp.top();
    }
};
```
