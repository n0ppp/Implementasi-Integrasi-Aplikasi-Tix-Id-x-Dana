-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 15, 2021 at 02:51 AM
-- Server version: 8.0.21
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `arsin_tixid`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `telepon` varchar(12) NOT NULL,
  `nama` varchar(144) NOT NULL,
  `dana_status` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`telepon`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`telepon`, `nama`, `dana_status`) VALUES
('08123456789', 'dummy', 1);

create table tiket (
	nama_bioskop VARCHAR(50),
	harga INT
);

insert into bioskop (nama_bioskop, harga) values
 ('San Jacinto', 28000),
 ('Szombathely', 50500),
 ('Jaguimitan', 30000),
 ('Sinanju', 47500),
 ('Båstad', 27500),
 ('Chengjiao Chengguanzhen', 57000),
 ('Göteborg', 47000),
 ('Shengli', 31000),
 ('Delong', 26500),
 ('Soito', 48500),
 ('Volodars’k-Volyns’kyy', 53000),
 ('Sergiyev Posad', 55000),
 ('Rechka', 59500),
 ('Cabricán', 35500),
 ('Dagsar', 45000),
 ('Annecy', 53500),
 ('Gwio Kura', 37500),
 ('Morrelgonj', 33500),
 ('Stony Hill', 50500),
 ('Chenxiang', 48000),
 ('Volgorechensk', 34000),
 ('Portëz', 44000),
 ('Wuyang', 40000),
 ('Gotemba', 26000),
 ('Oum Hadjer', 25000);


create table tiket (
	judul VARCHAR(50)
);

insert into film (judul) values
 ('Last Time I Saw Paris, The'),
 ('Storm Warning'),
 ('Superman/Batman: Apocalypse'),
 ('Julius Caesar'),
 ('Zombeavers'),
 ('Shoppen '),
 ('Critters 3'),
 ('Bungee Jumping of Their Own (Beonjijeompeureul hada)'),
 ('Not Forgotten'),
 ('Hidden Agenda'),
 ('About a Boy'),
 ('Breaking In'),
 ('Snow Dogs'),
 ('Strait-Jacket'),
 ('Tokyo Joe'),
 ('Good Will Hunting'),
 ('Surrender, Dorothy'),
 ('Ghidorah, the Three-Headed Monster (San daikaijû: Chikyû saidai no kessen)'),
 ('Flodder in Amerika!'),
 ('Don''t Go Breaking My Heart (Daan gyun naam yu)'),
 ('Smiling Lieutenant, The'),
 ('Good bye, Lenin!'),
 ('Child Is Waiting, A'),
 ('Unholy Three, The'),
 ('Wristcutters: A Love Story');

create table tiket (
	id_film INT,
	id_bioskop INT,
	tanggal DATE
);

insert into tiket (id_film, id_bioskop, tanggal) values
 (3, 5, '2021-09-17'),
 (7, 10, '2021-09-09'),
 (4, 7, '2021-09-27'),
 (8, 10, '2021-09-28'),
 (9, 4, '2021-09-11'),
 (1, 7, '2021-09-09'),
 (8, 5, '2021-09-04'),
 (5, 2, '2021-09-24'),
 (8, 5, '2021-09-13'),
 (2, 7, '2021-09-24'),
 (5, 6, '2021-09-29'),
 (7, 7, '2021-09-24'),
 (2, 2, '2021-09-10'),
 (5, 4, '2021-09-02'),
 (2, 7, '2021-09-03');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
