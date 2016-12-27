Permutation Sequence
========
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
```
"123"
"132"
"213"
"231"
"312"
"321"
```
Given n and k, return the kth permutation sequence.

这道题让我们寻找全排列的第k个是什么。

解法：这道题最主要就是找寻规律= =，反正巨蠢如我，没想出来，看了别人总结的[规律](http://www.cnblogs.com/grandyang/p/4358678.html)，然后做出来的。最后的递推式是

```
a1 = k / (n - 1)!
k1 = k

a2 = k1 / (n - 2)!
k2 = k1 % (n - 2)!
...

an-1 = kn-2 / 1!
kn-1 = kn-2 / 1!

an = kn-1 / 0!
kn = kn-1 % 0!
```
推导过程详见博主。

```
class Solution {
public:
    string getPermutation(int n, int k) {
        string res = "";
        string num = "123456789";
        vector<int> flag(n, 1);
        for (int i = 1; i < n; i++) flag[i] = flag[i - 1] * i;
        k--;
        for (int i = n; i >= 1; i--) {
            int j = k / flag[i - 1];
            res.push_back(num[j]);
            num.erase(j, 1);
            k %= flag[i - 1];
        }

        return res;
    }
};
```
