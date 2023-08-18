-- list of same score
SELECT score, count(*) as number FROM second_table
GROUP BY score
ORDER BY score DESC;