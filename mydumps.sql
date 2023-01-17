-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ahvdb
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$sAfix6N9lcgouErzjERk3p$ZSRgzHnEO4TCDED6h4qLHEvGUDNoFy/tJ/kTotJO030=','2022-10-12 13:18:19.511310',1,'admin','','','admin@gmail.com',1,1,'2022-10-07 09:01:28.702289'),(2,'pbkdf2_sha256$320000$Yh6TJn2mCWg96dps6BxAyf$sDPSnh1wjWeBBlxItUl2oOi2kssX4XTaj8QVyVAxroc=','2022-10-11 08:12:43.000000',1,'updeshkumar','Updesh','kumar','updeshkumarpal7753@gmail.com',1,1,'2022-10-11 08:12:09.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `device_id` int NOT NULL AUTO_INCREMENT,
  `refresh_token` varchar(500) DEFAULT 'False',
  `device_type` varchar(20) DEFAULT NULL,
  `device_token` varchar(255) DEFAULT 'False',
  `aws_arn` varchar(255) DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_active` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`device_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEsInVzZXJUeXBlIjoiVVNFUiIsImZ1bGxOYW1lIjpudWxsLCJwcm9maWxlUGljIjoiIiwiY291bnRyeUNvZGUiOjkxLCJtb2JpbGVObyI6Ijc3NTM4Mjg4NjMiLCJleHAiOjE2NzA2MDcyNDd9.uUxKm5G5CufP1Y6FpqEtcvoHXAT-NqbMaI9JmHiN-14','ANDROID','123456','','1','2022-10-08 09:09:36',1);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-10-11 08:12:09.797670','2','updeshkumar',1,'[{\"added\": {}}]',4,1),(2,'2022-10-11 08:12:48.317643','2','updeshkumar',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Superuser status\", \"Last login\"]}}]',4,1),(3,'2022-10-11 08:13:03.093984','2','updeshkumar',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'auth','user'),(2,'user','device'),(1,'user','mastercontents'),(3,'user','vehicalbasicdetail');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-10-07 08:57:30.266443'),(2,'auth','0001_initial','2022-10-07 08:57:30.935437'),(3,'admin','0001_initial','2022-10-07 08:57:31.113893'),(4,'admin','0002_logentry_remove_auto_add','2022-10-07 08:57:31.134663'),(5,'admin','0003_logentry_add_action_flag_choices','2022-10-07 08:57:31.154610'),(6,'contenttypes','0002_remove_content_type_name','2022-10-07 08:57:31.412921'),(7,'auth','0002_alter_permission_name_max_length','2022-10-07 08:57:31.517734'),(8,'auth','0003_alter_user_email_max_length','2022-10-07 08:57:31.585145'),(9,'auth','0004_alter_user_username_opts','2022-10-07 08:57:31.614070'),(10,'auth','0005_alter_user_last_login_null','2022-10-07 08:57:31.759678'),(11,'auth','0006_require_contenttypes_0002','2022-10-07 08:57:31.766661'),(12,'auth','0007_alter_validators_add_error_messages','2022-10-07 08:57:31.793588'),(13,'auth','0008_alter_user_username_max_length','2022-10-07 08:57:31.918307'),(14,'auth','0009_alter_user_last_name_max_length','2022-10-07 08:57:32.040712'),(15,'auth','0010_alter_group_name_max_length','2022-10-07 08:57:32.085606'),(16,'auth','0011_update_proxy_permissions','2022-10-07 08:57:32.111522'),(17,'auth','0012_alter_user_first_name_max_length','2022-10-07 08:57:32.233196'),(18,'sessions','0001_initial','2022-10-07 08:57:32.290530');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('85bquxvw5v9yfts1wg7qgl3ufpy8ofip','.eJxVjDEOwjAMRe-SGUV2k5aEkZ0zRHZsSAE1UtNOiLtDpQ6w_vfef5lE61LS2nROo5iTQXP43ZjyQ6cNyJ2mW7W5Tss8st0Uu9NmL1X0ed7dv4NCrXzrEFR9ABXvBANGQc6gMERkVUIIXe6uIBSxd8NRWZ1AFGDOHnvxYt4f6sw4TQ:1oibcp:VViXznskG68dL5UpdyPriKEhuqROhNnjDpnNwOLBvlo','2022-10-26 13:18:19.524418'),('duw1xz6rpqto7jlklrofqc0ajrtbi72p','.eJxVjDEOwjAMRe-SGUV2k5aEkZ0zRHZsSAE1UtNOiLtDpQ6w_vfef5lE61LS2nROo5iTQXP43ZjyQ6cNyJ2mW7W5Tss8st0Uu9NmL1X0ed7dv4NCrXzrEFR9ABXvBANGQc6gMERkVUIIXe6uIBSxd8NRWZ1AFGDOHnvxYt4f6sw4TQ:1ogkTK:WpS7CRv8EpZufmyFXzaIALikZxdhfzGvvEH56ZUvdJA','2022-10-21 10:20:50.597732'),('lvqmlwknxc1dg6gecy2x5perulpfng9x','.eJxVjDEOwjAMRe-SGUV2k5aEkZ0zRHZsSAE1UtNOiLtDpQ6w_vfef5lE61LS2nROo5iTQXP43ZjyQ6cNyJ2mW7W5Tss8st0Uu9NmL1X0ed7dv4NCrXzrEFR9ABXvBANGQc6gMERkVUIIXe6uIBSxd8NRWZ1AFGDOHnvxYt4f6sw4TQ:1oiAKE:KEjOvi17iwFWREvMMfKOwV9vNeKGMQVwzQnXLKf3vgs','2022-10-25 08:09:18.171124'),('rlgs1rzf5njn5uy75rcsmov2quntxg8s','.eJxVjDEOwjAMRe-SGUV2k5aEkZ0zRHZsSAE1UtNOiLtDpQ6w_vfef5lE61LS2nROo5iTQXP43ZjyQ6cNyJ2mW7W5Tss8st0Uu9NmL1X0ed7dv4NCrXzrEFR9ABXvBANGQc6gMERkVUIIXe6uIBSxd8NRWZ1AFGDOHnvxYt4f6sw4TQ:1ogjF4:Pdf2rd7UeIJq702jg_2VmfWkZGKBNAUpePhXKB3dkBw','2022-10-21 09:02:02.291313');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heavyvehicaladdressupload`
--

DROP TABLE IF EXISTS `heavyvehicaladdressupload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heavyvehicaladdressupload` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `tehsil` varchar(100) DEFAULT NULL,
  `houseblockstreet` varchar(100) DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `is_active` varchar(45) DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heavyvehicaladdressupload`
--

LOCK TABLES `heavyvehicaladdressupload` WRITE;
/*!40000 ALTER TABLE `heavyvehicaladdressupload` DISABLE KEYS */;
/*!40000 ALTER TABLE `heavyvehicaladdressupload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heavyvehicaldocumentupload`
--

DROP TABLE IF EXISTS `heavyvehicaldocumentupload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heavyvehicaldocumentupload` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `uploadvehicalphoto` varchar(255) DEFAULT NULL,
  `uploadaadharcard` varchar(255) DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `is_active` varchar(45) DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heavyvehicaldocumentupload`
--

LOCK TABLES `heavyvehicaldocumentupload` WRITE;
/*!40000 ALTER TABLE `heavyvehicaldocumentupload` DISABLE KEYS */;
/*!40000 ALTER TABLE `heavyvehicaldocumentupload` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heavyvehivalregistration`
--

DROP TABLE IF EXISTS `heavyvehivalregistration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heavyvehivalregistration` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `vehical_name` varchar(200) DEFAULT NULL,
  `vehical_number` varchar(200) DEFAULT NULL,
  `model_number` varchar(200) DEFAULT NULL,
  `ownername` varchar(300) DEFAULT NULL,
  `Aadhar_number` varchar(50) DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `is_active` varchar(45) DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heavyvehivalregistration`
--

LOCK TABLES `heavyvehivalregistration` WRITE;
/*!40000 ALTER TABLE `heavyvehivalregistration` DISABLE KEYS */;
INSERT INTO `heavyvehivalregistration` VALUES (1,'bus','123','123','muskan','1245',NULL,'1'),(2,'bus','123','123','muskan','1245',NULL,'1'),(3,'bus','123','123','muskan','1245',NULL,'1'),(4,'bus','123','123','muskan','1245',NULL,'1'),(5,'bus','123','123','muskan','1245',NULL,'1'),(6,'bus','123','123','muskan','1245',NULL,'1'),(7,'bus','123','123','muskan','1245',NULL,'1'),(8,'train','1234','1234','updesh','124545',NULL,'1'),(9,'train','1234','1234','updesh','124545',NULL,'1');
/*!40000 ALTER TABLE `heavyvehivalregistration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `labour_contructor`
--

DROP TABLE IF EXISTS `labour_contructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `labour_contructor` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `labourcontractorname` varchar(300) DEFAULT NULL,
  `labourwork` varchar(200) DEFAULT NULL,
  `lobourinnumber` varchar(100) DEFAULT NULL,
  `contractoraadharnumber` int DEFAULT NULL,
  `mobilenumber` int DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `labour_contructor`
--

LOCK TABLES `labour_contructor` WRITE;
/*!40000 ALTER TABLE `labour_contructor` DISABLE KEYS */;
/*!40000 ALTER TABLE `labour_contructor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upload_lobour_document`
--

DROP TABLE IF EXISTS `upload_lobour_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `upload_lobour_document` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `labourgroupphoto` varchar(255) DEFAULT NULL,
  `uploadlabourphoto` varchar(255) DEFAULT NULL,
  `uploadaadharcard` varchar(255) DEFAULT NULL,
  `is_active` varchar(45) NOT NULL DEFAULT '1',
  `created_by` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upload_lobour_document`
--

LOCK TABLES `upload_lobour_document` WRITE;
/*!40000 ALTER TABLE `upload_lobour_document` DISABLE KEYS */;
/*!40000 ALTER TABLE `upload_lobour_document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `country_code` int DEFAULT NULL,
  `mobile_number` varchar(20) DEFAULT NULL,
  `otp` varchar(4) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `email_id` varchar(100) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  `profile_pic` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `is_active` tinyint NOT NULL DEFAULT '1',
  `is_delete` tinyint NOT NULL DEFAULT '0',
  `gender` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,NULL,NULL,91,'7753828863','4905','2022-10-07 15:14:31',0,NULL,'USER',NULL,NULL,1,0,NULL,'2022-10-07 15:14:31'),(2,NULL,NULL,91,'7827536359','6624','2022-10-08 10:33:23',0,NULL,'USER',NULL,NULL,1,0,NULL,'2022-10-08 10:33:23');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_address`
--

DROP TABLE IF EXISTS `user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_address` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `tehsil` varchar(100) DEFAULT NULL,
  `houseblockstreet` varchar(100) DEFAULT NULL,
  `is_active` varchar(45) DEFAULT '1',
  `created_by` int DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_address`
--

LOCK TABLES `user_address` WRITE;
/*!40000 ALTER TABLE `user_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_mastercontents`
--

DROP TABLE IF EXISTS `user_mastercontents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_mastercontents` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `key` varchar(200) DEFAULT NULL,
  `value` varchar(200) DEFAULT NULL,
  `relate_to` bigint DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_mastercontents`
--

LOCK TABLES `user_mastercontents` WRITE;
/*!40000 ALTER TABLE `user_mastercontents` DISABLE KEYS */;
INSERT INTO `user_mastercontents` VALUES (1,'country','India',0),(2,'state','Uttar Pradesh',1),(3,'state','Madhya Pradesh',1),(4,'district','Kannauj',2),(5,'district','Mainpuri',2),(6,'district','Satna',3),(7,'city','Bewar',5),(8,'city','Chhibramau',4),(9,'district','farrukhabad',2),(10,'city','jahanganj',9),(11,'tehsil','fatehgarh',9),(12,'tehsil','chhibramau',4),(13,'tehsil','noida',2),(14,'state','vihar',2),(15,'city','chatarpur',14);
/*!40000 ALTER TABLE `user_mastercontents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicalbasicdetail`
--

DROP TABLE IF EXISTS `vehicalbasicdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicalbasicdetail` (
  `vehical_name` varchar(200) DEFAULT NULL,
  `vehical_number` varchar(500) DEFAULT NULL,
  `model_number` varchar(500) DEFAULT NULL,
  `ownername` varchar(300) DEFAULT NULL,
  `Aadhar_number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicalbasicdetail`
--

LOCK TABLES `vehicalbasicdetail` WRITE;
/*!40000 ALTER TABLE `vehicalbasicdetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehicalbasicdetail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-13 18:51:07
