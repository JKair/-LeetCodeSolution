Spiral Matrix II
================
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


这个题目是`Spiral Matrix`的变形，不让我们输出结果了，而是让我们生成矩阵。

这道题我们只要拿`Spiral Matrix`的代码稍微改装一下就可以得到结果了，如果你已经理解了`Spiral Matrix`，那这道题应该也难度不大。
```
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        if (n == 0) return {};
        int i = 0,top = 0,bot = n - 1,left = 0,right = n - 1,thisNum = 1;
        vector<vector<int>> res(n, vector<int>(n, 0));
        while (top <= bot || left <= right) {
            //往右边跑
            i = left;
            while (i <= right) {
                res[top][i++] = thisNum++;
            }
            if (++top > bot) break;
            //往下跑
            i = top;
            while (i <= bot) {
                res[i++][right] = thisNum++;
            }
            if (--right < left) break;
            //往左跑
            i = right;
            while (i >= left) {
                res[bot][i--] = thisNum++;
            }
            if (--bot < top) break;
            //往上跑
            i = bot;
            while (i >= top) {
                res[i--][left] = thisNum++;
            }
            if (++left > right) break;
        }

        return res;
    }
};
```

相似题目[Spiral Matrix](./Spiral Matrix)。
