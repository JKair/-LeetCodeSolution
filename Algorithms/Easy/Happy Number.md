Happy Number
=====
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
```
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

这道题让我们计算happy number，具体怎么判断规则看一下上面的例子就知道了。

解法一：这道题我们要界定如何确定它不是happy number。其实我们按照它的定义，只知道happy number怎么界定，不知道怎么界定非happy number。那么我们来举一个数字，假设是9。
```
9^2 = 81
8^2 + 1^2 = 65
6^2 + 5^2 = 61
6^2 + 1^2 = 37 //我出现在后面
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4
4^2 = 16
1^2 + 6^2 = 37 //37又出现了
```
之后就会陷入无穷无尽的循环了，所以呢，我们就可以界定了，如果我们计算过程中，出现了之前计算过的非1的数，那么就可以认为它不是happy number。

整理成代码：
```
class Solution {
public:
    bool isHappy(int n) {
        int res = 0;
        vector<int> flag;
        while (true) {
            res = 0;
            while (n != 0) {
                res += ((n % 10) * (n % 10));
                n /= 10;
            }
            if (res == 1) return true;
            else if (find(flag.begin(), flag.end(), res) != flag.end()) return false;

            flag.push_back(res);
            n = res;
        }
    }
};
```

解法二：还有一种解法，就是可以优化空间的，根据论坛的大兄弟说`Using fact all numbers in [2, 6] are not happy`。我也不会证明。

```
class Solution {
public:
    bool isHappy(int n) {
        int res = 0;
        while (n > 6) {
            res = 0;
            while (n != 0) {
                res += ((n % 10) * (n % 10));
                n /= 10;
            }
            if (res == 1) return true;

            n = res;
        }

        return n == 1;
    }
};
```
