Customers Who Never Order
=========
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.
```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```
Table: Orders.
```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```
Using the above tables as example, return the following:
```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

这道题让我们找出没有下过单的用户。

解法：我们可以先用一个子查询找出下过单的用户，然后用not in解决这个问题。

```
# Write your MySQL query statement below
select Name as Customers from Customers Where id NOT IN(
select CustomerId from Orders
)
```
