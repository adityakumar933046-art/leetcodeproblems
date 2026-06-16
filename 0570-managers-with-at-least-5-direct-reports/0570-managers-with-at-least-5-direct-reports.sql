# Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN Employee d
ON e.id = d.managerId
GROUP BY e.id, e.name
HAVING COUNT(*) >= 5;