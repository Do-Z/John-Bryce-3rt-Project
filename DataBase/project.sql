-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `country_name` varchar(45) NOT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'USA'),(2,'Germany'),(3,'Spain'),(4,'United Kingdom'),(5,'India'),(6,'Brazil'),(7,'Italy'),(8,'Georgia'),(9,'Turkey'),(10,'Sweden'),(11,'France');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `user_id` int NOT NULL,
  `vacation_id` int NOT NULL,
  KEY `userId_idx` (`user_id`),
  KEY `vacationId_idx` (`vacation_id`),
  CONSTRAINT `userId` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `vacationId` FOREIGN KEY (`vacation_id`) REFERENCES `vacations` (`vacation_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Admin'),(2,'User');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(256) NOT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `roleId_idx` (`role_id`),
  CONSTRAINT `roleId` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Dor','Ziv','dor@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',1),(2,'David','Ben-Gurion','david@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(3,'Moshe','Sharett','moshe@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(4,'Levi','Eshkol','levi@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(5,'Golda','Meir','golda@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(8,'Yitzhak','Rabin','yitzhakr@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(9,'Menachem','Begin','menachem@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(10,'Yitzhak','Shamir','yitzhaks@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2),(11,'Matan','Maman','matan@gmail.com','bf616fbe2ca17c775fe46b08e0327f875c579e9d96be03bdcd6a36ed6ed96b3ecd7b5150bcd6d317947f874675f1fe26e5617d7f9761e0ebc7f2dbce0b26f351',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacation_id` int NOT NULL AUTO_INCREMENT,
  `country_id` int NOT NULL,
  `description` text NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` int NOT NULL,
  `image` varchar(400) NOT NULL,
  PRIMARY KEY (`vacation_id`),
  KEY `countrieId_idx` (`country_id`),
  CONSTRAINT `countrieId` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (1,1,'Experience the vibrant energy of New York City with our vacation packages! Explore iconic landmarks, indulge in world-class dining, and immerse yourself in the rich culture. From Broadway shows to Central Park strolls, NYC offers unforgettable adventures for everyone.','2020-05-03','2020-05-09',5000,'NYC.png'),(2,2,'Explore the rich history and dynamic culture of Berlin with our exclusive vacation packages! Discover iconic landmarks, enjoy vibrant nightlife, and delve into world-class museums. Whether it\'s art, history, or culinary delights, Berlin offers an unforgettable experience for every traveler.','2020-04-04','2020-04-09',900,'Berlin.png'),(3,3,'Experience the vibrant charm of Madrid with our tailored vacation packages! Wander through historic streets, savor delicious tapas, and enjoy lively flamenco shows. From world-renowned museums to beautiful parks, Madrid offers an unforgettable blend of culture and excitement for every traveler.','2020-09-25','2020-09-30',1000,'Madrid.png'),(4,3,'\nDiscover the magic of Barcelona with our bespoke vacation packages! Marvel at Gaudí\'s architectural wonders, relax on sun-kissed beaches, and savor delicious Catalan cuisine. From vibrant markets to lively festivals, Barcelona offers an unforgettable blend of culture, beauty, and excitement.','2020-08-05','2020-08-10',950,'Barcelona.png'),(5,4,'Immerse yourself in the historic charm of London with our curated vacation packages! Explore iconic landmarks, enjoy world-class theater, and indulge in diverse culinary delights. From bustling markets to serene parks, London offers an unforgettable experience rich in culture and excitement.','2020-07-07','2020-07-11',1900,'London.png'),(6,5,'Explore the vibrant culture of New Delhi with our exclusive vacation packages! Wander through bustling markets, marvel at historic monuments, and savor flavorful cuisine. From the grandeur of the Red Fort to the serenity of Lotus Temple, New Delhi captivates every traveler.','2021-01-07','2021-01-13',1500,'NewDelhi.png'),(7,6,'Experience the rhythm and beauty of Rio de Janeiro with our bespoke vacation packages! Lounge on stunning beaches, explore lush rainforests, and samba the night away. From iconic landmarks like Christ the Redeemer to vibrant street festivals, Rio offers an unforgettable escape.','2021-03-04','2021-03-13',5300,'Rio.png'),(8,7,'Embark on a journey through history and romance in Rome with our tailored vacation packages! Discover ancient ruins, savor authentic Italian cuisine, and immerse yourself in the city\'s artistic treasures. From the Colosseum to Vatican City, Rome promises an unforgettable adventure.','2021-02-04','2021-02-09',1150,'Rome.png'),(9,8,'Discover the charm of Tbilisi with our exclusive vacation packages! Immerse yourself in Georgian hospitality, stroll through historic streets, and indulge in delectable cuisine. From ancient churches to vibrant markets, Tbilisi promises a captivating cultural experience for every traveler.','2021-03-14','2021-03-20',900,'Tbilisi.png'),(11,9,'Experience the allure of Istanbul with our tailored vacation packages! Delight in the blend of East and West as you explore historic mosques, shop in bustling bazaars, and cruise the scenic Bosphorus. Istanbul offers an unforgettable journey through time and culture.','2021-03-14','2021-03-20',750,'Istanbul.png'),(12,10,'Explore the beauty of Stockholm with our curated vacation packages! Wander through charming medieval streets, visit world-class museums, and cruise the scenic archipelago. From historic palaces to trendy cafes, Stockholm offers a blend of history, culture, and modern Scandinavian charm.','2021-06-16','2021-06-21',1200,'Stockholm.png'),(13,11,'Indulge in the romance and culture of Paris with our exclusive vacation packages! Discover iconic landmarks, savor gourmet cuisine, and stroll along the Seine. From art museums to charming cafes, Paris promises an enchanting experience for every traveler.','2021-08-12','2021-08-19',2200,'Paris.png'),(16,3,'Experience the picturesque beauty of Provence with our bespoke vacation packages! Explore quaint villages, stroll through lavender fields in bloom, and savor exquisite French cuisine. From historic châteaux to vibrant markets, Provence offers a serene retreat in the heart of southern France.','2024-06-01','2024-07-08',2500,'Provence.png');
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-12 11:01:22
