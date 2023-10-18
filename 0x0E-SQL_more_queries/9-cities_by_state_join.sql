-- displaying all cities in the database
SELECT cities.id, cities.name FROM states INNER JOIN cities ON states.id = cities.id ORDER BY cities.id ASC;
