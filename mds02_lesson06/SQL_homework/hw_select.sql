-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT 
    s.id, 
    s.fullname, 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;

-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT 
    s.id,
    s.fullname,
    ROUND(AVG(g.grade)) as average_grade
FROM grades g
JOIN students s  ON s.id = g.student_id
WHERE g.subject_id = 1  -- Предмет, з якого ви хочете знайти середній бал
GROUP BY s.id
order by average_grade desc 
limit 1;


