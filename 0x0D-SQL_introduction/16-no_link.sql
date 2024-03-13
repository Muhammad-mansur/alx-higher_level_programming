--  lists all records of the table second_table but no rows without a name value
SELECT score, name FROM second_table WHERE NOT name = NULL OR NOT name = '' ORDER BY score DESC;