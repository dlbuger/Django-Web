/*
 Navicat Premium Data Transfer

 Source Server         : 测试
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 09/01/2020 15:40:15
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 人工成本
-- ----------------------------
DROP TABLE IF EXISTS `人工成本`;
CREATE TABLE `人工成本` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `员工号` int(255) NOT NULL,
  `合同号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `预算人工` float(255,0) DEFAULT NULL,
  `实际人工` float(255,0) DEFAULT NULL,
  `修正1` float(255,0) DEFAULT NULL,
  `修正2` float(255,0) DEFAULT NULL,
  `修正3` float(255,0) DEFAULT NULL,
  PRIMARY KEY (`id`,`员工号`) USING BTREE,
  KEY `人工成本_员工号` (`员工号`),
  KEY `人工成本_合同号` (`合同号`),
  CONSTRAINT `人工成本_合同号` FOREIGN KEY (`合同号`) REFERENCES `项目` (`合同号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `人工成本_员工号` FOREIGN KEY (`员工号`) REFERENCES `员工` (`员工号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of 人工成本
-- ----------------------------
BEGIN;
INSERT INTO `人工成本` VALUES (1, 1, '123456', 30, 29, NULL, NULL, NULL);
INSERT INTO `人工成本` VALUES (2, 2, '123456', 30, 20, NULL, NULL, NULL);
INSERT INTO `人工成本` VALUES (3, 3, '523423', 60, 55, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for 员工
-- ----------------------------
DROP TABLE IF EXISTS `员工`;
CREATE TABLE `员工` (
  `员工号` int(255) NOT NULL,
  `姓名` varchar(255) DEFAULT NULL,
  `部门` varchar(255) DEFAULT NULL,
  `单位人工` float(255,0) DEFAULT NULL,
  PRIMARY KEY (`员工号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of 员工
-- ----------------------------
BEGIN;
INSERT INTO `员工` VALUES (1, '小王', '工程部', 300);
INSERT INTO `员工` VALUES (2, '小李', '工程部', 600);
INSERT INTO `员工` VALUES (3, '小曹', '软件部', 1000);
COMMIT;

-- ----------------------------
-- Table structure for 实际成本
-- ----------------------------
DROP TABLE IF EXISTS `实际成本`;
CREATE TABLE `实际成本` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `合同号` varchar(255) NOT NULL,
  `硬件成本` float(255,0) DEFAULT NULL,
  `软件成本` float(255,0) DEFAULT NULL,
  `差旅成本` float(255,0) DEFAULT NULL,
  `集成成本` float(255,0) DEFAULT NULL,
  `施工成本` float(255,0) DEFAULT NULL,
  PRIMARY KEY (`id`,`合同号`) USING BTREE,
  KEY `合同号` (`合同号`,`硬件成本`,`软件成本`,`差旅成本`,`集成成本`,`施工成本`),
  KEY `硬件成本` (`硬件成本`,`软件成本`,`差旅成本`,`集成成本`,`施工成本`),
  CONSTRAINT `实际成本_合同号` FOREIGN KEY (`合同号`) REFERENCES `项目` (`合同号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of 实际成本
-- ----------------------------
BEGIN;
INSERT INTO `实际成本` VALUES (2, '523423', 999, 5252, 224, 534, 345);
INSERT INTO `实际成本` VALUES (1, '123456', 2342, 53, 22, 242, 4242);
COMMIT;

-- ----------------------------
-- Table structure for 项目
-- ----------------------------
DROP TABLE IF EXISTS `项目`;
CREATE TABLE `项目` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `合同号` varchar(255) NOT NULL,
  `项目名称` varchar(255) DEFAULT NULL,
  `预计开始日期` date DEFAULT NULL,
  `预计结束日期` date DEFAULT NULL,
  `实际开始日期` date DEFAULT NULL,
  `实际结束日期` date DEFAULT NULL,
  PRIMARY KEY (`id`,`合同号`) USING BTREE,
  KEY `合同号` (`合同号`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of 项目
-- ----------------------------
BEGIN;
INSERT INTO `项目` VALUES (1, '123456', '运河', '2019-01-01', NULL, NULL, NULL);
INSERT INTO `项目` VALUES (2, '523423', '开天', '2020-01-01', NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for 预算成本
-- ----------------------------
DROP TABLE IF EXISTS `预算成本`;
CREATE TABLE `预算成本` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `合同号` varchar(255) NOT NULL,
  `硬件成本` float(255,0) DEFAULT NULL,
  `软件成本` float(255,0) DEFAULT NULL,
  `差旅成本` float(255,0) DEFAULT NULL,
  `集成成本` float(255,0) DEFAULT NULL,
  `施工成本` float(255,0) DEFAULT NULL,
  PRIMARY KEY (`id`,`合同号`) USING BTREE,
  KEY `合同号` (`合同号`,`硬件成本`,`软件成本`,`差旅成本`,`集成成本`,`施工成本`),
  KEY `硬件成本` (`硬件成本`,`软件成本`,`差旅成本`,`集成成本`,`施工成本`),
  CONSTRAINT `预算成本_合同号` FOREIGN KEY (`合同号`) REFERENCES `项目` (`合同号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- ----------------------------
-- Records of 预算成本
-- ----------------------------
BEGIN;
INSERT INTO `预算成本` VALUES (2, '523423', 23, 53453, 22, 452, 524);
INSERT INTO `预算成本` VALUES (3, 'as92423', 31, 1, 11, 22, 22);
INSERT INTO `预算成本` VALUES (1, '123456', 1321, 42342, 34314, 23423, 6546);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
