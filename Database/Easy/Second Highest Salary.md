Write a SQL query to get the second highest salary from the Employee table.
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

这道题让我们选出第二高的薪水。

解法：我们先选出最高的薪水，然后再选一个小于这个薪水的最高的薪水就可以了，一个子查询。

```
# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
```
