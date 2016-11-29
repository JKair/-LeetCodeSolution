N-Queens
==========
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

N皇后问题，最经典的算法之一了。给我们n个皇后，让我们在n * n的情况下保持皇后放置位置合法（就是对角线和左右上下都不能有其他皇后）

此题我们要解它，必须完成三个任务，第一个是尝试放置棋子，第二个是判断是否合法，第三个是生成棋盘。

解法一：递归回溯
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
    void dfs(vector<vector<string>> &res, vector<int> &temp, int col, int n) {
        if (col == n) {  //如果已经放满了皇后，则写入结果
            vector<string> flag(n, string(n, '.'));

            for (int i = 0; i < n; i++) {
                flag[i][temp[i]] = 'Q';
            }
            res.push_back(flag);

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
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<int> temp(n, -1);
        dfs(res, temp, 0, n);

        return res;
    }
};
```

相似问题[N-Queens II](./N-Queens II.md)
