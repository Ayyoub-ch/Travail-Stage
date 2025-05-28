-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 28 mai 2025 à 07:48
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
) ENGINE=MyISAM AUTO_INCREMENT=8100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `hard`
--

INSERT INTO `hard` (`id`, `competence1`, `categorie`) VALUES
(7981, 'Agiles', 'Méthodologie / Gestion de projet'),
(7982, 'AJAX', 'Frameworks / Bibliothèques'),
(7983, 'Algorithmie et structures de données', 'Structures & Concepts'),
(7984, 'Anglais', 'Langue'),
(7985, 'Angular', 'Frameworks / Bibliothèques'),
(7986, 'Apache Spark', 'Outils / Logiciels'),
(7987, 'API', 'Interfaces / API'),
(7988, 'asana', 'Outils / Logiciels'),
(7989, 'ASP', 'Frameworks / Bibliothèques'),
(7990, 'AWS', 'Cloud / Infrastructures'),
(7991, 'Azure', 'Cloud / Infrastructures'),
(7992, 'BPMN', 'Méthodologie / Gestion de projet'),
(7993, 'C#', 'Langages de programmation'),
(7994, 'C++', 'Langages de programmation'),
(7995, 'conception/modélisation UML', 'Structures & Concepts'),
(7996, 'Confluence', 'Outils / Logiciels'),
(7997, 'CRM', 'Méthodologie / Gestion de projet'),
(7998, 'CSS', 'Langages de programmation'),
(7999, 'DAX / MDX', 'Bases de données / SGBD'),
(8000, 'Dell Boomi', 'Outils / Logiciels'),
(8001, 'DEVBOOSTER', 'Frameworks / Bibliothèques'),
(8002, 'DevOps', 'Outils DevOps / CI-CD'),
(8003, 'Django', 'Frameworks / Bibliothèques'),
(8004, 'Docker', 'Outils DevOps / CI-CD'),
(8005, 'Eclipse', 'Outils / Logiciels'),
(8006, 'ENTITY', 'Frameworks / Bibliothèques'),
(8007, 'Erwin Data Modeler', 'Outils / Logiciels'),
(8008, 'Flask', 'Frameworks / Bibliothèques'),
(8009, 'front-end / back-end', 'Structures & Concepts'),
(8010, 'GanttProject', 'Outils / Logiciels'),
(8011, 'Gestion de la performance KPI', 'Structures & Concepts'),
(8012, 'GitHub / GitLab', 'Outils DevOps / CI-CD'),
(8013, 'Google Cloud', 'Cloud / Infrastructures'),
(8014, 'GSP', 'Autres'),
(8015, 'hadoop', 'Outils / Logiciels'),
(8016, 'Hibernate', 'Frameworks / Bibliothèques'),
(8017, 'HP ALM', 'Outils / Logiciels'),
(8018, 'HP QC', 'Outils / Logiciels'),
(8019, 'HTML', 'Langages de programmation'),
(8020, 'IBM Cognos', 'Outils / Logiciels'),
(8021, 'IBM Infosphere MDM', 'Outils / Logiciels'),
(8022, 'Informatica MDM', 'Outils / Logiciels'),
(8023, 'Informatica PowerCenter', 'Outils / Logiciels'),
(8024, 'IntelliJ IDEA', 'Outils / Logiciels'),
(8025, 'Java', 'Langages de programmation'),
(8026, 'Java EE', 'Frameworks / Bibliothèques'),
(8027, 'JavaScript', 'Langages de programmation'),
(8028, 'JDBC', 'Interfaces / API'),
(8029, 'Jenkins', 'Outils DevOps / CI-CD'),
(8030, 'Jira', 'Outils / Logiciels'),
(8031, 'JQUERY', 'Frameworks / Bibliothèques'),
(8032, 'JSON', 'Interfaces / API'),
(8033, 'JUnit', 'Tests / Qualité'),
(8034, 'Kubernetes', 'Outils DevOps / CI-CD'),
(8035, 'LINQ', 'Frameworks / Bibliothèques'),
(8036, 'maven / gradle', 'Outils DevOps / CI-CD'),
(8037, 'Méthodologie Agile', 'Méthodologie / Gestion de projet'),
(8038, 'Méthodologie PMP', 'Méthodologie / Gestion de projet'),
(8039, 'Méthodologie Scrum', 'Méthodologie / Gestion de projet'),
(8040, 'Méthodologie Waterfall', 'Méthodologie / Gestion de projet'),
(8041, 'Microsoft Azure, AWS', 'Cloud / Infrastructures'),
(8042, 'Microsoft Dynamics 365', 'Cloud / Infrastructures'),
(8043, 'Microsoft SQL Server Analysis Services (SSAS)', 'Bases de données / SGBD'),
(8044, 'Microsoft SQL Server Integration Services (SSIS)', 'Bases de données / SGBD'),
(8045, 'Microsoft Teams', 'Outils / Logiciels'),
(8046, 'Microsoft Visio', 'Outils / Logiciels'),
(8047, 'Miro', 'Outils / Logiciels'),
(8048, 'MongoDB', 'Bases de données / SGBD'),
(8049, 'MS Project', 'Outils / Logiciels'),
(8050, 'MuleSoft', 'Outils / Logiciels'),
(8051, 'MVC 5', 'Frameworks / Bibliothèques'),
(8052, 'MySQL', 'Bases de données / SGBD'),
(8053, 'NET', 'Langages de programmation'),
(8054, 'NOSQL', 'Bases de données / SGBD'),
(8055, 'ODI', 'Bases de données / SGBD'),
(8056, 'Oracle', 'Bases de données / SGBD'),
(8057, 'Oracle BI', 'Business Intelligence / Data Viz / Analytics'),
(8058, 'Oracle ERP', 'Cloud / Infrastructures'),
(8059, 'Oracle MDM', 'Outils / Logiciels'),
(8060, 'ORM', 'Frameworks / Bibliothèques'),
(8061, 'Pandas / NumPy', 'Frameworks / Bibliothèques'),
(8062, 'PMP', 'Méthodologie / Gestion de projet'),
(8063, 'PostgreSQL', 'Bases de données / SGBD'),
(8064, 'Postman', 'Outils / Logiciels'),
(8065, 'Power BI', 'Business Intelligence / Data Viz / Analytics'),
(8066, 'Prince 2', 'Méthodologie / Gestion de projet'),
(8067, 'Python', 'Langages de programmation'),
(8068, 'PyTorch', 'IA / Machine Learning'),
(8069, 'QlikView/Qlik Sense', 'Business Intelligence / Data Viz / Analytics'),
(8070, 'React.js', 'Frameworks / Bibliothèques'),
(8071, 'REST, SOAP', 'Interfaces / API'),
(8072, 'SAP', 'Cloud / Infrastructures'),
(8073, 'SAP BusinessObjects', 'Business Intelligence / Data Viz / Analytics'),
(8074, 'SAP, Oracle ERP', 'Cloud / Infrastructures'),
(8075, 'Savoir optimiser le code Python', 'Structures & Concepts'),
(8076, 'scala', 'Langages de programmation'),
(8077, 'Scikit-learn', 'IA / Machine Learning'),
(8078, 'Selenium', 'Tests / Qualité'),
(8079, 'SHAREPOINT', 'Outils / Logiciels'),
(8080, 'Slack', 'Outils / Logiciels'),
(8081, 'Spring Cloud', 'Frameworks / Bibliothèques'),
(8082, 'Spring Framework', 'Frameworks / Bibliothèques'),
(8083, 'SQL', 'Langages de programmation'),
(8084, 'SQL Server', 'Bases de données / SGBD'),
(8085, 'Sx Sigma', 'Méthodologie / Gestion de projet'),
(8086, 'sybase', 'Bases de données / SGBD'),
(8087, 'Tableau software', 'Business Intelligence / Data Viz / Analytics'),
(8088, 'Talend', 'Outils / Logiciels'),
(8089, 'TensorFlow', 'IA / Machine Learning'),
(8090, 'Tomcat / Jboss', 'Outils / Logiciels'),
(8091, 'Trello', 'Outils / Logiciels'),
(8092, 'UML', 'Structures & Concepts'),
(8093, 'Unit testing', 'Tests / Qualité'),
(8094, 'Visual Studio', 'Outils / Logiciels'),
(8095, 'Visual Studio Code', 'Outils / Logiciels'),
(8096, 'Vue JS', 'Frameworks / Bibliothèques'),
(8097, 'Waterfall', 'Méthodologie / Gestion de projet'),
(8098, 'WPF', 'Frameworks / Bibliothèques'),
(8099, 'Xray', 'Tests / Qualité');

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

