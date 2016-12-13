Valid Sudoku
=================
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

验证数独板，这道题其实就是让我们判断每一列和每一行还有每个盒子里面是不是1~9每个数都不重复。

这道题用动态规划可以解决，我们用三个数组记录数字的情况，分别是行列还有盒子。最主要是盒子哪里怎么记录要斟酌一下。

代码如下：
```
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        if (board.empty() && board[0].empty()) return false;
        vector<vector<bool>> col(board.size(), vector<bool>(board[0].size(), false));
        vector<vector<bool>> row(board.size(), vector<bool>(board[0].size(), false));
        vector<vector<bool>> box(board.size(), vector<bool>(board[0].size(), false));

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] > '9' || board[i][j] < '1') continue;

                int temp = board[i][j] - '1';
                if (col[i][temp] || row[j][temp] || box[3 * ( i / 3 ) + j / 3][temp]) {
                    return false;
                }

                col[i][temp] = true;
                row[j][temp] = true;
                box[3 * ( i / 3 )+ j / 3][temp] = true;
            }
        }

        return true;
    }
};
```
