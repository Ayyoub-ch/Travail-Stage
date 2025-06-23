-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 23 juin 2025 à 14:52
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
-- Base de données : `cvtech`
--

-- --------------------------------------------------------

--
-- Structure de la table `certifications`
--

DROP TABLE IF EXISTS `certifications`;
CREATE TABLE IF NOT EXISTS `certifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `certification_skills`
--

DROP TABLE IF EXISTS `certification_skills`;
CREATE TABLE IF NOT EXISTS `certification_skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skill` int NOT NULL,
  `id_user_certification` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_skill` (`id_skill`),
  KEY `id_user_certification` (`id_user_certification`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

DROP TABLE IF EXISTS `clients`;
CREATE TABLE IF NOT EXISTS `clients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `experience_skills`
--

DROP TABLE IF EXISTS `experience_skills`;
CREATE TABLE IF NOT EXISTS `experience_skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skill` int NOT NULL,
  `id_user_experience` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_skill` (`id_skill`,`id_user_experience`),
  KEY `id_user_experience` (`id_user_experience`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `formation_skills`
--

DROP TABLE IF EXISTS `formation_skills`;
CREATE TABLE IF NOT EXISTS `formation_skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skill` int NOT NULL,
  `id_user_formation` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_skill` (`id_skill`),
  KEY `id_user_formation` (`id_user_formation`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
CREATE TABLE IF NOT EXISTS `jobs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `languages`
--

DROP TABLE IF EXISTS `languages`;
CREATE TABLE IF NOT EXISTS `languages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `language_levels`
--

DROP TABLE IF EXISTS `language_levels`;
CREATE TABLE IF NOT EXISTS `language_levels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `skills`
--

DROP TABLE IF EXISTS `skills`;
CREATE TABLE IF NOT EXISTS `skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skill_category` int NOT NULL,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`id_skill_category`),
  KEY `id_skill_category` (`id_skill_category`)
) ENGINE=MyISAM AUTO_INCREMENT=320 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `skills`
--