--
-- Déchargement des données de la table `niveau_hard`
--

INSERT INTO `niveau_hard` (`id_personne`, `id_hard`, `niveau`) VALUES
(118, 7981, 4),
(118, 7982, 2),
(118, 7983, 4),
(118, 7984, 3),
(118, 7986, 2),
(118, 7987, 4),
(118, 7989, 2),
(118, 7990, 1),
(118, 7993, 4),
(118, 7994, 2),
(118, 7995, 3),
(118, 7996, 3),
(118, 7997, 3),
(118, 7998, 3),
(118, 8001, 3),
(118, 8002, 3),
(118, 8005, 2),
(118, 8006, 2),
(118, 8009, 4),
(118, 8010, 3),
(118, 8011, 3),
(118, 8012, 3),
(118, 8018, 3),
(118, 8019, 4),
(118, 8027, 4),
(118, 8029, 4),
(118, 8030, 4),
(118, 8031, 2),
(118, 8032, 2),
(118, 8035, 3),
(118, 8037, 4),
(118, 8038, 4),
(118, 8039, 4),
(118, 8045, 4),
(118, 8046, 3),
(118, 8049, 4),
(118, 8051, 3),
(118, 8052, 4),
(118, 8053, 4),
(118, 8054, 3),
(118, 8063, 3),
(118, 8079, 2),
(118, 8083, 4),
(118, 8084, 4),
(118, 8092, 4),
(118, 8094, 4),
(118, 8095, 3),
(118, 8096, 3),
(118, 8098, 3),
(118, 8099, 2);

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
) ENGINE=MyISAM AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id`, `nom`, `prenom`, `poste`) VALUES
(118, 'Morigny', 'Nicolas', 'Chef de projet');

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
