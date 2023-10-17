-- Retrieve the full table description for first_table
SELECT table_name AS 'Table', CREATE_TABLE AS 'Create Table'
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
