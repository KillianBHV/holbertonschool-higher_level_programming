-- GET NUMBER OF SCORES
SELECT DISTINCT score, COUNT(score) AS number FROM second_table ORDER BY score DESC;
