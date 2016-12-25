Rank Scores
====
Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```
For example, given the above Scores table, your query should generate the following report (order by highest score):
```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

这道题让我们根据成绩给那些成绩一个排行版，并且按照成绩从大到小排列。

解法：我们只要知道比这个分数大的成绩个数有多少个就可以了，所以我们可以通过一个子查询解决。

```
# Write your MySQL query statement below
SELECT Score,(SELECT count(DISTINCT Score) FROM Scores WHERE Score >= s.Score ) Rank
FROM Scores s ORDER BY Score DESC
```
