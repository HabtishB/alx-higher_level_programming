-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa
  -- The states table contains only record where name = california (but the id can be different, as per the example)
  -- do not use JOIN keyword
  -- The database name will be passed as an argurment to the mysql command

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE NAME = "California")
ORDER BY id ASC;
