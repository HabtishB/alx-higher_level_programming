-- script creates table second table in the database

USE hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
     id INT,
     name VARCHAR(256),
     score INT
);

INSERT INTO second_table(id, name, score)
VALUES ROW(1, "JOHN", 10),
       ROW(2, "Alex", 3),
       ROW(3, "Bob", 14),
       ROW(4, "George", 8);
