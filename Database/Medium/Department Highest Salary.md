Department Highest Salary
=========
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.
```
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```
The Department table holds all departments of the company.
```
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.
```
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```

这道题让我们找出在一个部门里面工资最高的人。

解法：这道题处理起来比较复杂，我们需要在选择字段的时候，选出一个最大值，然后再在条件里面分别对薪水和部门进行筛选

```
# Write your MySQL query statement below
Select D.Name as Department, E.Name as Employee, MAX_X.MAXS as Salary
FROM Employee as E,Department as D,(SELECT max(Salary) as MAXS,DepartmentId From Employee Group by DepartmentId) as MAX_X
WHERE E.Salary = MAX_X.MAXS AND E.DepartmentId = D.Id AND
  E.DepartmentId = MAX_X.DepartmentId;
```
