-- Drop the "employees" table if it already exists to avoid conflicts
DROP TABLE IF EXISTS employees;

-- Create a new "employees" table with the following columns:
CREATE TABLE employees (
    -- id: unique identifier for each employee, automatically increments
    id SERIAL PRIMARY KEY,

    -- name: employee's name, this field cannot be empty
    name VARCHAR(255) NOT NULL,

    -- age: employee's age, this field cannot be empty
    age INTEGER NOT NULL,

    -- department: the department where the employee works, this field can be empty
    department VARCHAR(255) NULL
);

