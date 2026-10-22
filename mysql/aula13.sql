USE cadastro;

SELECT carga FROM cursos
GROUP BY carga;

SELECT carga, COUNT(nome) AS quant_carga FROM cursos
GROUP BY carga;

SELECT totaulas, COUNT(*) AS quant_aulas FROM cursos
GROUP BY totaulas
ORDER BY totaulas;

SELECT * FROM cursos
WHERE totaulas = 30;

SELECT carga, COUNT(*) AS quant_carga FROM cursos
GROUP BY carga
HAVING COUNT(ano) > 5;


SELECT carga, COUNT(*) AS acima_da_media FROM cursos
WHERE ano > 2015
GROUP BY carga
HAVING carga > (SELECT AVG(carga) FROM cursos);