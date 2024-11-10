CREATE DATABASE  IF NOT EXISTS `hoteleria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hoteleria`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: hoteleria
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `habitacion`
--

DROP TABLE IF EXISTS `habitacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habitacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero` int DEFAULT NULL,
  `url_img` varchar(45) DEFAULT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `id_hotel` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_habiacion_hotel_idx` (`id_hotel`),
  CONSTRAINT `fk_habiacion_hotel` FOREIGN KEY (`id_hotel`) REFERENCES `hotel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habitacion`
--

LOCK TABLES `habitacion` WRITE;
/*!40000 ALTER TABLE `habitacion` DISABLE KEYS */;
INSERT INTO `habitacion` VALUES (1,10,NULL,'individual',100,1),(2,11,NULL,'suite',110,1),(3,12,NULL,'doble',120,1),(4,20,NULL,'individual',200,2),(5,21,NULL,'suite',210,2),(6,22,NULL,'doble',250,2),(10,3,NULL,'individual',350,3),(11,4,NULL,'suite',370,3),(12,5,NULL,'premiun',400,3);
/*!40000 ALTER TABLE `habitacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habitacion_servicios`
--

DROP TABLE IF EXISTS `habitacion_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habitacion_servicios` (
  `id_habitacion_servicios` int NOT NULL AUTO_INCREMENT,
  `id_habitacion` int NOT NULL,
  `id_servicios` int NOT NULL,
  PRIMARY KEY (`id_habitacion_servicios`),
  KEY `fk_habitacion_hab_serv_idx` (`id_habitacion`),
  KEY `fk_servicio_hab_serv_idx` (`id_servicios`),
  CONSTRAINT `fk_habitacion_hab_serv` FOREIGN KEY (`id_habitacion`) REFERENCES `habitacion` (`id`),
  CONSTRAINT `fk_servicio_hab_serv` FOREIGN KEY (`id_servicios`) REFERENCES `servicios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habitacion_servicios`
--

LOCK TABLES `habitacion_servicios` WRITE;
/*!40000 ALTER TABLE `habitacion_servicios` DISABLE KEYS */;
INSERT INTO `habitacion_servicios` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,1),(5,2,2),(6,2,3),(7,2,4),(8,3,3),(9,3,2),(10,3,1),(11,3,5),(12,3,4);
/*!40000 ALTER TABLE `habitacion_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel`
--

DROP TABLE IF EXISTS `hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `url_img` varchar(45) DEFAULT NULL,
  `region` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel`
--

LOCK TABLES `hotel` WRITE;
/*!40000 ALTER TABLE `hotel` DISABLE KEYS */;
INSERT INTO `hotel` VALUES (1,'continental','calle falsa 340','lorem ipsu data ta data data descripcion',NULL,'buenos aires'),(2,'la frula','lincoln 5425','un hotel para estar en comodidad en familia',NULL,'mar del plata'),(3,'messirve hotel','caminito 2324','busque su lugar ideal',NULL,NULL);
/*!40000 ALTER TABLE `hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel_servicios`
--

DROP TABLE IF EXISTS `hotel_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel_servicios` (
  `id_hotel_servicios` int NOT NULL AUTO_INCREMENT,
  `id_hotel` int NOT NULL,
  `id_servicio` int NOT NULL,
  PRIMARY KEY (`id_hotel_servicios`),
  KEY `fk_hotel_hs_idx` (`id_hotel`),
  KEY `fk_servicio_hs_idx` (`id_servicio`),
  CONSTRAINT `fk_hotel_hs` FOREIGN KEY (`id_hotel`) REFERENCES `hotel` (`id`),
  CONSTRAINT `fk_servicio_hs` FOREIGN KEY (`id_servicio`) REFERENCES `servicios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel_servicios`
--

LOCK TABLES `hotel_servicios` WRITE;
/*!40000 ALTER TABLE `hotel_servicios` DISABLE KEYS */;
INSERT INTO `hotel_servicios` VALUES (1,1,4),(2,1,5),(3,1,6),(4,1,1),(5,1,2),(6,1,3),(7,2,6),(8,2,5),(9,2,4),(10,2,3),(11,3,1),(12,3,2),(13,3,3),(14,3,4),(15,3,7),(16,3,8);
/*!40000 ALTER TABLE `hotel_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva`
--

DROP TABLE IF EXISTS `reserva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_habitacion` int NOT NULL,
  `llegada` date NOT NULL,
  `salida` date NOT NULL,
  `cliente_apellido` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `precio` int NOT NULL,
  `fecha_cancelacion` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_habitacion_reserva_idx` (`id_habitacion`),
  CONSTRAINT `fk_habitacion_reserva` FOREIGN KEY (`id_habitacion`) REFERENCES `habitacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva`
--

LOCK TABLES `reserva` WRITE;
/*!40000 ALTER TABLE `reserva` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva_servicios`
--

DROP TABLE IF EXISTS `reserva_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva_servicios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_reserva` int DEFAULT NULL,
  `id_servicio` int DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `precio` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reserva_idx` (`id_reserva`),
  KEY `fk_servicio_idx` (`id_servicio`),
  CONSTRAINT `fk_reserva` FOREIGN KEY (`id_reserva`) REFERENCES `reserva` (`id`),
  CONSTRAINT `fk_servicio` FOREIGN KEY (`id_servicio`) REFERENCES `servicios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva_servicios`
--

LOCK TABLES `reserva_servicios` WRITE;
/*!40000 ALTER TABLE `reserva_servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `servicio` varchar(45) DEFAULT NULL,
  `basico` tinyint DEFAULT NULL,
  `precio` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
INSERT INTO `servicios` VALUES (1,'tv',1,0),(2,'aire',1,0),(3,'desayuno',0,10),(4,'spa',0,15),(5,'gym',0,20),(6,'barra libre',0,500),(7,'casino',0,0),(8,'restaurante',0,0);
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-10 20:15:42
