CREATE TABLE members (
    std_id SERIAL PRIMARY KEY,
    std_name TEXT NOT NULL,
    age INT,
    address TEXT,
    salary NUMERIC(10,2)
);

INSERT INTO members (std_name, age, address, salary)
VALUES
('Ahmed Hassan', 30, 'Cairo', 65000),
('Sara Ali', 25, 'Giza', 55000),
('Mariam Mostafa', 35, 'Cairo', 72000),
('Omar Khaled', 28, 'Alexandria', 60000),
('Nour Ahmed', NULL, 'Giza', 50000),
('Ali Mohamed', 40, 'Cairo', 80000),
('Salma Tarek', 22, 'Alexandria', 48000),
('Youssef Adel', 32, 'Giza', 67000),
('Mona Samir', 27, 'Cairo', 59000),
('Hana Mahmoud', 29, 'Giza', 61000),
('Karim Hany', 31, 'Cairo', 64000),
('Laila Hassan', 24, 'Alexandria', 52000);

SELECT * FROM members;

-- part a

-- task 1
ALTER TABLE members
ADD COLUMN email TEXT;

SELECT * FROM members;


-- task 2
ALTER TABLE members
ADD CONSTRAINT check_age
CHECK (age >= 0);


-- task 3
ALTER TABLE members
RENAME COLUMN address TO city;

SELECT * FROM members;


-- task 4
ALTER TABLE members
DROP COLUMN email;

SELECT * FROM members;



-- part b

-- task 5
SELECT *
FROM members
ORDER BY age DESC;


-- task 6
SELECT *
FROM members
ORDER BY city, std_name;


-- task 7
SELECT *
FROM members
ORDER BY age NULLS LAST;


-- task 8
SELECT std_name AS "member name"
FROM members;


-- task 9
SELECT std_name || ' - ' || city AS member_info
FROM members;


-- task 10
SELECT DISTINCT city
FROM members;


-- task 11
SELECT m.std_id, m.std_name
FROM members AS m
WHERE m.std_id > 5;



-- part c

-- task 12
SELECT city, COUNT(*) AS member_count
FROM members
GROUP BY city;


-- task 13
SELECT city, AVG(age) AS average_age
FROM members
GROUP BY city;


-- task 14
SELECT city, COUNT(*) AS member_count
FROM members
GROUP BY city
HAVING COUNT(*) > 1;


-- task 15
SELECT
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM members;


-- task 16
SELECT *
FROM members
ORDER BY std_id
LIMIT 5;


-- task 17
SELECT *
FROM members
ORDER BY std_id
LIMIT 5
OFFSET 5;


-- task 18
SELECT *
FROM members
ORDER BY std_id
LIMIT 5
OFFSET 15;



-- part d

-- task 19
SELECT * FROM members
-- then type ;


-- task 20
SELECT std_name AS member_name
FROM members;

SELECT std_name member_name
FROM members;


-- task 21
SELECT 'Ahmed' || ' Hassan';

SELECT 'Ahmed' + ' Hassan';



-- part e

-- task 22
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    name TEXT
);


-- task 23
INSERT INTO suppliers (name)
VALUES
    ('Tech Supplier'),
    ('Office Supplier'),
    ('Home Supplier');

SELECT * FROM suppliers;


-- task 24
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    supplier_id INT REFERENCES suppliers(supplier_id),
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    quantity INT
);


-- task 25
INSERT INTO products (
    product_name,
    supplier_id,
    price
)
VALUES
    ('Laptop', 1, 30000),
    ('Mouse', 1, 500),
    ('Desk', 2, 4000),
    ('Chair', 3, 2500);

SELECT * FROM products;

INSERT INTO orders (
    product_id,
    quantity
)
VALUES
    (1, 2),
    (1, 1),
    (2, 5),
    (3, 2);

SELECT * FROM orders;



-- part f

-- task 26
SELECT
    o.order_id,
    p.product_name,
    o.quantity
FROM orders AS o
INNER JOIN products AS p
ON o.product_id = p.product_id;


-- task 27
SELECT
    p.product_id,
    p.product_name,
    o.order_id,
    o.quantity
FROM products AS p
LEFT JOIN orders AS o
ON p.product_id = o.product_id;


-- task 28
SELECT
    p.product_id,
    p.product_name,
    o.order_id,
    o.quantity
FROM products AS p
FULL JOIN orders AS o
ON p.product_id = o.product_id;

-- all rows from both


-- task 29
SELECT
    p.product_name,
    o.order_id
FROM products AS p
CROSS JOIN orders AS o;

SELECT COUNT(*)
FROM products AS p
CROSS JOIN orders AS o;



-- challenge

SELECT
    p.product_id,
    p.product_name,
    COUNT(o.order_id) AS number_of_orders,
    AVG(o.quantity) AS average_quantity
FROM products AS p
LEFT JOIN orders AS o
ON p.product_id = o.product_id
GROUP BY
    p.product_id,
    p.product_name
HAVING COUNT(o.order_id) >= 2
ORDER BY number_of_orders DESC;



-- part g

-- task 30
SELECT *
FROM orders
WHERE order_id = 1;

DELETE FROM orders
WHERE order_id = 1;

SELECT * FROM orders;


-- task 31
TRUNCATE TABLE orders;

SELECT * FROM orders;


-- task 32
DROP TABLE orders;