-- "Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando o pais de origem
-- é o total de pessoas nascidas lá. Só nos interessa os países que tiverem mais 3
-- gafanhotos com essa nacionalidade."

SELECT nacionalidade, COUNT(*) FROM gafanhotos
WHERE nacionalidade NOT IN ('Brasil')
GROUP BY nacionalidade
HAVING COUNT(*) > 3;