INSERT INTO `skills` (`id`, `id_skill_category`, `name`) VALUES
(98, 6, 'Autonomie'),
(99, 6, 'Capaciter à déléguer'),
(100, 6, 'Communication '),
(101, 6, 'Créatif / innovant'),
(102, 6, 'Enseigner et coacher'),
(103, 6, 'Esprit de logique'),
(104, 6, 'Esprit de synthèse'),
(105, 6, 'Esprit d\'équipe'),
(106, 6, 'Esprit d\'initiative'),
(107, 6, 'Flexibilité et adaptabilité'),
(108, 6, 'Gestion des risques '),
(109, 6, 'Gestion du stress '),
(110, 6, 'Gestion du temps'),
(111, 6, 'Négociation'),
(112, 6, 'Organisation '),
(113, 6, 'Prise de décision'),
(114, 6, 'Relationnel'),
(115, 6, 'Résolution de problèmes '),
(116, 6, 'Rigueur'),
(117, 6, 'Vision stratégique'),
(118, 6, 'Leadership'),
(119, 6, 'Management'),
(120, 6, 'Sens de la confidentialité'),
(121, 6, 'Curiosité intellectuelle'),
(122, 6, 'Pensée critique'),
(123, 6, 'Capacité à recevoir et donner du feedback'),
(124, 6, 'Orientation client'),
(125, 6, 'Gestion du changement'),
(126, 6, 'Prise de parole en public devant un large auditoire'),
(127, 6, 'Influence dans un contexte politique ou organisationnel complexe'),
(128, 6, 'Animation de workshops ou d’ateliers'),
(129, 6, 'Gestion de l’incertitude '),
(130, 6, 'Capacité à tirer des enseignements de l’échec'),
(131, 6, 'Intelligence émotionnelle'),
(132, 6, 'Accompagnement du changement'),
(133, 6, 'Accompagnement des juniors'),
(134, 6, 'Curiosité'),
(135, 6, 'Ecoute active'),
(136, 6, 'Adaptabilité'),
(137, 6, 'Responsabilité'),
(138, 6, 'Confiance en soi'),
(139, 6, 'Développement personnel'),
(140, 6, 'Humilité'),
(141, 6, 'Bienveillance'),
(142, 6, 'Polyvalence'),
(143, 6, 'Résolution de problèmes critique'),
(144, 6, 'Capaciter à apprendre'),
(145, 7, 'MySQL'),
(146, 7, 'NOSQL'),
(147, 7, 'ODI'),
(148, 7, 'Oracle'),
(149, 7, 'PostgreSQL'),
(150, 7, 'sybase'),
(151, 8, 'QlikView/Qlik Sense'),
(152, 8, 'Looker Studio'),
(153, 9, 'Google Cloud'),
(154, 10, 'API'),
(155, 10, 'JSON'),
(156, 10, 'REST, SOAP'),
(157, 11, 'C++'),
(158, 11, 'CSS'),
(159, 11, 'HTML'),
(160, 11, 'JavaScript'),
(161, 11, 'Python'),
(162, 11, 'SQL'),
(163, 12, 'Anglais'),
(164, 13, 'Agiles'),
(165, 13, 'CRM'),
(166, 13, 'Méthodologie Agile'),
(167, 13, 'Méthodologie Scrum'),
(168, 14, 'Confluence'),
(169, 14, 'GanttProject'),
(170, 14, 'hadoop'),
(171, 14, 'Informatica PowerCenter'),
(172, 14, 'Jira'),
(173, 14, 'Microsoft Teams'),
(174, 14, 'Microsoft Visio'),
(175, 14, 'Miro'),
(176, 14, 'SHAREPOINT'),
(177, 14, 'Talend'),
(178, 14, 'Tomcat / Jboss'),
(179, 14, 'Visual Studio'),
(180, 15, 'DevOps'),
(181, 15, 'GitHub / GitLab'),
(182, 15, 'Jenkins'),
(183, 16, 'Algorithmie et structures de données'),
(184, 16, 'conception/modélisation UML'),
(185, 16, 'front-end / back-end'),
(186, 16, 'Gestion de la performance KPI'),
(187, 17, 'Unit testing'),
(188, 7, 'Microsoft SQL Server Analysis Services (SSAS)'),
(189, 7, 'Microsoft SQL Server Integration Services (SSIS)'),
(190, 7, 'SQL Server'),
(191, 8, 'Power BI'),
(192, 9, 'AWS'),
(193, 9, 'Azure'),
(194, 9, 'Microsoft Azure, AWS'),
(195, 9, 'Microsoft Dynamics 365'),
(196, 9, 'SAP'),
(197, 9, 'SAP, Oracle ERP'),
(198, 11, 'C#'),
(199, 11, 'Java'),
(200, 14, 'asana'),
(201, 14, 'IBM Infosphere MDM'),
(202, 14, 'Informatica MDM'),
(203, 14, 'MS Project'),
(204, 14, 'Slack'),
(205, 14, 'Trello'),
(206, 14, 'Visual Studio Code'),
(207, 15, 'Docker'),
(208, 16, 'UML'),
(209, 14, 'Workspace One MDM'),
(210, 14, 'Zero-Touch Customer Portal'),
(211, 14, 'Samsung Knox'),
(212, 14, 'ABM Apple'),
(213, 14, 'Google Workspace'),
(214, 10, 'Google Apps Script'),
(215, 10, 'Google Cloud Console\n'),
(216, 14, 'système d\'exploitation Apple (y compris IOS)'),
(217, 14, 'Système d\'exploitation Windows'),
(218, 14, 'Système d\'exploitation Google'),
(219, 14, 'Système d\'exploitation Linux'),
(220, 18, 'Intelligence artificielle'),
(221, 19, 'Angular'),
(222, 19, 'Java EE'),
(223, 14, 'Eclipse'),
(224, 14, 'Postman'),
(225, 17, 'Xray'),
(226, 7, 'MongoDB'),
(227, 8, 'SAP BusinessObjects'),
(228, 8, 'Tableau software'),
(229, 9, 'Oracle ERP'),
(230, 19, 'React.js'),
(231, 19, 'Spring Cloud'),
(232, 19, 'Spring Framework'),
(233, 19, 'Vue JS'),
(234, 10, 'JDBC'),
(235, 14, 'IBM Cognos'),
(236, 14, 'IntelliJ IDEA'),
(237, 15, 'maven / gradle'),
(238, 8, 'Oracle BI'),
(239, 19, 'JQUERY'),
(240, 19, 'Terraform'),
(241, 19, 'ASP'),
(242, 11, 'NET'),
(243, 14, 'Informatica  Powerexchange'),
(244, 14, 'HP ALM'),
(245, 14, 'HP QC'),
(246, 15, 'Kubernetes'),
(247, 17, 'JUnit'),
(248, 17, 'Selenium'),
(249, 20, '$Universe'),
(250, 20, 'Unix'),
(251, 7, 'Teradata'),
(252, 9, 'Snowflake'),
(253, 19, 'Pandas / NumPy'),
(254, 18, 'PyTorch'),
(255, 18, 'Scikit-learn'),
(256, 18, 'TensorFlow'),
(257, 21, 'ETL/ELT'),
(258, 21, 'Stambia'),
(259, 11, 'R'),
(260, 11, 'VBA'),
(261, 11, 'SAS'),
(262, 13, 'BPMN'),
(263, 13, 'Méthodologie PMP'),
(264, 13, 'Méthodologie Waterfall'),
(265, 13, 'PMP'),
(266, 13, 'Waterfall'),
(267, 11, 'Shell (Mremout,Gitbash...) '),
(268, 9, 'GCP (Bigquery)'),
(269, 19, 'Hibernate'),
(270, 20, 'GSP'),
(271, 7, 'DAX / MDX'),
(272, 11, 'scala'),
(273, 14, 'Apache Spark'),
(274, 16, 'Savoir optimiser le code Python'),
(275, 14, 'Databricks'),
(276, 14, 'Airflow'),
(277, 19, 'Flask'),
(278, 19, 'AJAX'),
(279, 19, 'JSP'),
(280, 19, 'Concept MVC'),
(281, 17, 'Cypress'),
(282, 17, 'Semarchy'),
(283, 12, 'Portugais'),
(284, 21, 'DBT'),
(285, 21, 'SQLMesh'),
(286, 12, 'Espagnol'),
(287, 19, 'Django'),
(288, 13, 'Sx Sigma'),
(289, 11, 'Perl'),
(290, 9, 'c'),
(291, 19, 'Arduino'),
(292, 7, 'Redis'),
(293, 14, 'Git'),
(294, 11, 'PHP'),
(295, 19, 'SqlAlchemy'),
(296, 7, 'SqLite'),
(297, 11, 'Golang'),
(298, 20, 'NGINX'),
(299, 20, 'Administration Système GNU/Linux'),
(300, 19, 'Android'),
(301, 11, 'Kotlin'),
(302, 19, 'beautifulsoup4'),
(303, 14, 'MuleSoft'),
(304, 21, 'Semarchy xDi'),
(305, 14, 'Semarche xDm'),
(306, 14, 'DataGalaxy'),
(307, 19, 'MVC 5'),
(308, 19, 'ORM'),
(309, 19, 'WPF'),
(310, 17, 'Data Quality'),
(311, 14, 'Kestra'),
(312, 19, 'Typescript'),
(313, 14, 'Google site'),
(314, 19, 'ENTITY'),
(315, 19, 'LINQ'),
(316, 22, 'BigQuery'),
(317, 11, 'Windev'),
(318, 14, 'STEP MDM'),
(319, 19, 'DEVBOOSTER');

