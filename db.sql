/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - vitamin
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`vitamin` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `vitamin`;

/*Table structure for table `food` */

DROP TABLE IF EXISTS `food`;

CREATE TABLE `food` (
  `vitamin` varchar(100) DEFAULT NULL,
  `food` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `result` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `food` */

insert  into `food`(`vitamin`,`food`,`image`,`result`) values ('vita','orange','orange.jpg','1'),('vitb','apple','apple.jpg','1');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`username`,`password`,`email`,`mobile`,`address`) values (3,'chotu','123','moulalicce225@gmail.com','+918639966858','15-8-424');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `username` varchar(100) DEFAULT NULL,
  `vita` varchar(100) DEFAULT NULL,
  `vitb` varchar(100) DEFAULT NULL,
  `vitc` varchar(100) DEFAULT NULL,
  `vitd` varchar(100) DEFAULT NULL,
  `vite` varchar(100) DEFAULT NULL,
  UNIQUE KEY `id` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`username`,`vita`,`vitb`,`vitc`,`vitd`,`vite`) values ('chotu','1','0','1','0','1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
