CREATE TABLE `facebase` (
  `id` int(11) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `nis&nim` varchar(30) NOT NULL,
  `absensi` datetime DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `facebase` (`id`, `nama`, `nis&nim`, `absensi`) VALUES
(1, 'Ilham Idfiana', '6702184010', '');