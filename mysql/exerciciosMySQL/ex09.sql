-- "Quantos gafanhotos mulheres têm mais de 1.90m de altura?"

SELECT COUNT(*) FROM gafanhotos
WHERE sexo = 'f' AND altura > 1.90;
