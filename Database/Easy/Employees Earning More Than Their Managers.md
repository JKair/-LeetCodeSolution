Employees Earning More Than Their Managers
========

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.
```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

这道题让我们查一下，那个员工的工资高于他的上级。

解法：我们可以同时加入这两张表，用where描述上述条件就可以了，比较简单。

```
# Write your MySQL query statement below
select a.Name as Employee from Employee a,Employee b where a.ManagerId = b.id and a.Salary > b.Salary
```
