-- displaying all cities in the database
SELECT cities.id, cities.name states.name FROM states RIGHT JOIN cities ON states.id = cities.id ORDER BY cities.id ASC;
