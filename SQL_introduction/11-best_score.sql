-- 11-best_score.sql
-- Lists all records with score >= 10, displaying score and name, ordered by score descending

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
