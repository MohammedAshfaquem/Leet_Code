-- Write your PostgreSQL query statement below
SELECT email AS Email FROM Person GROUP BY  email HAVING Count(*)>1;