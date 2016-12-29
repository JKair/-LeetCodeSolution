Delete Duplicate Emails
=====
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
```
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:
```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

这道题让我们删除重复的邮箱。

解法：我们可以用一个子查询group by 那些Email，然后筛选出比较小的那个id，只要是id不在这个子查询中的数据，全部都删除就可以了。

```
# Write your MySQL query statement below
DELETE
FROM
    Person
WHERE
    Id NOT IN (
select * from(
        SELECT
            min(Id)
        FROM
            Person
        GROUP BY
            Email)b
    )
```
