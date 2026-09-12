-- Write your query below
SELECT name
FROM customers
WHERE customers.id NOT IN (
    SELECT customers.id
    FROM customers JOIN orders ON customers.id = orders.customer_id
)

