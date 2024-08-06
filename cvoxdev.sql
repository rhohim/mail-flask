-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2022 at 12:36 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cvoxdev`
--

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE `info` (
  `U_Id` int(10) UNSIGNED NOT NULL,
  `UserId` varchar(255) DEFAULT NULL,
  `UserPassword` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`U_Id`, `UserId`, `UserPassword`) VALUES
(4, 'noreply@cretivox.com', '$2b$12$V12PtpIbH4L400FZhsm48.QenSCV/oph7LW32qbDjwrOvcaXPjt62'),
(5, 'getpc2022@gmail.com', 'bWluaW1hbDg='),
(6, 'cretivox.web@gmail.com', 'QWt1NjY0MzI5Iw==');

-- --------------------------------------------------------

--
-- Table structure for table `usernameandpassworddemo`
--

CREATE TABLE `usernameandpassworddemo` (
  `U_Id` int(10) UNSIGNED NOT NULL,
  `UserId` varchar(255) DEFAULT NULL,
  `UserPassword` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usernameandpassworddemo`
--

INSERT INTO `usernameandpassworddemo` (`U_Id`, `UserId`, `UserPassword`) VALUES
(1, 'getpc2022@gmail.com', '99d56572d55a95c22fc6dc8fee6635be');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`U_Id`),
  ADD UNIQUE KEY `UserId` (`UserId`);

--
-- Indexes for table `usernameandpassworddemo`
--
ALTER TABLE `usernameandpassworddemo`
  ADD PRIMARY KEY (`U_Id`),
  ADD UNIQUE KEY `UserId` (`UserId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `info`
--
ALTER TABLE `info`
  MODIFY `U_Id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `usernameandpassworddemo`
--
ALTER TABLE `usernameandpassworddemo`
  MODIFY `U_Id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
