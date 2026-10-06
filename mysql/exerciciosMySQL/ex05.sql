'''
"Uma lista com o nome e nacionalidade de todos os homens que têm Silva no nome,
não nasceram no Brasil e pesam menos de 100kg"
'''

SELECT nome, nacionalidade FROM gafanhotos
WHERE nome LIKE '%_Silva%' AND sexo = 'M' 
    AND not nacionalidade = 'Brasil' AND peso < 100;