USE cadastro;

INSERT INTO cursos (
    nome, descricao, carga, totaulas, ano
) VALUES
('HTML', 'Curso de HTML', '40', '37', '2014'),
('Algoritmos', 'Logica de Programação', '20', '15', '2014'),
('Photoshop', 'Dicad de  Photoshop CC', '10', '8', '2014'),
('PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('Word', 'Curso completo de Word', '40', '30', '2016'),
('Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('Youtube', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = 1
LIMIT 1;

DELETE FROM cursos
WHERE ano = 2018
LIMIT 3;

TRUNCATE TABLE cursos;

SELECT * FROM cursos;