-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2025 at 07:48 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recommendationnotetaking`
--

-- --------------------------------------------------------

-- --------------------------------------------------------

--
-- Table structure for table `feedbackrelevance`
--

CREATE TABLE `feedbackrelevance` (
  `feedbackid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `noteid` int(11) NOT NULL,
  `materialTitle` varchar(255) NOT NULL,
  `isRelevant` tinyint(1) NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedbackrelevance`
--

INSERT INTO `feedbackrelevance` (`feedbackid`, `userid`, `noteid`, `materialTitle`, `isRelevant`, `createdAt`) VALUES
(2, 5, 12, 'INDIAN HISTORY ( A Comprehensive Guide for all Competitive Exams )', 0, '2025-01-11 21:08:12'),
(5, 5, 16, 'Web Design with HTML, CSS, JavaScript and Jquery Set', 1, '2025-01-11 22:41:59'),
(6, 5, 16, 'HTML: Web Guide For Absolute HTML Beginners (Web Development - HTML Book 1)', 1, '2025-01-11 22:42:02'),
(7, 5, 12, 'Oswaal CBSE Question Bank Class 12 English, Physics, Chemistry & Biology (Set of 4 Books) (For 2024 Board Exams)', 1, '2025-01-11 22:42:47'),
(13, 5, 10, 'PYTHON FOR DATA ANALYSIS: Master the Basics of Data Analysis in Python Using Numpy & Pandas: Answers all your Questions Step-by-Step (Programming for Beginners: A Friendly Q & A Guide Book 2)', 1, '2025-01-11 22:46:36'),
(14, 5, 18, 'The Great Derangement: Climate Change and the Unthinkable [Paperback] Ghosh, Amitav', 0, '2025-01-11 22:50:35'),
(15, 5, 19, 'Your Pregnancy Nutrition Guide', 0, '2025-01-11 22:51:21'),
(16, 5, 20, 'DATA SCIENCE: 2 Books in 1: Data Analytics, Artificial Intelligence, Machine Learning and Deep Learning', 1, '2025-01-11 22:52:15'),
(17, 5, 17, 'Yoga and Meditation', 1, '2025-01-12 12:36:53'),
(18, 5, 13, '2019 MeSH Highlights', 0, '2025-01-12 12:42:57'),
(19, 5, 13, 'Topic Searching in PubMed: Using the Medical Subject Headings (MeSH)', 1, '2025-01-12 12:43:04'),
(20, 7, 21, 'Principles Of Microeconomics (english, Paperback, H.l. Ahuja)', 1, '2025-01-13 16:07:53'),
(21, 7, 21, 'Microeconomics For Class - 12 - 12103', 1, '2025-01-13 16:07:58'),
(22, 7, 21, 'Behaviour Based Safety Management', 1, '2025-01-13 16:08:01'),
(23, 7, 22, 'SEO 2024: Learn search engine optimization with smart internet marketing strategies', 1, '2025-01-13 16:09:14'),
(24, 7, 22, 'This is Marketing', 1, '2025-01-13 16:09:17'),
(25, 7, 22, 'Digital Marketing', 0, '2025-01-13 16:09:20'),
(26, 7, 23, 'Analysis of Financial Statements Book for Class 12 Part B - CBSE - Examination 2023-2024', 0, '2025-01-13 16:09:55'),
(27, 7, 23, 'Fundamental Analysis for Beginners: Grow Your Investment Portfolio Like A Pro Using Financial Statements and Ratios of Any Business with Zero Investing Experience Required', 0, '2025-01-13 16:10:02'),
(28, 7, 23, 'Financial Statement Analysis Handbook', 1, '2025-01-13 16:10:05'),
(29, 8, 24, 'Java Software Development with Event B: A Practical Guide (Synthesis Lectures on Software Engineering)', 1, '2025-01-13 16:24:00'),
(30, 8, 24, 'Agile Software Development, Principles, Patterns, and Practices (Alan Apt Series)', 1, '2025-01-13 16:24:12'),
(31, 8, 24, 'Software Architecture with C# 10 and .NET 6: Develop software solutions using microservices, DevOps, EF Core, and design patterns for Azure', 0, '2025-01-13 16:24:16'),
(32, 8, 24, 'Object Oriented Programming with C++', 1, '2025-01-13 16:25:20'),
(33, 8, 24, 'Oop With C++(Revised 1St Ed)', 1, '2025-01-13 16:25:24'),
(34, 8, 24, 'Design Patterns: Elements of Reusable Object-Oriented Software', 1, '2025-01-13 16:25:31'),
(35, 8, 24, 'Artificial Intelligence and Software Testing: Building systems you can trust', 1, '2025-01-13 16:26:29'),
(36, 8, 24, 'Lessons Learned in Software Testing: A Context-Driven Approach', 1, '2025-01-13 16:26:35'),
(37, 8, 24, 'Psychological Testing, 7e', 0, '2025-01-13 16:26:37'),
(38, 9, 25, 'Network Security and Cryptography', 1, '2025-01-13 16:33:13'),
(39, 9, 25, 'Introduction to Cyber Security : Guide to the World of Cyber Security', 1, '2025-01-13 16:33:17'),
(40, 9, 25, 'IIBF’s IT Security – Covering all Essentials of IT Security in Banking Institutes such as Overview, Security Controls, Security Threats and IS Audit & Regulatory Compliance', 0, '2025-01-13 16:33:25'),
(41, 9, 25, 'Algorithms', 0, '2025-01-13 16:34:09'),
(42, 9, 25, 'Data Structures and Algorithms Made Easy', 0, '2025-01-13 16:34:20'),
(43, 9, 25, 'Data Structures and Algorithms Using C++', 0, '2025-01-13 16:34:22'),
(44, 9, 25, 'The Antisocial Network', 0, '2025-01-13 16:34:58');

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `noteid` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp(),
  `updatedAt` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `is_archived` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notes`
