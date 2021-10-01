-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2021 at 06:07 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ais_tixid`
--

-- --------------------------------------------------------

--
-- Table structure for table `bioskop`
--

CREATE TABLE `bioskop` (
  `id_bioskop` int(3) NOT NULL,
  `nama_bioskop` varchar(64) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bioskop`
--

INSERT INTO `bioskop` (`id_bioskop`, `nama_bioskop`, `harga`) VALUES
(1, 'San Jacinto', 28000),
(2, 'Szombathely', 50500),
(3, 'Jaguimitan', 30000),
(4, 'Sinanju', 47500),
(5, 'Båstad', 27500),
(6, 'Chengjiao Chengguanzhen', 57000),
(7, 'Göteborg', 47000),
(8, 'Shengli', 31000),
(9, 'Delong', 26500),
(10, 'Soito', 48500),
(11, 'Volodars’k-Volyns’kyy', 53000),
(12, 'Sergiyev Posad', 55000),
(13, 'Rechka', 59500),
(14, 'Cabricán', 35500),
(15, 'Dagsar', 45000),
(16, 'Annecy', 53500),
(17, 'Gwio Kura', 37500),
(18, 'Morrelgonj', 33500),
(19, 'Stony Hill', 50500),
(20, 'Chenxiang', 48000),
(21, 'Volgorechensk', 34000),
(22, 'Portëz', 44000),
(23, 'Wuyang', 40000),
(24, 'Gotemba', 26000),
(25, 'Oum Hadjer', 25000);

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `id_film` int(3) NOT NULL,
  `judul` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id_film`, `judul`) VALUES
(1, 'Last Time I Saw Paris, The'),
(2, 'Storm Warning'),
(3, 'Superman/Batman: Apocalypse'),
(4, 'Julius Caesar'),
(5, 'Zombeavers'),
(6, 'Shoppen '),
(7, 'Critters 3'),
(8, 'Bungee Jumping of Their Own (Beonjijeompeureul hada)'),
(9, 'Not Forgotten'),
(10, 'Hidden Agenda'),
(11, 'About a Boy'),
(12, 'Breaking In'),
(13, 'Snow Dogs'),
(14, 'Strait-Jacket'),
(15, 'Tokyo Joe'),
(16, 'Good Will Hunting'),
(17, 'Surrender, Dorothy'),
(18, 'Ghidorah, the Three-Headed Monster (San daikaijû: Chikyû saidai '),
(19, 'Flodder in Amerika!'),
(20, 'Don\'t Go Breaking My Heart (Daan gyun naam yu)'),
(21, 'Smiling Lieutenant, The'),
(22, 'Good bye, Lenin!'),
(23, 'Child Is Waiting, A'),
(24, 'Unholy Three, The'),
(25, 'Wristcutters: A Love Story');

-- --------------------------------------------------------

--
-- Table structure for table `tiket`
--

CREATE TABLE `tiket` (
  `id_film` int(3) NOT NULL,
  `id_bioskop` int(3) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiket`
--

INSERT INTO `tiket` (`id_film`, `id_bioskop`, `tanggal`) VALUES
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

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `telepon` varchar(12) NOT NULL,
  `nama` varchar(144) NOT NULL,
  `dana_status` int(11) NOT NULL DEFAULT 0
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`telepon`, `nama`, `dana_status`) VALUES
('08123456789', 'dummy', 1),
('123', 'Dava', 1),
('321', 'Dida tixID', 1),
('1234', 'Dava Aditya Jauhar', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bioskop`
--
ALTER TABLE `bioskop`
  ADD PRIMARY KEY (`id_bioskop`);

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id_film`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`telepon`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bioskop`
--
ALTER TABLE `bioskop`
  MODIFY `id_bioskop` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `id_film` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
