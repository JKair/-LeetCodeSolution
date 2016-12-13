Climbing Stairs
================
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

这道题让我们计算有N阶楼梯，一共可能会有多少种走的方法。

解法一：其实就是菲波那切数列，假设有5阶楼梯，我们可以这样想，最后一步肯定是走1步或者走2步的，那么就是剩余4阶和3阶楼梯。也就是说，5阶楼梯，就是3和4阶楼梯的和。dp解法

```
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1)  return 1;
        int res[n] = {1};
        res[1] = 2;

        for (int i = 2; i < n; i++) {
            res[i] = res[i - 1] + res[i - 2];
        }

        return res[n-1];
    }
};
```


解法二：针对上面那道题，我们可以优化空间到O(1)

```
class Solution {
public:
    int climbStairs(int n) {
        int a = 1,b = 1;

        while (n--) {
            b += a;
            a = b - a;
        }

        return a;
    }
};
```
