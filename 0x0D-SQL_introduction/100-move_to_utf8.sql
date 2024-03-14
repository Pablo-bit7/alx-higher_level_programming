-- Description: Converts the entire database hbtn_0c_0 to UTF8

/* Convert database to UTF8 */
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* Convert all tables and their columns to UTF8 */
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

