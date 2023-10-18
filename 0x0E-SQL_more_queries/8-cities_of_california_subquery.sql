-- list all cities in california
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id;
