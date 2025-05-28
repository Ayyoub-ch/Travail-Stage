-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 28 mai 2025 à 08:42
-- Version du serveur : 9.1.0
-- Version de PHP : 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `matrice`
--

-- --------------------------------------------------------

--
-- Structure de la table `hard`
--

DROP TABLE IF EXISTS `hard`;
CREATE TABLE IF NOT EXISTS `hard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `competence1` varchar(50) NOT NULL,
  `categorie` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8814 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `niveau_hard`
--

DROP TABLE IF EXISTS `niveau_hard`;
CREATE TABLE IF NOT EXISTS `niveau_hard` (
  `id_personne` int NOT NULL,
  `id_hard` int NOT NULL,
  `niveau` int NOT NULL,
  KEY `fk_hard` (`id_hard`),
  KEY `id_personne` (`id_personne`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `niveau_soft`
--

DROP TABLE IF EXISTS `niveau_soft`;
CREATE TABLE IF NOT EXISTS `niveau_soft` (
  `id_personne` int NOT NULL,
  `id_soft` int NOT NULL,
  `niveau` varchar(50) NOT NULL,
  KEY `id_soft` (`id_soft`),
  KEY `id_personne` (`id_personne`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

DROP TABLE IF EXISTS `personne`;
CREATE TABLE IF NOT EXISTS `personne` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(12) NOT NULL,
  `prenom` varchar(12) NOT NULL,
  `poste` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id`, `nom`, `prenom`, `poste`) VALUES
(136, 'Morigny', 'Nicolas', 'Chef de projet');

-- --------------------------------------------------------

--
-- Structure de la table `soft`
--

DROP TABLE IF EXISTS `soft`;
CREATE TABLE IF NOT EXISTS `soft` (
  `id` int NOT NULL AUTO_INCREMENT,
  `competence2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=312 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `soft`
--

INSERT INTO `soft` (`id`, `competence2`) VALUES
(311, 'Autonomie');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