-- --------------------------------------------------------

--
-- Structure de la table `skill_categories`
--

DROP TABLE IF EXISTS `skill_categories`;
CREATE TABLE IF NOT EXISTS `skill_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(191) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `skill_categories`
--

INSERT INTO `skill_categories` (`id`, `name`) VALUES
(6, 'Soft Skills'),
(7, 'Bases de données / SGBD'),
(8, 'Business Intelligence / Data Viz / Analytics'),
(9, 'Cloud / Infrastructures'),
(10, 'Interfaces / API'),
(11, 'Langages de programmation'),
(12, 'Langue'),
(13, 'Méthodologie / Gestion de projet'),
(14, 'Outils / Logiciels'),
(15, 'Outils DevOps / CI-CD'),
(16, 'Structures & Concepts'),
(17, 'Tests / Qualité'),
(18, 'IA / Machine Learning'),
(19, 'Frameworks / Bibliothèques'),
(20, 'Autres'),
(21, 'Intégration / ETL'),
(22, 'Big Data / Traitement distribué');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_job` int DEFAULT NULL,
  `last_name` varchar(191) NOT NULL,
  `first_name` varchar(191) NOT NULL,
  `mail` varchar(191) NOT NULL,
  `password` varchar(191) NOT NULL,
  `roles` varchar(191) NOT NULL,
  `on_mission` int DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`mail`),
  KEY `id_job` (`id_job`)
) ENGINE=MyISAM AUTO_INCREMENT=1633 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `id_job`, `last_name`, `first_name`, `mail`, `password`, `roles`, `on_mission`, `description`) VALUES
(1589, NULL, 'CABY', 'MAXIME', 'cmaxime@logical-conseils.com', 'logical', 'Consultant data', 0, NULL),
(1590, NULL, 'MOULAY', 'Medhi', 'mmedhi@logical-conseils.com', 'logical', 'Consultant ADMINISTRATEUR SYSTEMES', 0, NULL),
(1591, NULL, 'Benjamin', 'Thomas', 'bthomas@logical-conseils.com', 'logical', 'Business Analyst', 0, NULL),
(1592, NULL, 'TAOUSSI', 'SARA', 'tsara@logical-conseils.com', 'logical', 'DATA ENGINEER', 0, NULL),
(1593, NULL, 'ANDRY', 'ADRIEN', 'aadrien@logical-conseils.com', 'logical', 'Consultant Data Confirme', 0, NULL),
(1594, NULL, 'LEROUX', 'HERVE', 'lherve@logical-conseils.com', 'logical', 'Consultant Data', 0, NULL),
(1595, NULL, 'TRAN-MEYER', 'Quan', 'tquan@logical-conseils.com', 'logical', 'QA Test Analyst', 0, NULL),
(1596, NULL, 'LESOT', 'Jérémy', 'ljérémy@logical-conseils.com', 'logical', 'Data Engineer', 0, NULL),
(1597, NULL, 'Maxime', 'Leroy', 'mleroy@logical-conseils.com', 'logical', 'Consultant d\'application Sénior', 0, NULL),
(1598, NULL, 'Boussouf', 'Madani', 'bmadani@logical-conseils.com', 'logical', 'data analyste', 0, NULL),
(1599, NULL, 'Ali ABDOULKA', 'ALI', 'aali@logical-conseils.com', 'logical', 'Consultant Data', 0, NULL),
(1600, NULL, 'AMRAOUI', 'Youssef', 'ayoussef@logical-conseils.com', 'logical', 'Développeur Informatique', 0, NULL),
(1601, NULL, 'TARAHOU', 'Ismail', 'tismail@logical-conseils.com', 'logical', 'Data Analyst', 0, NULL),
(1602, NULL, 'NOUMSSI', 'Joseph', 'njoseph@logical-conseils.com', 'logical', 'Consultant Technico-fonctionnel Data', 0, NULL),
(1603, NULL, 'Ly TRAN-MEYE', 'Kim', 'lkim@logical-conseils.com', 'logical', 'Développeuse BI', 0, NULL),
(1604, NULL, 'WARLOP', 'Tristan', 'wtristan@logical-conseils.com', 'logical', 'Software Engineer', 0, NULL),
(1605, NULL, 'Matallah', 'Mouadh', 'mmouadh@logical-conseils.com', 'logical', 'Data engineer', 0, NULL),
(1606, NULL, 'Appéré', 'Loïck', 'aloïck@logical-conseils.com', 'logical', 'Ingénieur fullstack devOps', 0, NULL),
(1607, NULL, 'Madache', 'Zineddine', 'mzineddine@logical-conseils.com', 'logical', 'Consultant data', 0, NULL),
(1608, NULL, 'DE SOUZA', 'Jardel', 'djardel@logical-conseils.com', 'logical', 'Consultant Data', 0, NULL),
(1609, NULL, 'Lecocq', 'Johann', 'ljohann@logical-conseils.com', 'logical', 'Developpeur', 0, NULL),
(1610, NULL, 'Mauchaussée', 'Pauline', 'mpauline@logical-conseils.com', 'logical', 'Data engineer', 0, NULL),
(1611, NULL, 'Amrane', 'Yanis', 'ayanis@logical-conseils.com', 'logical', 'Data Analyst', 0, NULL),
(1612, NULL, 'GUIDONI', 'Elodie', 'gelodie@logical-conseils.com', 'logical', 'Consultante MDM', 0, NULL),
(1613, NULL, 'Bourrel', 'William', 'bwilliam@logical-conseils.com', 'logical', 'Data Engineer / Analytics Engineer', 0, NULL),
(1614, NULL, 'Mara', 'Kabalo', 'mkabalo@logical-conseils.com', 'logical', 'Data ingénieur', 0, NULL),
(1615, NULL, 'Ridha', 'JADLA', 'rjadla@logical-conseils.com', 'logical', 'Consultant applicatif Senior', 0, NULL),
(1616, NULL, 'BOVE', 'Sylvain', 'bsylvain@logical-conseils.com', 'logical', 'Business Analyst Run N3', 0, NULL),
(1617, NULL, 'ABDELLATIF', 'Aya', 'aaya@logical-conseils.com', 'logical', 'data engineer', 0, NULL),
(1618, NULL, 'AMRANE', 'Karim', 'akarim@logical-conseils.com', 'logical', 'Consultant BI - Developpeur BI', 0, NULL),
(1619, NULL, 'BKHAIRI', 'Imen', 'bimen@logical-conseils.com', 'logical', 'Consultante Data', 0, NULL),
(1620, NULL, 'Steve', 'Caron', 'scaron@logical-conseils.com', 'logical', 'Data engineer / Data analyst', 0, NULL),
(1621, NULL, 'Becquart', 'Guillaume', 'bguillaume@logical-conseils.com', 'logical', 'Chef de projet', 0, NULL),
(1622, NULL, 'TARAHOU', 'Bilel', 'tbilel@logical-conseils.com', 'logical', 'Consultant Data', 0, NULL),
(1623, NULL, 'BOUHADOUN', 'Mammar', 'bmammar@logical-conseils.com', 'logical', 'Développeur Full Stack', 0, NULL),
(1624, NULL, 'Buchet', 'Florent', 'bflorent@logical-conseils.com', 'logical', 'Lead Data Engineer', 0, NULL),
(1625, NULL, 'Darghane', 'Haïfa', 'dhaïfa@logical-conseils.com', 'logical', 'chef de projet', 0, NULL),
(1626, NULL, 'JAMALI', 'Mohamed', 'jmohamed@logical-conseils.com', 'logical', 'Data Engineer', 0, NULL),
(1627, NULL, 'EL-HAYEK', 'Nicolas', 'enicolas@logical-conseils.com', 'logical', 'DATA ENGINEER', 0, NULL),
(1628, NULL, 'BESSAHA', 'Nassim', 'bnassim@logical-conseils.com', 'logical', 'Consultant Data', 0, NULL),
(1629, NULL, 'BOULAHYA', 'Younes', 'byounes@logical-conseils.com', 'logical', 'DATA ENGINEER', 0, NULL),
(1630, NULL, 'Franck', 'Alison', 'falison@logical-conseils.com', 'logical', 'Développeuse Windev', 0, NULL),
(1631, NULL, 'JONGMANEE', 'Patrick', 'jpatrick@logical-conseils.com', 'logical', 'Consultant PIM MDM', 0, NULL),
(1632, NULL, 'Morigny', 'Nicolas', 'mnicolas@logical-conseils.com', 'logical', 'Chef de projet', 0, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `user_certifications`
--

DROP TABLE IF EXISTS `user_certifications`;
CREATE TABLE IF NOT EXISTS `user_certifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_certification` int NOT NULL,
  `id_user` int NOT NULL,
  `year` int NOT NULL,
  `validation_duration` int NOT NULL,
  `description` text,
  `serial_certification` varchar(191) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_certification` (`id_certification`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_diplomas`
--

DROP TABLE IF EXISTS `user_diplomas`;
CREATE TABLE IF NOT EXISTS `user_diplomas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `name` varchar(191) NOT NULL,
  `year` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_experiences`
--

DROP TABLE IF EXISTS `user_experiences`;
CREATE TABLE IF NOT EXISTS `user_experiences` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_client` int NOT NULL,
  `id_job` int NOT NULL,
  `id_user` int NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `description` text,
  `brief_description` text,
  `keyword` text,
  PRIMARY KEY (`id`),
  KEY `id_client` (`id_client`),
  KEY `id_job` (`id_job`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_formations`
--

DROP TABLE IF EXISTS `user_formations`;
CREATE TABLE IF NOT EXISTS `user_formations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `name` varchar(191) NOT NULL,
  `year` int NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_languages`
--

DROP TABLE IF EXISTS `user_languages`;
CREATE TABLE IF NOT EXISTS `user_languages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_language_level` int NOT NULL,
  `id_language` int NOT NULL,
  `id_user` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_language` (`id_language`,`id_user`),
  KEY `id_language_level` (`id_language_level`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `user_skills`
--

DROP TABLE IF EXISTS `user_skills`;
CREATE TABLE IF NOT EXISTS `user_skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skill` int NOT NULL,
  `id_user` int NOT NULL,
  `level` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_skill` (`id_skill`,`id_user`),
  KEY `id_user` (`id_user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
