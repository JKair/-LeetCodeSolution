Consecutive Numbers
========
Write a SQL query to find all numbers that appear at least three times consecutively.
```
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
```
For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

这道题让我们寻找连续出现三次的数字。

解法：我们只要将这个表用where来连接，找出相同的数字，然后id要连续的就好了。

```
# Write your MySQL query statement below
SELECT DISTINCT l1.Num as ConsecutiveNums From Logs l1, Logs l2, Logs l3
WHERE (l1.id = l2.id + 1 AND l1.Num = l2.Num)
AND (l1.Num = l3.Num AND l1.id = l3.id + 2)
```
