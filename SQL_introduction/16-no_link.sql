-- 16-no_null.sql
-- Lists all records with a name, showing score and name, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
