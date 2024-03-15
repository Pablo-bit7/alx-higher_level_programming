-- Description: List all cities of California without using JOIN

-- Select all cities of California
SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

