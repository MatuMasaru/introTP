-- MySQL Script generated by MySQL Workbench
-- Tue Nov  5 12:36:48 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`sucursale`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`sucursale` (
  `id_sucursales` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `http` VARCHAR(45) NULL,
  PRIMARY KEY (`id_sucursales`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`habitaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`habitaciones` (
  `id_habiatcion` INT NOT NULL AUTO_INCREMENT,
  `piso` VARCHAR(45) NULL,
  `parte` VARCHAR(45) NULL,
  `tipo` VARCHAR(45) NULL,
  `precio` VARCHAR(45) NULL,
  `disposicion` VARCHAR(45) NULL,
  `personas` VARCHAR(45) NULL,
  `sucursale_id_sucursales` INT NOT NULL,
  PRIMARY KEY (`id_habiatcion`),
  INDEX `fk_habitaciones_sucursale1_idx` (`sucursale_id_sucursales` ASC) VISIBLE,
  CONSTRAINT `fk_habitaciones_sucursale1`
    FOREIGN KEY (`sucursale_id_sucursales`)
    REFERENCES `mydb`.`sucursale` (`id_sucursales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`conexion_reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`conexion_reserva` (
  `id` INT NOT NULL,
  `sucursale_id_sucursales` INT NOT NULL,
  `habitaciones_id_habiatcion` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_conexion_reserva_sucursale1_idx` (`sucursale_id_sucursales` ASC) VISIBLE,
  INDEX `fk_conexion_reserva_habitaciones1_idx` (`habitaciones_id_habiatcion` ASC) VISIBLE,
  CONSTRAINT `fk_conexion_reserva_sucursale1`
    FOREIGN KEY (`sucursale_id_sucursales`)
    REFERENCES `mydb`.`sucursale` (`id_sucursales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_conexion_reserva_habitaciones1`
    FOREIGN KEY (`habitaciones_id_habiatcion`)
    REFERENCES `mydb`.`habitaciones` (`id_habiatcion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`reservas` (
  `id_reserva` INT NOT NULL,
  `llegada` DATE NULL,
  `salida` DATE NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `fecha_cancelacion` DATE NULL,
  `conexion_reserva_id` INT NOT NULL,
  PRIMARY KEY (`id_reserva`),
  INDEX `fk_reservas_conexion_reserva1_idx` (`conexion_reserva_id` ASC) VISIBLE,
  CONSTRAINT `fk_reservas_conexion_reserva1`
    FOREIGN KEY (`conexion_reserva_id`)
    REFERENCES `mydb`.`conexion_reserva` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`servicios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`servicios` (
  `id_servicios` INT NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  `precio` VARCHAR(45) NULL,
  `tipo` VARCHAR(45) NULL,
  `sucursale_id_sucursales` INT NOT NULL,
  PRIMARY KEY (`id_servicios`),
  INDEX `fk_servicios_sucursale_idx` (`sucursale_id_sucursales` ASC) VISIBLE,
  CONSTRAINT `fk_servicios_sucursale`
    FOREIGN KEY (`sucursale_id_sucursales`)
    REFERENCES `mydb`.`sucursale` (`id_sucursales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
