Nth Highest Salary
========
Write a SQL query to get the nth highest salary from the Employee table.
```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.


这道题让我们选出薪水第N高的数。

解法：因为是第N高，下标是从0开始的，所以我们可以用`ORDER BY + GROUP BY + OFFSET`解决。

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee GROUP BY Salary
      ORDER BY Salary DESC LIMIT 1 OFFSET N
  );
END
```

相似题目[Second Highest Salary](../Easy/Second Highest Salary.md)
