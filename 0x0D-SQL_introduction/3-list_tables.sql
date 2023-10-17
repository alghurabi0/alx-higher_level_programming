-- List all tables in the specified database

-- This query retrieves the table names
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE(); -- This uses the currently selected database

-- If you want to use a specific database name provided as an argument to the mysql command, you can remove the DATABASE() function and use the following instead:
-- WHERE table_schema = 'your_database_name';
