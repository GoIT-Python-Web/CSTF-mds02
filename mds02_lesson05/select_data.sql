SELECT id, name AS fullname
FROM contacts AS c
WHERE favorite != FALSE 
ORDER BY fullname DESC 
LIMIT 10
OFFSET 1;

SELECT name, age, email 
FROM users u 
WHERE age IN (20, 30, 40, 50, 60);

SELECT name, age, email 
FROM users u 
WHERE age NOT BETWEEN 24 AND 40;

SELECT name, age, email 
FROM users u 
WHERE age >= 24 AND age <= 40;

SELECT name, age, email 
FROM users u 
WHERE age >= 40 OR age <= 23;

SELECT c.name, c.phone 
FROM contacts c 
WHERE name LIKE "%le%";

SELECT ROUND(AVG(age), 2) "average_age"
FROM users u ;

SELECT COUNT(user_id) total, user_id 
FROM contacts c 
GROUP BY user_id ;

SELECT *
FROM contacts c 
WHERE user_id IN (
	SELECT id 
	FROM users u 
	WHERE age <= 35
);

SELECT c.name, c.phone , u.name username
FROM contacts c 
JOIN users u ON u.id = c.user_id 
WHERE u.age <= 35;

SELECT c.name, c.phone , u.name username
FROM contacts c 
JOIN users u ON u.id = c.user_id;

SELECT c.name, c.phone , u.name username
FROM contacts c 
LEFT JOIN users u ON u.id = c.user_id;

SELECT c.name, c.phone , u.name username
FROM users u 
LEFT JOIN contacts c ON u.id = c.user_id;

UPDATE contacts SET user_id = 3 WHERE id = 5;