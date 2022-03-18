-- creates the table force_name on your MySQL server.
  -- force_name description:
    -- id INT
    -- name VARCHAR(256)
  -- The database name will be passed as an argument of the mysql command
  -- if the table exists, it shouldn't fail

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