--

INSERT INTO `notes` (`noteid`, `userid`, `title`, `content`, `createdAt`, `updatedAt`, `is_archived`) VALUES
(10, 5, 'Introduction to Python Programming', '<p><code>This note is a beginner\'s guide to Python programming. It covers data types, control structures, functions, and libraries such as NumPy and pandas for data analysis.</code></p>', '2025-01-10 02:39:07', '2025-01-10 02:39:07', 0),
(11, 5, 'Medical Innovations in Biology', '\r\n                Exploring cutting-edge research in genetics and biotechnology.\r\n            ', '2025-01-10 02:41:06', '2025-01-10 02:41:06', 0),
(12, 5, 'Preparation for Competitive Exams', '\r\n                A comprehensive guide to preparing for biology and chemistry sections of competitive exams\r\n            ', '2025-01-10 02:41:43', '2025-01-10 02:41:43', 0),
(13, 5, '2019 MeSH Highlights', '\r\n                on january 4, 2019, nlm staff provided a highlight of the updates made to the Medical Subject Headings (MeSH) system.\r\n            ', '2025-01-10 02:43:36', '2025-01-10 02:43:36', 0),
(16, 5, 'Introduction to Web Development', '\r\n                Learn the basics of HTML, CSS, and JavaScript to build responsive websites. This course covers foundational web technologies and practical tools used by web developers. Ideal for beginners.\r\n            ', '2025-01-11 22:41:51', '2025-01-11 22:42:12', 0),
(17, 5, 'Benefits of Yoga for Mental Health', '\r\n                Yoga is a practice that combines physical postures, breathing exercises, and meditation to promote mental and physical well-being. Studies have shown that regular yoga practice can reduce stress, anxiety, and depression. It is particularly effective in improving sleep quality and enhancing overall mental resilience.\r\n            ', '2025-01-11 22:49:42', '2025-01-11 22:49:42', 0),
(18, 5, 'Climate Change and Its Global Impact', '\r\n                Climate change refers to long-term alterations in temperature, precipitation, and other atmospheric conditions. It is driven by human activities, such as burning fossil fuels and deforestation, leading to global warming. Effects include rising sea levels, extreme weather events, and loss of biodiversity. Mitigating climate change requires global cooperation and sustainable practices.\r\n            ', '2025-01-11 22:50:23', '2025-01-11 22:50:23', 0),
(19, 5, 'The Importance of Nutrition in Education', '\r\n                \r\n                \r\n                \r\n                \r\n                \r\n                 Proper nutrition is critical for cognitive development and academic performance. Balanced <b>meals</b> with essential nutrients like proteins, vitamins, and minerals improve concentration, memory, and energy levels. Schools can play a vital role by promoting healthy eating habits through meal programs and education.', '2025-01-11 22:51:04', '2025-01-11 23:11:28', 0),
(20, 5, 'Artificial Intelligence in Healthcare', '\r\n                \r\n                \r\n                Artificial Intelligence (AI) is revolutionizing healthcare through innovations like predictive analytics, personalized medicine, and robotic surgery. AI-powered tools analyze medical data to improve diagnoses and treatment plans. Challenges include data privacy, ethical considerations, and the need for skilled AI professionals in healthcare.\r\n            \r\n            \r\n            ', '2025-01-11 22:52:05', '2025-01-12 12:18:57', 0),
(21, 7, 'Introduction to Microeconomics', 'Microeconomics focuses on the behaviour of individuals and firms in making decisions regarding the allocation of resources. Key concepts include supply and demand, elasticity, marginal utility, and market equilibrium. Understanding these principles helps in analyzing consumer behaviour and production costs.', '2025-01-13 16:07:37', '2025-01-13 16:07:37', 0),
(22, 7, 'Marketing Strategies in the Digital Age', '<div>Digital marketing has revolutionized how businesses reach customers. Strategies like search engine optimization (SEO), pay-per-click (PPC) advertising, email marketing, and social media campaigns are crucial in modern marketing. Data-driven decision-making is at the heart of these approaches to ensure customer engagement and return on investment (ROI).</div><div><br></div>', '2025-01-13 16:09:06', '2025-01-13 16:09:06', 0),
(23, 7, 'Financial Statements and Analysis', '\r\n                Financial statements provide a snapshot of a company\'s financial health. The balance sheet, income statement, and cash flow statement are key reports used by stakeholders. Ratio analysis, such as liquidity and profitability ratios, aids in understanding a company\'s performance and financial position.\r\n            ', '2025-01-13 16:09:46', '2025-01-13 16:09:46', 0),
(24, 8, 'Software Testing Techniques', '\r\n                \r\n                <div><div>Software testing ensures the software is free from bugs and meets user expectations. Techniques include unit testing, integration testing, system testing, and acceptance testing. Automation tools like Selenium and JUnit are often used in testing.</div><div>Keywords Expected: Software testing, unit testing, integration testing, system testing, acceptance testing, Selenium, JUnit, bug-free software.</div></div>\r\n            \r\n            ', '2025-01-13 16:23:28', '2025-01-13 16:26:05', 0),
(25, 9, 'Network Security Essentials', '\r\n                \r\n                <div><div>Network security focuses on protecting data during transmission. Firewalls, intrusion detection systems (IDS), and virtual private networks (VPNs) are essential tools. Techniques like encryption and access control ensure that only authorized individuals can access sensitive data.</div><div>Keywords Expected: Network security, firewalls, intrusion detection systems, VPN, encryption, access control.</div></div>\r\n            \r\n            ', '2025-01-13 16:32:59', '2025-01-13 16:34:35', 0);

