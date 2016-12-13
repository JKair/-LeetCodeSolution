Set Matrix Zeroes
================
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

这道题让我们当遇到0的之后，就把行和列全部都赋值为0，否则别动。

这道题最主要看我们对空间复杂度的优化。

解法一：空间复杂度为O(n²)的解法，创建一个新的容器，然后遍历原来那个，赋值过去。

```
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>> flag = matrix;

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    for (int k = 0; k < matrix.size(); k++) {
                        flag[k][j] = 0;
                    }
                    for (int k = 0; k < matrix[0].size(); k++) {
                        flag[i][k] = 0;
                    }
                }
            }
        }

        matrix = flag;
    }
};
```

解法二：空间复杂度为O(mn)的解法，这里我们创建两个数组，来记录行和列的情况就可以了，这样就节省了大量的空间。

```
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        vector<int> col(n,1), row(m,1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {
                    col[i] = 0;
                    row[j] = 0;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (col[i] == 0) {
                for (int k = 0; k < m; k++) {
                    matrix[i][k] = 0;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            if (row[i] == 0) {
                for (int k = 0; k < n; k++) {
                    matrix[k][i] = 0;
                }
            }
        }
    }
};
```

解法三：空间复杂度为O(n)的解法，实际上我们可以用表头来记录行和列的情况，这里有一个点，就是第一行和第一列的情况，我们需要额外创建多两个变量，看一下第一行和第一列是否需要变化为0.

```
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool row0 = false, col0 = false;
        int n = matrix.size(), m = matrix[0].size();

        for (int i = 0; i < n; i++) {
            if (matrix[i][0] == 0) col0 = true;
        }
        for (int i = 0; i < m; i++) {
            if (matrix[0][i] == 0) row0 = true;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (int i = 1; i < n; ++i) {
            for (int j = 1; j < m; ++j) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (row0) {
            for (int i = 0; i < m; i++) {
                matrix[0][i] = 0;
            }
        }
        if (col0) {
            for (int i = 0; i < n; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};
```
