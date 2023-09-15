-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: aerolinea
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `satisfaction_fallidos`
--

DROP TABLE IF EXISTS `satisfaction_fallidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satisfaction_fallidos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gender` enum('Male','Female') NOT NULL DEFAULT 'Male',
  `customer_type` enum('disloyal Customer','Loyal Customer') NOT NULL DEFAULT 'disloyal Customer',
  `age` int NOT NULL DEFAULT '0',
  `type_of_travel` enum('Personal Travel','Business Travel') NOT NULL DEFAULT 'Personal Travel',
  `class` enum('Eco','Eco Plus','Business') NOT NULL DEFAULT 'Eco',
  `flight_distance` int NOT NULL DEFAULT '0',
  `inflight_wifi_service` int NOT NULL DEFAULT '0',
  `departure_arrival_time_convenient` int NOT NULL DEFAULT '0',
  `ease_of_online_booking` int NOT NULL DEFAULT '0',
  `gate_location` int NOT NULL DEFAULT '0',
  `food_and_drink` int NOT NULL DEFAULT '0',
  `online_boarding` int NOT NULL DEFAULT '0',
  `seat_comfort` int NOT NULL DEFAULT '0',
  `inflight_entetairment` int NOT NULL DEFAULT '0',
  `onboard_service` int NOT NULL DEFAULT '0',
  `leg_room_service` int NOT NULL DEFAULT '0',
  `baggage_handling` int NOT NULL DEFAULT '0',
  `checkin_service` int NOT NULL DEFAULT '0',
  `cleanliness` int NOT NULL DEFAULT '0',
  `inflight_service` int NOT NULL DEFAULT '0',
  `departure_delay_in_minutes` int NOT NULL DEFAULT '0',
  `arrival_delay_in_minutes` int NOT NULL DEFAULT '0',
  `satisfaction` enum('neutral or dissatisfied','satisfied') NOT NULL DEFAULT 'neutral or dissatisfied',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satisfaction_fallidos`
--

LOCK TABLES `satisfaction_fallidos` WRITE;
/*!40000 ALTER TABLE `satisfaction_fallidos` DISABLE KEYS */;
INSERT INTO `satisfaction_fallidos` VALUES (1,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(2,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(3,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(4,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(5,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(6,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(7,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(8,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(9,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(10,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(11,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(12,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(13,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(14,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(15,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(16,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(17,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(18,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(19,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(20,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(21,'Male','Loyal Customer',10,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(22,'Male','Loyal Customer',30,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied'),(23,'Male','Loyal Customer',0,'Business Travel','Eco',100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'neutral or dissatisfied');
/*!40000 ALTER TABLE `satisfaction_fallidos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-12 11:58:04
