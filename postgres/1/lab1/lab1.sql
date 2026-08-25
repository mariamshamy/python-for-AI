CREATE TABLE employees (
 employee_id integer
 GENERATED ALWAYS AS IDENTITY
 PRIMARY KEY,
 first_name varchar(50) NOT NULL,
 last_name varchar(50) NOT NULL,
 phone varchar(20),
 age smallint CHECK (age >= 18),
 salary numeric(10,2)
 CHECK (salary >= 0)
);

INSERT INTO employees (
 first_name,
 last_name,
 phone,
 age,
 salary
)
VALUES (
 'Ahmed',
 'Hassan',
 '01012345678',
 30,
 65000
);

INSERT INTO employees (
    first_name,
    last_name,
    phone,
    age,
    salary
)
VALUES (
    'Sara',
    'Ali',
    '01198765432',
    25,
    55000
);

INSERT INTO employees (
    first_name,
    last_name,
    phone,
    age,
    salary
)
VALUES (
    'Mariam',
    'Mostafa',
    '01234567890',
    35,
    72000
);

SELECT * FROM employees;

--or do this 
/*
INSERT INTO employees (
    first_name,
    last_name,
    phone,
    age,
    salary
)
VALUES
    ('Ahmed', 'Hassan', '01012345678', 30, 65000),
    ('Sara', 'Ali', '01198765432', 25, 55000),
    ('Mariam', 'Mostafa', '01234567890', 35, 72000);
*/

INSERT INTO employees (
 first_name,
 last_name,
 phone,
 age,
 salary
)
VALUES (
 'Fatma',
 'Elraey',
 '01020304050',
 24,
 50000
)
RETURNING *
-------------------- q3 -----
INSERT INTO employees (
    first_name,
    last_name,
    phone,
    age,
    salary
)
VALUES (
    'Ali',
    'Mahmoud',
    '01011112222',
    16,
    50000
);
--The insertion fails because the employee's age is 16, which violates the CHECK constraint that requires age to be at least 18
--ERROR:  new row for relation "employees" violates check constraint "employees_age_check" Failing row contains (5, Ali, Mahmoud, 01011112222, 16, 50000.00). 


INSERT INTO employees (
    first_name,
    last_name,
    phone,
    age,
    salary
)
VALUES (
    'Ali',
    'Mahmoud',
    '01011112222',
    16,
    -50000
);
-- ERROR:  new row for relation "employees" violates check constraint "employees_age_check" Failing row contains (6, Ali, Mahmoud, 01011112222, 16, -50000.00). 
-- company_db=# drop database company_db;
--   ERROR:  cannot drop the currently open database
-- to drop database we should not connect to it, so we can connect to postgres database first and make sure that it is also not openned in th pgadmin prog or any other then try to drop it, it will be successfully dropped 