-- Description: Create table unique_id with id and name columns, with id having default value 1 and being unique

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

