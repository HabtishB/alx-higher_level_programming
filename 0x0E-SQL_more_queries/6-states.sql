-- A script that creates database hbtn_0d_usa and a table states
  -- states description:
    -- id INT unique auto generated can't be null and is a primary key
    -- name VARCHAR(256) can't be null
  -- if the database hbtn_0d_usa already exists, your script should not fail
  -- if the table states already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
      id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(256)
);
