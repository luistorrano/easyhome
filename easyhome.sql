-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: easyhome
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_usuario'),(22,'Can change user',6,'change_usuario'),(23,'Can delete user',6,'delete_usuario'),(24,'Can view user',6,'view_usuario'),(25,'Can add República',7,'add_republica'),(26,'Can change República',7,'change_republica'),(27,'Can delete República',7,'delete_republica'),(28,'Can view República',7,'view_republica'),(29,'Can add Mensagem',8,'add_mensagem'),(30,'Can change Mensagem',8,'change_mensagem'),(31,'Can delete Mensagem',8,'delete_mensagem'),(32,'Can view Mensagem',8,'view_mensagem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_mysite_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_mysite_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `mysite_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-19 13:43:58.473674','15','Republica da USJT',2,'[{\"changed\": {\"fields\": [\"slug\", \"user\"]}}]',7,14);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(8,'mysite','mensagem'),(7,'mysite','republica'),(6,'mysite','usuario'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-02 18:24:11.029988'),(2,'contenttypes','0002_remove_content_type_name','2018-10-02 18:24:12.783615'),(3,'auth','0001_initial','2018-10-02 18:24:18.491045'),(4,'auth','0002_alter_permission_name_max_length','2018-10-02 18:24:18.670460'),(5,'auth','0003_alter_user_email_max_length','2018-10-02 18:24:18.750509'),(6,'auth','0004_alter_user_username_opts','2018-10-02 18:24:18.805637'),(7,'auth','0005_alter_user_last_login_null','2018-10-02 18:24:18.867131'),(8,'auth','0006_require_contenttypes_0002','2018-10-02 18:24:18.915362'),(9,'auth','0007_alter_validators_add_error_messages','2018-10-02 18:24:19.001089'),(10,'auth','0008_alter_user_username_max_length','2018-10-02 18:24:19.063091'),(11,'auth','0009_alter_user_last_name_max_length','2018-10-02 18:24:19.133054'),(12,'mysite','0001_initial','2018-10-02 18:24:26.988647'),(13,'admin','0001_initial','2018-10-02 18:24:29.514739'),(14,'admin','0002_logentry_remove_auto_add','2018-10-02 18:24:29.632900'),(15,'admin','0003_logentry_add_action_flag_choices','2018-10-02 18:24:29.713695'),(16,'sessions','0001_initial','2018-10-02 18:24:30.764155'),(17,'mysite','0002_republica_rep_id','2018-10-03 18:13:12.820040'),(18,'mysite','0002_auto_20181016_0859','2018-10-16 11:59:27.546289'),(19,'mysite','0003_auto_20181017_1953','2018-10-17 22:53:38.421090'),(20,'mysite','0004_mensagem','2018-11-19 16:09:41.454879'),(21,'mysite','0005_auto_20181120_1749','2018-11-20 19:49:27.525873');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1fs5rkk5dr6mb9bswz51amsvpvejzoba','NTk2NmE5OTdlM2MzOTE1OGM0Y2ZlYjZjYmM5YjY2Mzk2OTBmMWRjMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNWU2MDQ4Y2Q0ODVkNDhmZWFiNTAxMjVhZWZjYzEzMWMxNTAyYzkyIn0=','2018-10-31 22:30:05.927737'),('2mtyjmrbz9icu0rzdagx8ucpljj1karr','NzlhOWMyY2RmZjMxMGQzM2RmOGNmODI5OTQ2OTc1OTJiY2RiZTI1YTp7fQ==','2018-10-20 17:31:40.164812'),('3xxgvnk8wfas55li24r6ube0t6dgajg5','NzlhOWMyY2RmZjMxMGQzM2RmOGNmODI5OTQ2OTc1OTJiY2RiZTI1YTp7fQ==','2018-10-20 17:51:43.840718'),('bq47hrng4vx2td4eeyfkgwf5xzlthqsv','NzlhOWMyY2RmZjMxMGQzM2RmOGNmODI5OTQ2OTc1OTJiY2RiZTI1YTp7fQ==','2018-10-20 18:10:18.724879'),('e7lr1bniw950bkphzz39lowzw4pk58ci','YWZlZDRmYTBjYTNjZTQxMmI0YWMzY2Q5MWQ1NGNiMmVlMjQyMDM5YTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDQ2NWQ1MmM0NzE5YmZkNTMxODkzYzc3YTg5N2Q2YjE3ODg2ZjAzOSJ9','2018-12-04 14:11:03.008968'),('pk891co4cjpz5djz6bchbszaobt5qrn9','NTk2NmE5OTdlM2MzOTE1OGM0Y2ZlYjZjYmM5YjY2Mzk2OTBmMWRjMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNWU2MDQ4Y2Q0ODVkNDhmZWFiNTAxMjVhZWZjYzEzMWMxNTAyYzkyIn0=','2018-10-28 19:44:34.244984'),('ql1vfzn7w7ipnb2miae391jds0j0anlg','ZmJkNDhiYjYzNmJjMjQ4MzZiOTQ1MzIyMmQxOTJiNGEzMmI5OTY0Yzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYmU3MWRiZDM5NjhiNzI5ZmI1MzFiYTZlMGI4NmM4YmU3ZGE5N2IyIn0=','2018-12-04 15:45:18.004588'),('r31n9f9fh7120shox7uxv24pt60sslvc','ZmJkNDhiYjYzNmJjMjQ4MzZiOTQ1MzIyMmQxOTJiNGEzMmI5OTY0Yzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYmU3MWRiZDM5NjhiNzI5ZmI1MzFiYTZlMGI4NmM4YmU3ZGE5N2IyIn0=','2018-12-06 16:38:47.097214'),('rjnzgal9lhm12tia632b4lcefaadozfj','YTY4NTA1MWU1YTY2MjA3NzkwYTc2MTY2YjUxNDA1MjFhOGNlNGU5NDp7Il9hdXRoX3VzZXJfaWQiOiIxMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWQ4ZDQ5MjRjMDViMmEzZTA1YjAxNzVhYzQ2MmVlNTU5MGM2YTAwOSJ9','2018-11-09 21:03:12.290349'),('va3w00dql2s0fzagysrzvba3pcqjw56q','NjkyYzQzYjg2MGY5YjMwNmYyYTBlNjc1ZjU2ZWJkMTlhNTU3NWM3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODg3MjY4YzYyNjQ2MDIzNmY3OGM1NWIzNmJkZDIxZDMxNmVjZGZkMCJ9','2018-11-09 23:33:37.654060'),('vb3y1pj2xd7hoci5i4bvaf28ep0h2qcq','NTk2NmE5OTdlM2MzOTE1OGM0Y2ZlYjZjYmM5YjY2Mzk2OTBmMWRjMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNWU2MDQ4Y2Q0ODVkNDhmZWFiNTAxMjVhZWZjYzEzMWMxNTAyYzkyIn0=','2018-10-17 05:21:13.174591'),('vzhbnv88tc44dwknq4z2ojv2a635hdxj','NjhiNWIxYmQxNTA4MTI5MjdjMmMzMGY3YzA4Mjk1NDUxMTc0NTNkMjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZDhkZGM1ZThhZTViNTlkNjRiNDA4NWMzNzNjZjZhMWE5MGMyZTZmIn0=','2018-10-17 20:10:47.101291'),('ylkljzz3rsprrtgwxi3dg5h7z6qha3gw','ZmJkNDhiYjYzNmJjMjQ4MzZiOTQ1MzIyMmQxOTJiNGEzMmI5OTY0Yzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhYmU3MWRiZDM5NjhiNzI5ZmI1MzFiYTZlMGI4NmM4YmU3ZGE5N2IyIn0=','2018-12-04 22:42:07.028072'),('zmnltutgwgo5wig53o55zla9h2smpdt7','NjkyYzQzYjg2MGY5YjMwNmYyYTBlNjc1ZjU2ZWJkMTlhNTU3NWM3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiODg3MjY4YzYyNjQ2MDIzNmY3OGM1NWIzNmJkZDIxZDMxNmVjZGZkMCJ9','2018-11-09 22:42:38.463342');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_mensagem`
--

