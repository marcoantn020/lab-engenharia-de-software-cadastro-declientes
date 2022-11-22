CREATE TABLE IF NOT EXISTS `pessoa` (
  `id` int primary key auto_increment,
  `nome` varchar(40),
  `idade` int(3),
  `sexo` varchar(1),
  `salario` float
);
