-- phpMyAdmin SQL Dump
-- version 3.1.3.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 26-04-2017 a las 12:01:03
-- Versión del servidor: 5.1.33
-- Versión de PHP: 5.2.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `estacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE IF NOT EXISTS `factura` (
  `nombre` varchar(20) DEFAULT NULL,
  `identificacion` int(20) NOT NULL,
  `tipo_gasolina` varchar(20) NOT NULL,
  `cantidad` int(20) NOT NULL,
  `puntos` int(20) NOT NULL,
  `total` int(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `factura`
--

INSERT INTO `factura` (`nombre`, `identificacion`, `tipo_gasolina`, `cantidad`, `puntos`, `total`) VALUES
('0', 12344, 'extra', 200000, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gasolina`
--

CREATE TABLE IF NOT EXISTS `gasolina` (
  `id_gasolina` int(20) NOT NULL AUTO_INCREMENT,
  `nombre_gasolina` varchar(20) NOT NULL,
  `precio_gasolina` int(11) NOT NULL,
  PRIMARY KEY (`id_gasolina`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcar la base de datos para la tabla `gasolina`
--

INSERT INTO `gasolina` (`id_gasolina`, `nombre_gasolina`, `precio_gasolina`) VALUES
(1, 'extra', 120000),
(2, 'acpm', 210000),
(3, 'corriente', 15000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `nombre` varchar(20) DEFAULT NULL,
  `identificacion` int(20) NOT NULL,
  `puntos` int(20) NOT NULL,
  `correo` varchar(40) DEFAULT NULL,
  `contrasena` varchar(40) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcar la base de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`nombre`, `identificacion`, `puntos`, `correo`, `contrasena`) VALUES
('lina', 12344, 23, 'linita26gmail.com', '123'),
('fausto', 23344, 34, 'ayfgmail.com', '345'),
('lina', 12344, 0, NULL, NULL);
