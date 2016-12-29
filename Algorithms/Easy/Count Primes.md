Count Primes
=====
Description:

Count the number of prime numbers less than a non-negative number, n.

这道题让我们计算不小于n的素数有多少个。

解法：[埃拉托斯特尼筛法](http://baike.baidu.com/link?url=Jo-lP6fh2IfRl7-TL8Z9qivc5Df6PuADMjahIXIDU5Sx2J5DYN0tEhVIps3hV5ePbJPdi2sQJJT3ZrH2XjkUb5mf7-qB7upqmTO9wMKCKxhoxWO2Jhlzz99W_21rlLyUMOFlIS2kpKdtf6kidnDA8kVFxgOS77KHh-kYej7nqm)。

```
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> flag(n, false);

        for (int i = 2; i * i < n; i++) {
            if (!flag[i]) {
                for (int j = i; j * i < n; j++) {
                    flag[i * j] = true;
                }
            }
        }

        int res = 0;
        for (int i = 2; i < n; i ++) {
            if (!flag[i]) res++;
        }

        return res;
    }
};
```
