USE cadastro;
CREATE Table assiste (
    id INT AUTO_INCREMENT,
    data date,
    idgafanhoto INT,
    idcurso INT,
    PRIMARY KEY (id),
    FOREIGN KEY (idgafanhoto) REFERENCES gafanhotos(id),
    FOREIGN KEY (idcurso) REFERENCES cursos(idcurso)
);

INSERT INTO  assiste VALUES
(default, '2014-03-01', 1, 2),
(default, '2015-12-22', 3, 6),
(default, '2014-01-01', 22, 12),
(default, '2016-05-12', 1, 19);

SELECT g.nome as aluno, c.nome as assistindo FROM gafanhotos AS g JOIN assiste AS a
ON g.id = a.idgafanhoto
JOIN cursos as c
ON a.idcurso = c.idcurso;
