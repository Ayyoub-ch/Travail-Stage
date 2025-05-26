-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 26 mai 2025 à 14:30
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
) ENGINE=MyISAM AUTO_INCREMENT=2021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `hard`
--

INSERT INTO `hard` (`id`, `competence1`, `categorie`) VALUES
(1902, '0', 'Méthodologie / Gestion de projet'),
(1903, '0', 'Frameworks / Bibliothèques'),
(1904, '0', 'Structures & Concepts'),
(1905, '0', 'Langue'),
(1906, '0', 'Frameworks / Bibliothèques'),
(1907, '0', 'Outils / Logiciels'),
(1908, '0', 'Interfaces / API'),
(1909, '0', 'Outils / Logiciels'),
(1910, '0', 'Frameworks / Bibliothèques'),
(1911, '0', 'Cloud / Infrastructures'),
(1912, '0', 'Cloud / Infrastructures'),
(1913, '0', 'Méthodologie / Gestion de projet'),
(1914, '0', 'Langages de programmation'),
(1915, '0', 'Langages de programmation'),
(1916, '0', 'Structures & Concepts'),
(1917, '0', 'Outils / Logiciels'),
(1918, '0', 'Méthodologie / Gestion de projet'),
(1919, '0', 'Langages de programmation'),
(1920, '0', 'Bases de données / SGBD'),
(1921, '0', 'Outils / Logiciels'),
(1922, '0', 'Frameworks / Bibliothèques'),
(1923, '0', 'Outils DevOps / CI-CD'),
(1924, '0', 'Frameworks / Bibliothèques'),
(1925, '0', 'Outils DevOps / CI-CD'),
(1926, '0', 'Outils / Logiciels'),
(1927, '0', 'Frameworks / Bibliothèques'),
(1928, '0', 'Outils / Logiciels'),
(1929, '0', 'Frameworks / Bibliothèques'),
(1930, '0', 'Structures & Concepts'),
(1931, '0', 'Outils / Logiciels'),
(1932, '0', 'Structures & Concepts'),
(1933, '0', 'Outils DevOps / CI-CD'),
(1934, '0', 'Cloud / Infrastructures'),
(1935, '0', 'Autres'),
(1936, '0', 'Outils / Logiciels'),
(1937, '0', 'Frameworks / Bibliothèques'),
(1938, '0', 'Outils / Logiciels'),
(1939, '0', 'Outils / Logiciels'),
(1940, '0', 'Langages de programmation'),
(1941, '0', 'Outils / Logiciels'),
(1942, '0', 'Outils / Logiciels'),
(1943, '0', 'Outils / Logiciels'),
(1944, '0', 'Outils / Logiciels'),
(1945, '0', 'Outils / Logiciels'),
(1946, '0', 'Langages de programmation'),
(1947, '0', 'Frameworks / Bibliothèques'),
(1948, '0', 'Langages de programmation'),
(1949, '0', 'Interfaces / API'),
(1950, '0', 'Outils DevOps / CI-CD'),
(1951, '0', 'Outils / Logiciels'),
(1952, '0', 'Frameworks / Bibliothèques'),
(1953, '0', 'Interfaces / API'),
(1954, '0', 'Tests / Qualité'),
(1955, '0', 'Outils DevOps / CI-CD'),
(1956, '0', 'Frameworks / Bibliothèques'),
(1957, '0', 'Outils DevOps / CI-CD'),
(1958, '0', 'Méthodologie / Gestion de projet'),
(1959, '0', 'Méthodologie / Gestion de projet'),
(1960, '0', 'Méthodologie / Gestion de projet'),
(1961, '0', 'Méthodologie / Gestion de projet'),
(1962, '0', 'Cloud / Infrastructures'),
(1963, '0', 'Cloud / Infrastructures'),
(1964, '0', 'Bases de données / SGBD'),
(1965, '0', 'Bases de données / SGBD'),
(1966, '0', 'Outils / Logiciels'),
(1967, '0', 'Outils / Logiciels'),
(1968, '0', 'Outils / Logiciels'),
(1969, '0', 'Bases de données / SGBD'),
(1970, '0', 'Outils / Logiciels'),
(1971, '0', 'Outils / Logiciels'),
(1972, '0', 'Frameworks / Bibliothèques'),
(1973, '0', 'Bases de données / SGBD'),
(1974, '0', 'Langages de programmation'),
(1975, '0', 'Bases de données / SGBD'),
(1976, '0', 'Bases de données / SGBD'),
(1977, '0', 'Bases de données / SGBD'),
(1978, '0', 'Business Intelligence / Data Viz / Analytics'),
(1979, '0', 'Cloud / Infrastructures'),
(1980, '0', 'Outils / Logiciels'),
(1981, '0', 'Frameworks / Bibliothèques'),
(1982, '0', 'Frameworks / Bibliothèques'),
(1983, '0', 'Méthodologie / Gestion de projet'),
(1984, '0', 'Bases de données / SGBD'),
(1985, '0', 'Outils / Logiciels'),
(1986, '0', 'Business Intelligence / Data Viz / Analytics'),
(1987, '0', 'Méthodologie / Gestion de projet'),
(1988, '0', 'Langages de programmation'),
(1989, '0', 'IA / Machine Learning'),
(1990, '0', 'Business Intelligence / Data Viz / Analytics'),
(1991, '0', 'Frameworks / Bibliothèques'),
(1992, '0', 'Interfaces / API'),
(1993, '0', 'Cloud / Infrastructures'),
(1994, '0', 'Business Intelligence / Data Viz / Analytics'),
(1995, '0', 'Cloud / Infrastructures'),
(1996, '0', 'Structures & Concepts'),
(1997, '0', 'Langages de programmation'),
(1998, '0', 'IA / Machine Learning'),
(1999, '0', 'Tests / Qualité'),
(2000, '0', 'Outils / Logiciels'),
(2001, '0', 'Outils / Logiciels'),
(2002, '0', 'Frameworks / Bibliothèques'),
(2003, '0', 'Frameworks / Bibliothèques'),
(2004, '0', 'Langages de programmation'),
(2005, '0', 'Bases de données / SGBD'),
(2006, '0', 'Méthodologie / Gestion de projet'),
(2007, '0', 'Bases de données / SGBD'),
(2008, '0', 'Business Intelligence / Data Viz / Analytics'),
(2009, '0', 'Outils / Logiciels'),
(2010, '0', 'IA / Machine Learning'),
(2011, '0', 'Outils / Logiciels'),
(2012, '0', 'Outils / Logiciels'),
(2013, '0', 'Structures & Concepts'),
(2014, '0', 'Tests / Qualité'),
(2015, '0', 'Outils / Logiciels'),
(2016, '0', 'Outils / Logiciels'),
(2017, '0', 'Frameworks / Bibliothèques'),
(2018, '0', 'Méthodologie / Gestion de projet'),
(2019, '0', 'Frameworks / Bibliothèques'),
(2020, '0', 'Tests / Qualité');

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
  `niveau` int NOT NULL,
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
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id`, `nom`, `prenom`, `poste`) VALUES
(54, 'Morigny', 'Nicolas', 'Chef de projet');

-- --------------------------------------------------------

--
-- Structure de la table `soft`
--

DROP TABLE IF EXISTS `soft`;
CREATE TABLE IF NOT EXISTS `soft` (
  `id` int NOT NULL AUTO_INCREMENT,
  `competence2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=289 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
