CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE utf8_general_ci;

USE cadastro;

CREATE TABLE pessoas(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    nascimento DATE,
    sexo ENUM('M', 'F'),
    peso DECIMAL(5,2),
    altura DECIMAL(3, 2),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

INSERT INTO pessoas(
    id, nome, nascimento, sexo, peso, altura, nacionalidade
) VALUES
(DEFAULT, 'Ana', '2010-3-10', 'F', '65.5', '1.65', 'EUA'),
(DEFAULT, 'Cláudio', '1975-4-22', 'M', '99.0', '2.15', DEFAULT),
(DEFAULT, 'Janaina', '1967-12-07', 'F', '75.4', '1.66', 'Mexico');

ALTER TABLE pessoas
RENAME TO peoples;

DESC pessoas;
