-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS sistema_gestion_may CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

USE sistema_gestion_may;

-- Tabla unit_types
CREATE TABLE `unit_types` (
  `Unit_id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) NOT NULL,
  `Symbol` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Unit_id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla category
CREATE TABLE `category` (
  `Category_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `is_perishable` tinyint(1) NOT NULL DEFAULT '0',
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Category_ID`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla brands
CREATE TABLE `brands` (
  `Brand_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Brand_ID`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla products
CREATE TABLE `products` (
  `Product_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Stock` int DEFAULT '0',
  `Price` decimal(10,2) NOT NULL,
  `Cost` decimal(10,2) NOT NULL,
  `Category_ID` int DEFAULT NULL,
  `Min_Stock` int DEFAULT '0',
  `Barcode` varchar(50) DEFAULT NULL,
  `Is_Active` tinyint(1) DEFAULT '1',
  `Expiration_Date` date DEFAULT NULL,
  `Unit_Id` int NOT NULL DEFAULT '1' COMMENT '1 = unidad (valor por defecto)',
  PRIMARY KEY (`Product_ID`),
  UNIQUE KEY `Barcode` (`Barcode`),
  KEY `Category_ID` (`Category_ID`),
  KEY `fk_product_unit` (`Unit_Id`),
  CONSTRAINT `fk_product_unit` FOREIGN KEY (`Unit_Id`) REFERENCES `unit_types` (`Unit_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`Category_ID`) REFERENCES `category` (`Category_ID`),
  CONSTRAINT `chk_stock` CHECK ((`Stock` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla brands_products
CREATE TABLE `brands_products` (
  `Product_ID` int NOT NULL,
  `Brand_ID` int NOT NULL,
  PRIMARY KEY (`Product_ID`,`Brand_ID`),
  KEY `Brand_ID` (`Brand_ID`),
  CONSTRAINT `brands_products_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`),
  CONSTRAINT `brands_products_ibfk_2` FOREIGN KEY (`Brand_ID`) REFERENCES `brands` (`Brand_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla clients
CREATE TABLE `clients` (
  `Client_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Client_ID`),
  UNIQUE KEY `Phone` (`Phone`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla payment_methods
CREATE TABLE `payment_methods` (
  `Payment_Method_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Payment_Method_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla suppliers
CREATE TABLE `suppliers` (
  `Supplier_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Supplier_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla purchases
CREATE TABLE `purchases` (
  `Purchase_ID` int NOT NULL AUTO_INCREMENT,
  `Supplier_ID` int DEFAULT NULL,
  `Date` datetime NOT NULL,
  `Total` decimal(10,2) NOT NULL,
  `Payment_Method_ID` int DEFAULT NULL,
  PRIMARY KEY (`Purchase_ID`),
  KEY `Supplier_ID` (`Supplier_ID`),
  KEY `Payment_Method_ID` (`Payment_Method_ID`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`Supplier_ID`) REFERENCES `suppliers` (`Supplier_ID`),
  CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`Payment_Method_ID`) REFERENCES `payment_methods` (`Payment_Method_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla purchase_details
CREATE TABLE `purchase_details` (
  `Purchase_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  `Quantity` decimal(10,2) NOT NULL,
  `Subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`Purchase_ID`,`Product_ID`),
  KEY `Product_ID` (`Product_ID`),
  CONSTRAINT `purchase_details_ibfk_1` FOREIGN KEY (`Purchase_ID`) REFERENCES `purchases` (`Purchase_ID`),
  CONSTRAINT `purchase_details_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla sales
CREATE TABLE `sales` (
  `Sale_ID` int NOT NULL AUTO_INCREMENT,
  `Date_Of_Purchase` datetime NOT NULL,
  `Client_ID` int DEFAULT NULL,
  `Total` decimal(10,2) NOT NULL,
  `Payment_Method_ID` int DEFAULT NULL,
  `Sale_Type` enum('minorista','mayorista') DEFAULT 'minorista',
  `Discount` decimal(5,2) DEFAULT '0.00',
  `Status` enum('pendiente','completada','cancelada') DEFAULT 'completada',
  PRIMARY KEY (`Sale_ID`),
  KEY `Client_ID` (`Client_ID`),
  KEY `Payment_Method_ID` (`Payment_Method_ID`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`Client_ID`) REFERENCES `clients` (`Client_ID`),
  CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`Payment_Method_ID`) REFERENCES `payment_methods` (`Payment_Method_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla sale_details
CREATE TABLE `sale_details` (
  `Sale_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  `Quantity` decimal(10,2) NOT NULL,
  `Subtotal` decimal(10,2) NOT NULL,
  PRIMARY KEY (`Sale_ID`,`Product_ID`),
  KEY `Product_ID` (`Product_ID`),
  CONSTRAINT `sale_details_ibfk_1` FOREIGN KEY (`Sale_ID`) REFERENCES `sales` (`Sale_ID`),
  CONSTRAINT `sale_details_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla stock_movements
CREATE TABLE `stock_movements` (
  `Movement_ID` int NOT NULL AUTO_INCREMENT,
  `Quantity` decimal(10,2) NOT NULL,
  `Type` enum('Ingreso','Salida','Ajuste') NOT NULL,
  `Date` datetime NOT NULL,
  `Reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Movement_ID`),
  CONSTRAINT `chk_quantity` CHECK ((`Quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla stock_movement_details
CREATE TABLE `stock_movement_details` (
  `Movement_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  `Quantity` decimal(10,2) NOT NULL,
  PRIMARY KEY (`Movement_ID`,`Product_ID`),
  KEY `Product_ID` (`Product_ID`),
  CONSTRAINT `stock_movement_details_ibfk_1` FOREIGN KEY (`Movement_ID`) REFERENCES `stock_movements` (`Movement_ID`),
  CONSTRAINT `stock_movement_details_ibfk_2` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Datos iniciales para unit_types
INSERT INTO `unit_types` (`Unit_id`, `Name`, `Symbol`) VALUES
(1, 'unidad', 'ud'),
(2, 'kilogramo', 'kg'),
(3, 'gramo', 'g'),
(4, 'litro', 'L'),
(5, 'mililitro', 'ml'),
(6, 'paquete', 'pqte');

-- Datos iniciales para category
INSERT INTO `category` (`Category_ID`, `Name`, `is_perishable`, `description`) VALUES
(14, 'Verduras y Frutas', 1, 'Productos frescos de temporada'),
(15, 'Panificados', 1, 'Pan, facturas, galletitas, harinas'),
(16, 'Alimentos envasados', 0, 'Arroz, fideos, latas, conservas'),
(17, 'Lácteos', 1, 'Leche, yogures, quesos, manteca'),
(18, 'Golosinas', 0, 'Caramelos, chicles, chocolates'),
(19, 'Snacks', 0, 'Papas fritas, palitos, maní'),
(20, 'Fiambres', 1, 'Jamón, salame, queso en fetas'),
(21, 'Bebidas', 0, 'Gaseosas, aguas, jugos, cervezas'),
(22, 'Limpieza', 0, 'Detergentes, lavandinas, aromatizantes'),
(23, 'Congelados', 1, 'Helados, vegetales congelados'),
(24, 'Perfumería', 0, 'Jabones, shampoo, pasta dental'),
(25, 'Abarrotes', 0, 'Aceites, vinagres, especias'),
(26, 'Mascotas', 0, 'Alimento para perros/gatos'),
(27, 'Electro', 0, 'Pilas, bombillas, cables'),
(28, 'Bazar', 0, 'Vajilla, cubiertos, contenedores'),
(29, 'Tabaco', 0, 'Cigarrillos, picadillo'),
(30, 'Libretería', 0, 'Cuadernos, lápices, cartucheras');

-- Datos iniciales para payment_methods
INSERT INTO `payment_methods` (`Payment_Method_ID`, `Name`, `Description`) VALUES
(1, 'Efectivo', 'Pago en efectivo'),
(2, 'Débito', 'Tarjeta de débito bancaria'),
(3, 'Crédito', 'Tarjeta de crédito bancaria'),
(4, 'Transferencia', 'Transferencia bancaria'),
(5, 'Mercado Pago QR', 'Pago a través de Mercado Pago Codigo QR'),
(6, 'Mercado Pago Transferencia', 'Pago a través de Mercado Pago con CBU o ALIAS'),
(7, 'Cuenta DNI QR', 'Pago digital con QR'),
(8, 'Cuenta DNI Transferencia', 'Pago digital con DNI, CBU ó ALIAS');

-- Datos iniciales para brands
INSERT INTO `brands` (`Brand_ID`, `Name`, `Description`) VALUES
(7, 'Coca Cola', 'Marca lider'),
(8, 'Pepsi', '');

-- Datos iniciales para products
INSERT INTO `products` (`Product_ID`, `Name`, `Stock`, `Price`, `Cost`, `Category_ID`, `Min_Stock`, `Barcode`, `Is_Active`, `Expiration_Date`, `Unit_Id`) VALUES
(6, 'Gaseosa', 12, 2500.00, 2000.00, 21, 0, NULL, 1, '2025-04-06', 1),
(7, 'Gaseosa', 5, 2600.00, 3000.00, 21, 20, NULL, 1, '2025-05-10', 1);

-- Datos iniciales para brands_products
INSERT INTO `brands_products` (`Product_ID`, `Brand_ID`) VALUES
(6, 7),
(7, 8);