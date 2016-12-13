Pow(x, n)
=========
Implement pow(x, n).

算一个数的n平方

关于幂的计算，一般都是使用快速幂去解决，我们很容易可以推导，如果我们的基数不是x而是x*x的话，那么n就可以变成n/2，这样循环下去，我们计算的次数会减少很多。

```
class Solution {
public:
    double halfPow(double x, int n) {
        if (n == 0) return 1;
        double res = 1;
        bool flag = false;
        if (n < 0) {
            flag = true;
            n = -n;
        }
        while (n) {
            if (n & 1)
                res = res * x;
            x *= x;
            n /= 2;
        }

        return flag ? 1/res : res;
    }
    double myPow(double x, int n) {
        return halfPow(x, n);
    }
};
```