-- --------------------------------------------------------

--
-- Table structure for table `recommendations`
--

CREATE TABLE `recommendations` (
  `recommendationid` int(11) NOT NULL,
  `noteid` int(11) DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `resourceName` varchar(255) NOT NULL,
  `resourceURL` varchar(2083) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `subjectArea` varchar(255) DEFAULT NULL,
  `bookAuthor` varchar(255) DEFAULT NULL,
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp(),
  `is_initial` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `recommendations`
--

INSERT INTO `recommendations` (`recommendationid`, `noteid`, `userid`, `resourceName`, `resourceURL`, `description`, `subjectArea`, `bookAuthor`, `createdAt`, `is_initial`) VALUES
(40, NULL, 5, 'The Feminism Book ( Big Ideas)', 'No link available', 'No description available', 'No subject area provided', 'Joya Chatterji', '2025-01-10 02:33:57', 1),
(41, NULL, 5, 'Difficult Women: A History of Feminism in 11 Fights (The Sunday Times Bestseller)', 'No link available', 'No description available', 'No subject area provided', 'Paperback', '2025-01-10 02:33:57', 1),
(42, NULL, 5, 'The Women in me', 'No link available', 'No description available', 'No subject area provided', 'Audio CD', '2025-01-10 02:33:57', 1),
(52, 10, 5, 'PYTHON FOR DATA ANALYSIS: Master the Basics of Data Analysis in Python Using Numpy & Pandas: Answers all your Questions Step-by-Step (Programming for Beginners: A Friendly Q & A Guide Book 2)', 'No link available', 'No description available', 'No subject area provided', 'J D Gauchat', '2025-01-10 02:39:13', 0),
(53, 10, 5, 'Python: - The Bible- 3 Manuscripts in 1 Book: -Python Programming for Beginners -Python Programming for Intermediates -Python Programming for Advanced', 'No link available', 'No description available', 'No subject area provided', 'Erik Bertram', '2025-01-10 02:39:13', 0),
(54, 10, 5, 'Python Programming for Beginners: An Introduction to the Python Computer Language and Computer Programming (Python, Python 3, Python Tutorial)', 'No link available', 'No description available', 'No subject area provided', 'Oona Flanagan', '2025-01-10 02:39:13', 0),
(55, 11, 5, 'Genetics', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-10 02:41:12', 0),
(56, 11, 5, 'Biotechnology', 'No link available', 'No description available', 'No subject area provided', 'H.L. Kaila', '2025-01-10 02:41:12', 0),
(57, 11, 5, 'Top 100 Indian Innovations (2023)', 'No link available', 'No description available', 'No subject area provided', 'Clay Scroggins', '2025-01-10 02:41:12', 0),
(58, 12, 5, 'Oswaal CBSE Question Bank Class 12 English, Physics, Chemistry & Biology (Set of 4 Books) (For 2024 Board Exams)', 'No link available', 'No description available', 'No subject area provided', 'MTG Editorial Board', '2025-01-10 02:41:53', 0),
(59, 12, 5, 'CrPC-Sections & Related Notes', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-10 02:41:53', 0),
(60, 12, 5, 'INDIAN HISTORY ( A Comprehensive Guide for all Competitive Exams )', 'No link available', 'No description available', 'No subject area provided', 'Trinity College London', '2025-01-10 02:41:53', 0),
(61, 13, 5, 'Topic Searching in PubMed: Using the Medical Subject Headings (MeSH)', 'https://www.nlm.nih.gov/oet/ed/pubmed/mesh/index.html', 'learn how to use the medical subject headings (mesh) for expert pubmed searching in this hands-on, self-paced course.', 'Medical Subject Headings (MeSH); PubMed', 'Unknown', '2025-01-10 02:43:41', 0),
(62, 13, 5, 'Cataloging with Medical Subject Headings (MeSH)', 'https://www.nlm.nih.gov/oet/ed/mesh/2023/9-29_mesh-cataloging.html', 'on september 26, 2023, sharon willis, senior cataloging specialist at the u.s. national library of medicine, taught cataloging with medical subject headings (mesh). this webinar explores the use of the medical subject headings (mesh) in the cataloging environment.', 'Medical Subject Headings (MeSH)', 'Unknown', '2025-01-10 02:43:41', 0),
(63, 13, 5, '2019 MeSH Highlights', 'https://www.nlm.nih.gov/bsd/disted/clinics/mesh_2019.html', 'on january 4, 2019, nlm staff provided a highlights tour of the 2019 medical subject headings (mesh). a 20-minute presentation featured new publication types, including systematic reviews; three deleted subheadings; and additional terminology for data, neoplasms and more.', 'Medical Subject Headings (MeSH); PubMed', 'Unknown', '2025-01-10 02:43:41', 0),
(70, 16, 5, 'Web Design with HTML, CSS, JavaScript and Jquery Set', 'No link available', 'No description available', 'No subject area provided', 'Amrinder Arora', '2025-01-11 22:41:56', 0),
(71, 16, 5, 'HTML: Web Guide For Absolute HTML Beginners (Web Development - HTML Book 1)', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-11 22:41:56', 0),
(72, 16, 5, 'Web Design With HTML & CSS : HTML & CSS Complete Beginner\'s Guide', 'No link available', 'No description available', 'No subject area provided', 'DT Editorial Services', '2025-01-11 22:41:56', 0),
(76, 17, 5, 'Yoga and Meditation', 'No link available', 'No description available', 'No subject area provided', 'Hardcover', '2025-01-11 22:49:46', 0),
(77, 17, 5, 'KRIYA YOGA in practice', 'No link available', 'No description available', 'No subject area provided', 'Neven Paar', '2025-01-11 22:49:46', 0),
(78, 17, 5, 'Yoga and Meditation: Understand the Anatomy and Physiology to Perfect Your Practice', 'No link available', 'No description available', 'No subject area provided', 'Tina Gong', '2025-01-11 22:49:46', 0),
(79, 18, 5, 'Climate Variations, Climate Change and Water Resources Engineering', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-11 22:50:29', 0),
(80, 18, 5, 'The Biochar Solution: Carbon Farming and Climate Change', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-11 22:50:29', 0),
(81, 18, 5, 'The Great Derangement: Climate Change and the Unthinkable [Paperback] Ghosh, Amitav', 'No link available', 'No description available', 'No subject area provided', 'Audio, Cassette', '2025-01-11 22:50:29', 0),
(82, 19, 5, 'NUTRITION SCIENCE 7 EDITION', 'No link available', 'No description available', 'No subject area provided', 'Leslie M. Hocking', '2025-01-11 22:51:09', 0),
(83, 19, 5, 'What you must know about vitamins, minerals and herbs', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-11 22:51:10', 0),
(84, 19, 5, 'Your Pregnancy Nutrition Guide', 'No link available', 'No description available', 'No subject area provided', 'James Earls', '2025-01-11 22:51:10', 0),
(85, 20, 5, 'DATA SCIENCE: 2 Books in 1: Data Analytics, Artificial Intelligence, Machine Learning and Deep Learning', 'No link available', 'No description available', 'No subject area provided', 'Sam Newman', '2025-01-11 22:52:09', 0),
(86, 20, 5, 'Artificial Intelligence Question Bank (for Class X)', 'No link available', 'No description available', 'No subject area provided', 'Yashavant Kanetkar', '2025-01-11 22:52:09', 0),
(87, 20, 5, 'Artificial Intelligence & Generative Ai for Beginners: The Complete Guide', 'No link available', 'No description available', 'No subject area provided', 'MP3 CD', '2025-01-11 22:52:09', 0),
(88, 20, 5, 'Artificial Intelligence for People in a Hurry: How You Can Benefit from the Next Industrial Revolution (Artificial Intelligence for Beginners Book 2)', 'No link available', 'No description available', 'No subject area provided', 'Roselyn Teukolsky', '2025-01-11 22:56:05', 0),
(89, 20, 5, 'Artificial Intelligence Oceanography', 'No link available', 'No description available', 'No subject area provided', 'Paperback', '2025-01-11 22:56:05', 0),
(93, NULL, 7, 'Business Law', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:05:48', 1),
(94, NULL, 7, 'The Law', 'No link available', 'No description available', 'No subject area provided', 'S.Y. Quraishi', '2025-01-13 16:05:48', 1),
(95, NULL, 7, 'Business Law : Complete Understanding of Commercial Law| Corporate law| Industrial Law', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:05:48', 1),
(96, 21, 7, 'Principles Of Microeconomics (english, Paperback, H.l. Ahuja)', 'No link available', 'No description available', 'No subject area provided', 'Sree Krishna Seelam', '2025-01-13 16:07:48', 0),
(97, 21, 7, 'Microeconomics For Class - 12 - 12103', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:07:48', 0),
(98, 21, 7, 'Behaviour Based Safety Management', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:07:48', 0),
(99, 22, 7, 'SEO 2024: Learn search engine optimization with smart internet marketing strategies', 'No link available', 'No description available', 'No subject area provided', 'Preloaded Digital Audio Player', '2025-01-13 16:09:11', 0),
(100, 22, 7, 'This is Marketing', 'No link available', 'No description available', 'No subject area provided', 'Hardcover', '2025-01-13 16:09:11', 0),
(101, 22, 7, 'Digital Marketing', 'No link available', 'No description available', 'No subject area provided', 'Thibaut  Meurisse', '2025-01-13 16:09:11', 0),
(102, 23, 7, 'Financial Statement Analysis Handbook', 'No link available', 'No description available', 'No subject area provided', 'Brian Tracy', '2025-01-13 16:09:52', 0),
(103, 23, 7, 'Analysis of Financial Statements Book for Class 12 Part B - CBSE - Examination 2023-2024', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:09:52', 0),
(104, 23, 7, 'Fundamental Analysis for Beginners: Grow Your Investment Portfolio Like A Pro Using Financial Statements and Ratios of Any Business with Zero Investing Experience Required', 'No link available', 'No description available', 'No subject area provided', 'Audio CD', '2025-01-13 16:09:52', 0),
(105, NULL, 8, 'Java Software Development with Event B: A Practical Guide (Synthesis Lectures on Software Engineering)', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:20:12', 1),
(106, NULL, 8, 'Development as Freedom', 'No link available', 'No description available', 'No subject area provided', 'Andrew Collier', '2025-01-13 16:20:12', 1),
(107, NULL, 8, 'Accelerate With AI : How to use AI for Business Growth', 'No link available', 'No description available', 'No subject area provided', 'Brian Christian', '2025-01-13 16:20:12', 1),
(108, 24, 8, 'Java Software Development with Event B: A Practical Guide (Synthesis Lectures on Software Engineering)', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:23:38', 0),
(109, 24, 8, 'Software Architecture with C# 10 and .NET 6: Develop software solutions using microservices, DevOps, EF Core, and design patterns for Azure', 'No link available', 'No description available', 'No subject area provided', 'John Monks', '2025-01-13 16:23:38', 0),
(110, 24, 8, 'Agile Software Development, Principles, Patterns, and Practices (Alan Apt Series)', 'No link available', 'No description available', 'No subject area provided', 'MP3 CD', '2025-01-13 16:23:38', 0),
(111, 24, 8, 'Object Oriented Programming with C++', 'No link available', 'No description available', 'No subject area provided', 'Paul A. Keddy', '2025-01-13 16:25:10', 0),
(112, 24, 8, 'Oop With C++(Revised 1St Ed)', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:25:10', 0),
(113, 24, 8, 'Design Patterns: Elements of Reusable Object-Oriented Software', 'No link available', 'No description available', 'No subject area provided', 'Richard Lee', '2025-01-13 16:25:10', 0),
(114, 24, 8, 'Psychological Testing, 7e', 'No link available', 'No description available', 'No subject area provided', 'Arihant Experts', '2025-01-13 16:26:10', 0),
(115, 24, 8, 'Artificial Intelligence and Software Testing: Building systems you can trust', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:26:10', 0),
(116, 24, 8, 'Lessons Learned in Software Testing: A Context-Driven Approach', 'No link available', 'No description available', 'No subject area provided', 'Rebecca Parsons', '2025-01-13 16:26:10', 0),
(117, NULL, 9, 'Foundations of Computing', 'No link available', 'No description available', 'No subject area provided', 'Mike Chapple', '2025-01-13 16:30:25', 1),
(118, NULL, 9, 'Mobile Edge Computing (Simula SpringerBriefs on Computing Book 9)', 'No link available', 'No description available', 'No subject area provided', 'Hardcover', '2025-01-13 16:30:25', 1),
(119, NULL, 9, 'Soft Computing', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:30:25', 1),
(120, 25, 9, 'IIBF’s IT Security – Covering all Essentials of IT Security in Banking Institutes such as Overview, Security Controls, Security Threats and IS Audit & Regulatory Compliance', 'No link available', 'No description available', 'No subject area provided', 'No author', '2025-01-13 16:33:07', 0),
(121, 25, 9, 'Network Security and Cryptography', 'No link available', 'No description available', 'No subject area provided', 'Lane Bailey', '2025-01-13 16:33:07', 0),
(122, 25, 9, 'Introduction to Cyber Security : Guide to the World of Cyber Security', 'No link available', 'No description available', 'No subject area provided', 'David West', '2025-01-13 16:33:07', 0),
(123, 25, 9, 'Algorithms', 'No link available', 'No description available', 'No subject area provided', 'Ram Ji Tripathi', '2025-01-13 16:33:58', 0),
(124, 25, 9, 'Data Structures and Algorithms Made Easy', 'No link available', 'No description available', 'No subject area provided', 'Narasimha Karumanchi', '2025-01-13 16:33:58', 0),
(125, 25, 9, 'Data Structures and Algorithms Using C++', 'No link available', 'No description available', 'No subject area provided', 'Hemang Doshi', '2025-01-13 16:33:58', 0),
(126, 25, 9, 'The Antisocial Network', 'No link available', 'No description available', 'No subject area provided', 'Audio CD', '2025-01-13 16:34:42', 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userid` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `kindOfSchool` enum('University','College','High School','Other') NOT NULL,
  `currentCM` text NOT NULL,
  `subOfInt` text NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`, `username`, `name`, `password`, `email`, `kindOfSchool`, `currentCM`, `subOfInt`, `createdAt`) VALUES
(5, 'user', 'user', '$2b$12$HB46VIyL0VTK2F5ygwScO.xPUbfXUhTKYUuwa9O2rMVp7z3rj.npC', 'user@gmail.com', 'University', 'feminism', 'women\'s rights', '2025-01-09 00:56:14'),
(7, 'david', 'david strachan ', '$2b$12$Ky7WE92PFdjmL6jmCxsWyObcntEiQsc1hZx/FqPmpO5zXhM159GXK', 'creativsyncbroy@gmail.com', 'University', 'business law, tax law', 'travelling', '2025-01-13 16:05:47'),
(8, 'ta', 'Oluwatojuba Adebayo', '$2b$12$GkDdgWo0NpmLDFrZhTGRfufzZjPC.z2uUmRqVME167Hzvh4La7W4O', 'ta2011@outlook.com', 'University', 'Software Development', 'Ai', '2025-01-13 16:20:11'),
(9, 'sasumiru', 'Samir Khalafalla', '$2b$12$fB1FyF9DcprUzXDftPkHCuB9XPVvH87z5TVLpA.ycuJJ4JCDLWMEu', 'sk2053@hw.ac.uk', 'University', 'computing science', 'physics, ai, computing science', '2025-01-13 16:30:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `feedbackrelevance`
--
ALTER TABLE `feedbackrelevance`
  ADD PRIMARY KEY (`feedbackid`),
  ADD KEY `userid` (`userid`),
  ADD KEY `noteid` (`noteid`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`noteid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `recommendations`
--
ALTER TABLE `recommendations`
  ADD PRIMARY KEY (`recommendationid`),
  ADD KEY `noteid` (`noteid`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `feedbackrelevance`
--
ALTER TABLE `feedbackrelevance`
  MODIFY `feedbackid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `noteid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `recommendations`
--
ALTER TABLE `recommendations`
  MODIFY `recommendationid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=127;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `feedbackrelevance`
--
ALTER TABLE `feedbackrelevance`
  ADD CONSTRAINT `feedbackrelevance_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`),
  ADD CONSTRAINT `feedbackrelevance_ibfk_2` FOREIGN KEY (`noteid`) REFERENCES `notes` (`noteid`);

--
-- Constraints for table `notes`
--
ALTER TABLE `notes`
  ADD CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE CASCADE;

--
-- Constraints for table `recommendations`
--
ALTER TABLE `recommendations`
  ADD CONSTRAINT `recommendations_ibfk_1` FOREIGN KEY (`noteid`) REFERENCES `notes` (`noteid`) ON DELETE CASCADE,
  ADD CONSTRAINT `recommendations_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
