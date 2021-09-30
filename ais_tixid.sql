-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 30, 2021 at 05:37 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

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
  `id_bioskop` int(11) NOT NULL,
  `nama` varchar(80) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `id` int(11) NOT NULL,
  `judul` varchar(80) NOT NULL,
  `keterangan` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `jadwal`
--

CREATE TABLE `jadwal` (
  `id_jadwal` int(11) NOT NULL,
  `id_film` int(11) NOT NULL,
  `id_bioskop` int(11) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_bioskop` int(11) NOT NULL,
  `id_film` int(11) NOT NULL,
  `id_jadwal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
-- Indexes for dumped tables
--

--
-- Indexes for table `bioskop`
--
ALTER TABLE `bioskop`
  ADD PRIMARY KEY (`id_bioskop`);

<<<<<<< HEAD
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

=======
--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`id_jadwal`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`);

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
  MODIFY `id_bioskop` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `id_jadwal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT;
>>>>>>> e6f8f6ce8b61775c1a5f76082bc4425483603160
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
