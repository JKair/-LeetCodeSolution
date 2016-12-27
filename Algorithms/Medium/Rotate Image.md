Rotate Image
=========
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

这道题给我们一个矩阵，然后让我们计算出旋转90°之后的矩阵。

解法一：我们可以折一下右上和左下的对角线，然后再对折中线，就可以得到这个旋转之后的矩阵了。

```
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i; j++) {
                swap(matrix[i][j], matrix[n - j - 1][n - i - 1]);
            }
        }

        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n; j++) {
                swap(matrix[i][j], matrix[n - i - 1][j]);
            }
        }
    }
};
```

解法二：我们还可以先对折一下左上角和右下角的对角线，然后再把每一行都翻转，就可以得到这个旋转之后的矩阵了。

```
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }

            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```
