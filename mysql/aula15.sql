USE cadastro;
DESCRIBE gafanhotos;

-- Adicionando uma FOREING KEY na tabela gafanhotos;

ALTER TABLE gafanhotos
ADD COLUMN cursopreferido INT;

ALTER TABLE gafanhotos
ADD FOREIGN KEY (cursopreferido)
REFERENCES cursos(idcurso);

-- Relacionando uma FOREIGN KEY;

UPDATE gafanhotos
SET cursopreferido = '6'
WHERE id = '1';

SELECT nome, cursopreferido FROM gafanhotos;

-- Este comando não vai funcionar, pois, foi criado a ligação e com os dados não serão afetados
DELETE FROM cursos
WHERE idcurso = 6;

-- Usando o "JOIN" para mostrar os nomes dos cursos ao invés de mostrar somento os números

SELECT g.nome, c.nome, c.ano
FROM gafanhotos as g LEFT JOIN cursos as c
ON c.idcurso = g.cursopreferido;

-- OBS.: Sempre que utilizar qualquer "JOIN" tem que usar a clausula "ON" para dar sentido
-- ao join.