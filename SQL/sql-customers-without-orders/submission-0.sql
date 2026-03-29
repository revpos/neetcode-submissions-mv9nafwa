SELECT c.name
FROM orders AS o
RIGHT JOIN customers AS c
    ON c.id = o.customer_id
WHERE o.id IS NULL