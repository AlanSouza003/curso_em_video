-- "Uma lista com as profissões dos garfanhotos e seus respectivos quantitativos."

SELECT profissao, COUNT(*) AS quantidade FROM gafanhotos
GROUP BY profissao;