-- Description: Create table id_not_null with id and name columns, with id having default value 1

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

