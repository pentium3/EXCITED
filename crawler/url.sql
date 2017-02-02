create database url;

use url;

/*
Navicat MySQL Data Transfer

Source Server         : 192.168.100.102_3306
Source Server Version : 50717
Source Host           : 192.168.100.102:3306
Source Database       : url

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-01-29 21:52:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `graphtable`
-- ----------------------------
DROP TABLE IF EXISTS `graphtable`;
CREATE TABLE `graphtable` (
  `uh` char(16) NOT NULL,
  `uid` char(16) NOT NULL,
  `nout` int(11) NOT NULL,
  `nin` int(11) NOT NULL,
  PRIMARY KEY (`uh`),
  UNIQUE KEY `uh` (`uh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of graphtable
-- ----------------------------

-- ----------------------------
-- Table structure for `lnktable`
-- ----------------------------
DROP TABLE IF EXISTS `lnktable`;
CREATE TABLE `lnktable` (
  `fid` char(16) NOT NULL,
  `sid` char(16) NOT NULL,
  PRIMARY KEY (`fid`,`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of lnktable
-- ----------------------------

-- ----------------------------
-- Table structure for `urltable`
-- ----------------------------
DROP TABLE IF EXISTS `urltable`;
CREATE TABLE `urltable` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `url` text NOT NULL,
  `uh` char(16) NOT NULL,
  PRIMARY KEY (`uid`,`uh`),
  UNIQUE KEY `uh` (`uh`),
  UNIQUE KEY `uid_UNIQUE` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1600 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of urltable
-- ----------------------------
