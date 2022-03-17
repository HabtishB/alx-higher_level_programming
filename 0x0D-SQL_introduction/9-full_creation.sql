-- script creates table second table in the database

CREATE TABLE IF NOT EXISTS second_table(
     id INT,
     name VARCHAR(256),
     score 101
);

INSERT INTO second_table(id, name, score)
VALUES (1, "JOHN", 10),
       (2, "Alex", 3),
       (3, "Bob", 14),
       (4, "George", 8);
