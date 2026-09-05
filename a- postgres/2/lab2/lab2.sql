CREATE TABLE products (
 product_id integer PRIMARY KEY,
 name text UNIQUE,
 price numeric CHECK (price > 0)
);

CREATE TABLE orders (
 order_id integer PRIMARY KEY,
 product_id integer REFERENCES products(product_id),
 quantity numeric DEFAULT 1
);
-- test 1 -----------------
INSERT INTO products (
 product_id,
 name,
 price
)
VALUES (
 1,
 'ranch',
 -500
);

INSERT INTO products (
 product_id,
 name,
 price
)
VALUES (
 1,
 'ranch',
 500
);

-- test 2 -------------
INSERT INTO orders (
 order_id,
 product_id
)
VALUES (
 1,
 1
);

SELECT * from orders

-- part c: ------------
INSERT INTO products (
    product_id,
    name,
	price
)
VALUES
    (2,'bread',250),
    (3,'butter',400);

INSERT INTO orders (
 order_id,
 product_id,
 quantity
)
VALUES
 (2,2,4),
 (3,2,6);

INSERT INTO orders (
 order_id,
 product_id,
 quantity
)
VALUES
 (4,4,2);
-- part d :
DELETE FROM products WHERE product_id = 1;
-- part e :
DROP TABLE orders;
CREATE TABLE orders (
 order_id integer PRIMARY KEY,
 product_id integer REFERENCES products(product_id) ON DELETE CASCADE,
 quantity numeric DEFAULT 1
);

INSERT INTO orders (
 order_id,
 product_id
)
VALUES (
 1,
 1
);

SELECT * from products -- 3 prod
SELECT * from orders   -- one order refrenced to prod 1

DELETE FROM products WHERE product_id = 1;

-- Practical Challenge ----------
CREATE TABLE categories (
 category_id SERIAL PRIMARY KEY,
 category_name VARCHAR(50) NOT NULL UNIQUE	
);

ALTER TABLE products
ADD COLUMN category_id INT;

ALTER TABLE products
ADD CONSTRAINT fk_product_category
FOREIGN KEY (category_id)
REFERENCES categories(category_id)
ON DELETE RESTRICT;

INSERT INTO categories (category_name)
VALUES
    ('Electronics'),
    ('Clothing'),
    ('Food');
	
SELECT * FROM categories;
SELECT * FROM products;

UPDATE products
SET category_id = 1
WHERE product_id = 1;

UPDATE products
SET category_id = 2
WHERE product_id = 2;

UPDATE products
SET category_id = 3
WHERE product_id = 3;

DELETE FROM categories WHERE category_id = 1;