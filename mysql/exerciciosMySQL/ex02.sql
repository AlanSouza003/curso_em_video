-- "Uma lista com os dados de todos aqueles que nasceram entre 1/jan/2000 e 31/dez/2015"

SELECT * FROM gafanhotos
WHERE nascimento BETWEEN '2000-01-01' AND '2015-12-31';
