-- count number of time of occurence of a record in table second_table
SELECT `score`,COUNT(*) AS `value` FROM `second_table` GROUP BY `score` ORDER BY `value` DESC;