DROP TABLE IF EXISTS `mysite_mensagem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_mensagem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pergunta` longtext NOT NULL,
  `pergunta_datetime` datetime(6) NOT NULL,
  `resposta` longtext,
  `resposta_datetime` datetime(6) DEFAULT NULL,
  `republica_id` int(11) NOT NULL,
  `usuario_pergunta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mysite_mensagem_republica_id_220d292a_fk_mysite_republica_id` (`republica_id`),
  KEY `mysite_mensagem_usuario_pergunta_id_1dd7ad2e_fk_mysite_us` (`usuario_pergunta_id`),
  CONSTRAINT `mysite_mensagem_republica_id_220d292a_fk_mysite_republica_id` FOREIGN KEY (`republica_id`) REFERENCES `mysite_republica` (`id`),
  CONSTRAINT `mysite_mensagem_usuario_pergunta_id_1dd7ad2e_fk_mysite_us` FOREIGN KEY (`usuario_pergunta_id`) REFERENCES `mysite_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_mensagem`
--

LOCK TABLES `mysite_mensagem` WRITE;
/*!40000 ALTER TABLE `mysite_mensagem` DISABLE KEYS */;
INSERT INTO `mysite_mensagem` VALUES (1,'cu','2018-11-20 19:51:30.375550','A vai toma no cu','2018-11-20 22:26:06.472925',15,4),(2,'vai toma no cu vc','2018-11-20 22:49:15.131138','Ta me tirando caralho\r\n','2018-11-20 22:49:46.735114',15,4),(3,'Seu viado \r\nflw','2018-11-20 22:51:59.809244',NULL,NULL,15,4),(4,'Viado é rolimã...como vc e sua irmã','2018-11-20 22:56:10.510418',NULL,NULL,15,4),(5,'bosta\r\n','2018-11-22 16:39:09.764896',NULL,NULL,14,4);
/*!40000 ALTER TABLE `mysite_mensagem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_republica`
--

DROP TABLE IF EXISTS `mysite_republica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_republica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `qtd_vagas` int(10) unsigned NOT NULL,
  `tipo_imovel` varchar(20) NOT NULL,
  `imagens` varchar(100) NOT NULL,
  `data_registro` date NOT NULL,
  `latitude` decimal(30,20) NOT NULL,
  `longitude` decimal(30,20) NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `comentarios` varchar(1000) DEFAULT NULL,
  `mensagem` longtext,
  `user_id` int(11) DEFAULT NULL,
  `rep_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mysite_republica_user_id_1e76132a_fk_mysite_usuario_id` (`user_id`),
  KEY `mysite_republica_slug_4187e4a3` (`slug`),
  CONSTRAINT `mysite_republica_user_id_1e76132a_fk_mysite_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `mysite_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_republica`
--

LOCK TABLES `mysite_republica` WRITE;
/*!40000 ALTER TABLE `mysite_republica` DISABLE KEYS */;
INSERT INTO `mysite_republica` VALUES (14,'Republica bresser','repbresser@gmail.com','Rua Bresser, 220 - Brás, São Paulo - SP, Brasil','','M',10,'CS','media/imagens/cod-94-projetos_de_casas_modelo_001.webp','2018-10-26',-23.53363960000000000000,-46.61280740000001000000,720.00,NULL,NULL,12,NULL),(15,'Republica da USJT','republica@qualquer.com','Rua Taquari, 20 - Mooca, São Paulo - SP, Brasil','fddffd','M',4,'AP','media/imagens/Captura_de_tela_de_2018-09-13_15-27-45_U3M6CHI.png','2018-10-26',-23.55308700000000000000,-46.59971799999999600000,300.00,NULL,NULL,14,NULL);
/*!40000 ALTER TABLE `mysite_republica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_usuario`
--

DROP TABLE IF EXISTS `mysite_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `endereco` varchar(255) NOT NULL,
  `mensagem` longtext,
  `cidade` varchar(255) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `telefone` varchar(15) NOT NULL,
  `rg` varchar(11) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `tipo_acesso` varchar(1) NOT NULL,
  `imagem` varchar(100) DEFAULT NULL,
  `data_registro` date NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_usuario`
--

LOCK TABLES `mysite_usuario` WRITE;
/*!40000 ALTER TABLE `mysite_usuario` DISABLE KEYS */;
INSERT INTO `mysite_usuario` VALUES (3,'pbkdf2_sha256$120000$5zMIwBhKJjAF$s9xxqOZdimttsN3bK2yIojn7ZRs/S2Fgz9brDyaysEo=','2018-10-07 18:35:08.286194',0,'guilherme','','',0,1,'2018-10-07 18:35:06.951998','','Rua taquaro, 33 mooca',NULL,'são Paulo','SP','25062581','000000000','00000000000','M','E','','2018-10-07','aluno@usjt.br'),(4,'pbkdf2_sha256$120000$qeo1XVKAOQuE$yRHw+o0ZvCtUpgG4kZgkacLnyIDQepcR8xJBSeTQ71Q=','2018-11-22 16:38:47.020874',0,'luisgtorrano','','',0,1,'2018-10-07 18:38:39.150247','','Rua tarquari, 33, mooca city',NULL,'São Paulo','SP','00000000','000000000','00000000000','M','E','','2018-10-07','aluno@usjt.co.br'),(5,'pbkdf2_sha256$120000$VExysx9PMpzQ$W1lk2l1dn61F0pyqdyFn105/nZnGS8+pkxjv+n8Ev0o=','2018-10-07 18:48:42.735507',0,'torranoluis','','',0,1,'2018-10-07 18:40:29.468945','','rua ibitirama 33',NULL,'São Acre','AL','00000000','000000000','00000000000','M','E','','2018-10-07','t@usjt.br'),(6,'pbkdf2_sha256$120000$Do7FYhoaq4ad$w1/HmCCKyLiL+hMxPfM6EEr5dfH489zRxXlCvcONd20=','2018-10-07 18:42:07.836083',0,'tooranoluis','','',0,1,'2018-10-07 18:42:06.692460','','Rua taraqua, 33 - mooca',NULL,'São PAulo','SP','00000000','000000000','00000000000','M','E','','2018-10-07','tl@uskt.br'),(7,'pbkdf2_sha256$120000$0axap6EyKXbS$U/UGtB9oIe7wyvgQC18IzmE40uImB1Dhn8ka2X3aRec=','2018-10-10 00:24:00.537006',0,'torrano123','','',0,1,'2018-10-10 00:23:59.802976','','Rua tarquari, 33, mooca city',NULL,'são Paulo','AC','00000000','000000000','00000000000','M','P','','2018-10-09','ltorrano@ltorrnao.com'),(8,'pbkdf2_sha256$120000$i2kmLckJMkeK$oU7KuCldf3Mn9spcF3oJ2/hSdj3i4sh+PKLNHs6b9Ng=','2018-10-16 00:51:24.910941',0,'testimage','','',0,1,'2018-10-16 00:51:17.712715','','Rua da mooca, 3000',NULL,NULL,NULL,'22222222','000000000','00000000000','M','E','','2018-10-15','gui@usjt.brr'),(9,'pbkdf2_sha256$120000$cUg2BytLpmIx$iEFJOzu6FKGTJpeqHzBBexgxjkE4bZLBiAMXRSIX6E8=','2018-10-16 00:58:49.138508',0,'testee','','',0,1,'2018-10-16 00:58:44.210045','','rua luos,33',NULL,NULL,NULL,'00000000','000000000','00000000000','M','P','imagens/Fundo_GxFOHaR_dV0Armg.png','2018-10-15','aluno2@hota.com'),(10,'pbkdf2_sha256$120000$asm09GCkjSZq$9+O0Al0AJpK501RgG2PzkqCprpr8oBfszQgLmjBeyH0=','2018-10-16 15:59:20.799823',0,'usertest','','',0,1,'2018-10-16 15:59:03.163058','Luisssss','Rua lalala, 3333',NULL,NULL,NULL,'00000000','000000000','00000000000','F','P','imagens/Captura_de_tela_de_2018-09-25_13-33-31_ASMBF4v.png','2018-10-16','gui@usjt.br'),(11,'pbkdf2_sha256$120000$UHQVSeluvIti$ehMPdxmIAe60wqgOCyM2jKdsaVN2++EQiMxHZ5NiVpg=','2018-10-23 00:22:15.413676',0,'viniciusdaniel','','',0,1,'2018-10-23 00:22:14.281375','Vinicius Daniel Carvalho','rua amparo, 300',NULL,NULL,NULL,'3333-3333','000000000','43747278841','O','P','imagens/Captura_de_tela_de_2018-10-02_15-11-02.png','2018-10-22','vinicius_danizinho@bol.com.br'),(12,'pbkdf2_sha256$120000$1DWh8jc8gSYI$EZ/yKt6Yjw4aPhzYjNMFvf7bjBKRfm9fRFWiS+r0Mfo=','2018-10-26 23:33:37.563167',0,'ltorrano','','',0,1,'2018-10-26 11:32:22.112560','Luis Guilherme Torrano','rua ibitirama, 2051 - vila prudente',NULL,NULL,NULL,'1122023535','502792001','43747278841','M','P','imagens/Captura_de_tela_de_2018-09-27_23-49-56.png','2018-10-26','guiilherme.t36@gmail.com'),(13,'pbkdf2_sha256$120000$88EdS12eUXXm$YjdZZ8b8jGDiNuEQn3hVOKmR5JnWOaeUW+jej+w249E=','2018-10-26 21:03:12.233904',0,'luistorrano','','',0,1,'2018-10-26 21:03:11.293828','Luis Torrano','av paes de barros 2000',NULL,NULL,NULL,'983403131','502803980','38472283994','M','E','imagens/Fundo_HbDOdR3.png','2018-10-26','luistorrano@gmail.com'),(14,'pbkdf2_sha256$120000$l3cxRC7Beuh1$ZVmfQ5utHzxbPxU6aQH1PiV2YsPrGynQ8H8O2rISDPY=','2018-11-20 22:41:12.399312',1,'gabriel','','',1,1,'2018-11-19 13:26:59.924703','','',NULL,NULL,NULL,'','','','','P','','2018-11-19','gabrielmeinbergreno@gmail.com');
/*!40000 ALTER TABLE `mysite_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_usuario_groups`
--

DROP TABLE IF EXISTS `mysite_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_usuario_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mysite_usuario_groups_usuario_id_group_id_4de5886b_uniq` (`usuario_id`,`group_id`),
  KEY `mysite_usuario_groups_group_id_81e200e5_fk_auth_group_id` (`group_id`),
  CONSTRAINT `mysite_usuario_groups_group_id_81e200e5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `mysite_usuario_groups_usuario_id_02a0a551_fk_mysite_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `mysite_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_usuario_groups`
--

LOCK TABLES `mysite_usuario_groups` WRITE;
/*!40000 ALTER TABLE `mysite_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `mysite_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysite_usuario_user_permissions`
--

DROP TABLE IF EXISTS `mysite_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysite_usuario_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mysite_usuario_user_perm_usuario_id_permission_id_19aa951f_uniq` (`usuario_id`,`permission_id`),
  KEY `mysite_usuario_user__permission_id_0d615d25_fk_auth_perm` (`permission_id`),
  CONSTRAINT `mysite_usuario_user__permission_id_0d615d25_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `mysite_usuario_user__usuario_id_4b6b26f0_fk_mysite_us` FOREIGN KEY (`usuario_id`) REFERENCES `mysite_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysite_usuario_user_permissions`
--

LOCK TABLES `mysite_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `mysite_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `mysite_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-26  9:38:46
