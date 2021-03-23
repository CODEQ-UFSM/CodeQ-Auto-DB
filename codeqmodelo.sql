-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 23-Mar-2021 às 01:31
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `codeqteste`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `aula`
--

CREATE TABLE `aula` (
  `id_aula` int(15) UNSIGNED NOT NULL,
  `nome` varchar(200) DEFAULT NULL,
  `num_ordem` int(11) NOT NULL,
  `descricao` text DEFAULT NULL,
  `data` date DEFAULT NULL,
  `imagem` text DEFAULT NULL,
  `id_secao` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pagina`
--

CREATE TABLE `pagina` (
  `id_pagina` int(15) UNSIGNED NOT NULL,
  `num_ordem` int(11) DEFAULT NULL,
  `html` longtext DEFAULT NULL,
  `id_aula` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `secao`
--

CREATE TABLE `secao` (
  `id_secao` int(15) UNSIGNED NOT NULL,
  `id_trilha` int(10) UNSIGNED DEFAULT NULL,
  `nome` varchar(200) DEFAULT NULL,
  `descricao` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `trilha`
--

CREATE TABLE `trilha` (
  `id_trilha` int(15) UNSIGNED NOT NULL,
  `nome` varchar(200) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `frase` text DEFAULT NULL,
  `autor` varchar(200) DEFAULT NULL,
  `imagem` text DEFAULT NULL,
  `cor` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `trilha`
--

INSERT INTO `trilha` (`id_trilha`, `nome`, `descricao`, `frase`, `autor`, `imagem`, `cor`) VALUES
(1, 'Pensamento Lógico', NULL, '“We can only see a short distance ahead, but we can see plenty there that needs to be done.”', 'Alan Turing', 'https://i.ibb.co/NC5j5LJ/andy-makely-0cn3wuj6-Cmw-unsplash.jpg', '16,188,249'),
(2, 'Matemática', NULL, '“The mathematician does not study pure mathematics because it is useful, he studies it because he delights in it and he delights in it because it is beautiful.”', 'Henri Poincaré', 'https://media.wnyc.org/i/800/0/l/85/1/shutterstock_math.jpg', '11,232,129'),
(3, 'Física', NULL, 'Trilha em desenvolvimento', 'Equipe CodeQ', 'https://img.freepik.com/fotos-gratis/berco-do-pendulo-de-newton-em-um-fundo-preto_103577-5224.jpg?size=626&ext=jpg', '255,63,52'),
(4, 'Estatística', NULL, 'Trilha em desenvolvimento', 'Equipe CodeQ', 'https://www.wallpapers4u.org/wp-content/uploads/cards_chips_poker_table_black_white_7909_1920x1080.jpg', '247, 183, 49'),
(5, 'Engenharia Química', NULL, 'Trilha em desenvolvimento', 'Equipe CodeQ', 'https://www.digglescreative.com/images/blog/photography-for-industrial-companies/intro-4-types-of-industrial-photogrpahy.jpg', '136,84,208');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `aula`
--
ALTER TABLE `aula`
  ADD PRIMARY KEY (`id_aula`),
  ADD KEY `id_secao` (`id_secao`);

--
-- Índices para tabela `pagina`
--
ALTER TABLE `pagina`
  ADD PRIMARY KEY (`id_pagina`);

--
-- Índices para tabela `secao`
--
ALTER TABLE `secao`
  ADD PRIMARY KEY (`id_secao`),
  ADD KEY `id_trilha` (`id_trilha`);

--
-- Índices para tabela `trilha`
--
ALTER TABLE `trilha`
  ADD PRIMARY KEY (`id_trilha`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `aula`
--
ALTER TABLE `aula`
  MODIFY `id_aula` int(15) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pagina`
--
ALTER TABLE `pagina`
  MODIFY `id_pagina` int(15) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `secao`
--
ALTER TABLE `secao`
  MODIFY `id_secao` int(15) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `trilha`
--
ALTER TABLE `trilha`
  MODIFY `id_trilha` int(15) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `aula`
--
ALTER TABLE `aula`
  ADD CONSTRAINT `aula_ibfk_1` FOREIGN KEY (`id_secao`) REFERENCES `secao` (`id_secao`);

--
-- Limitadores para a tabela `secao`
--
ALTER TABLE `secao`
  ADD CONSTRAINT `secao_ibfk_1` FOREIGN KEY (`id_trilha`) REFERENCES `trilha` (`id_trilha`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
