Duplicate Emails
=======
Write a SQL query to find all duplicate emails in a table named Person.
```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```
For example, your query should return the following for the above table:
```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

这道题让我们找出有邮箱一样的邮箱。

解法：这道题最主要考察的就是对groupby 还有having的使用
```
# Write your MySQL query statement below
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) > 1
```
