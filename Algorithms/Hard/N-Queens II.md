N-Queens II
============
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

这道题是`n-queens`的改版，要我们不生成棋盘了，直接计算数量就好了。

解法和`n-queens`一样。
```
class Solution {
public:
    bool canPlace(vector<int> &temp, int row, int col) {
        for (int i = 0; i < col; i++) {
            if (row == temp[i] || abs(col - i) == abs(row - temp[i])) { //判断对角线或者上下左右是否有棋子
                return false;
            }
        }

        return true;
    }
    void dfs(int &res, vector<int> &temp, int col, int n) {
        if (col == n) {  //如果已经放满了皇后，则写入结果
            res++;

            return ;
        }
        for (int row = 0; row < n; row++) {
            if (canPlace(temp, row, col)) { //判断能不能放置
                temp[col] = row;  //当前这一列放置在row上
                dfs(res, temp, col + 1, n); //放置下一个皇后
                temp[col] = -1;
            }
        }
    }
    int totalNQueens(int n) {
        int res = 0;
        vector<int> temp(n, -1);
        dfs(res, temp, 0, n);

        return res;
    }
};
```

相似问题[N-Queens](./N-Queens.md)
