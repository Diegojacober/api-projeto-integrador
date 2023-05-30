-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.0.30 - MySQL Community Server - GPL
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando dados para a tabela integrador.cars: ~3 rows (aproximadamente)
INSERT INTO `cars` (`id`, `name`, `description`, `combustivel`, `cambio`, `ano`, `url_image`, `valor`, `marca_id`, `categoria_id`) VALUES
	(1, 'BMW X6', 'Uma BMW bem legal', 'Flex', 'Automático', '2023', 'https://s2.glbimg.com/0E89TlGfUg21BMHx-VDYvpq4iBE=/0x0:1400x788/924x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2023/U/5/kMidWdTIAvJNonx1vUeQ/bmw-x6-m-competition-.jpg', 250000, 2, 1),
	(2, 'BMW Off Road', 'Uma BMw off road muito zia', 'Diesel', 'Automático', '2030', 'https://i.ytimg.com/vi/D72IzaVoETE/maxresdefault.jpg', 650000, 2, 2),
	(3, 'Porsche Carrera', 'Porsche carrera bem rápida', 'Gasolina', 'Automático', '2021', 'https://s2.glbimg.com/gqNT9DiXCHIPEHdCzC0WbVC0088=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_cf9d035bf26b4646b105bd958f32089d/internal_photos/bs/2020/i/d/dLzNHJRdADSKsnvPBFTw/2020-03-03-porsche-911-turbo-s-96.jpeg', 350000, 7, 1);

-- Copiando dados para a tabela integrador.categorias: ~3 rows (aproximadamente)
INSERT INTO `categorias` (`id`, `nome`) VALUES
	(1, 'Esportivos'),
	(2, 'Off Road'),
	(3, 'Blindados');

-- Copiando dados para a tabela integrador.marcas: ~8 rows (aproximadamente)
INSERT INTO `marcas` (`id`, `nome`) VALUES
	(1, 'Ferrari'),
	(2, 'BMW'),
	(3, 'Lamborghini'),
	(4, 'Land Rover'),
	(5, 'Jeep'),
	(6, 'Mercedes'),
	(7, 'Porsche'),
	(8, 'Audi');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
