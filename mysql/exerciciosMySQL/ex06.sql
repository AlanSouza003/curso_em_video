-- Qual é a maior altura entre gafanhotos homens que moram no Brasil?

SELECT MAX(altura) FROM gafanhotos
WHERE sexo = 'M' AND nacionalidade = 'Brasil';