-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS hoteles;
USE hoteles;

-- Eliminar tablas existentes
DROP TABLE IF EXISTS habitacion_servicio;
DROP TABLE IF EXISTS hotel_servicio;
DROP TABLE IF EXISTS reserva_servicios;
DROP TABLE IF EXISTS reserva;
DROP TABLE IF EXISTS servicios;
DROP TABLE IF EXISTS habitaciones;
DROP TABLE IF EXISTS hotel;

-- Crear tablas
CREATE TABLE hotel (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre TEXT,
  direccion TEXT,
  descripcion TEXT,
  url_img TEXT, 
  region TEXT
);

CREATE TABLE habitaciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_hotel INT,
  numero INT,
  url_img TEXT,
  tipo TEXT,
  precio INT,
  FOREIGN KEY (id_hotel) REFERENCES hotel(id)
);

CREATE TABLE servicios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  servicio TEXT,
  tipo TEXT
);

CREATE TABLE reserva (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_habitacion INT,
  FOREIGN KEY (id_habitacion) REFERENCES habitaciones(id),
  llegada DATE,
  salida DATE,
  cliente_apellido TEXT,
  estado TEXT,
  precio INT,
  fecha_cancelacion DATE
);

CREATE TABLE reserva_servicios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_reserva INT,
  id_servicio INT,
  estado TEXT,
  precio INT,
  FOREIGN KEY (id_reserva) REFERENCES reserva(id),
  FOREIGN KEY (id_servicio) REFERENCES servicios(id)
);

CREATE TABLE hotel_servicio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_hotel INT,
  id_servicio INT,
  precio INT,
  FOREIGN KEY (id_hotel) REFERENCES hotel(id),
  FOREIGN KEY (id_servicio) REFERENCES servicios(id)
);

CREATE TABLE habitacion_servicio (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_habitacion INT,
  id_servicio INT,
  precio INT,
  FOREIGN KEY (id_habitacion) REFERENCES habitaciones(id),
  FOREIGN KEY (id_servicio) REFERENCES servicios(id)
);

-- Insertar datos
INSERT INTO hotel
  (nombre, direccion, descripcion, region, url_img)
VALUES
  ('Hotel Sol', '123 Calle Principal, Ciudad', 'Ubicado en el corazón de la vibrante capital, nuestro hotel ofrece un oasis de tranquilidad en medio del bullicio urbano. Ideal para viajeros de negocios y turistas por igual.', 'Buenos Aires', 'static/assets/hotel-buenos-aire.jpg'),
  ('Hotel Luna', '456 Avenida Central, Ciudad', 'Perfecto para quienes buscan la combinación ideal de playa y ciudad. Disfrute del sol, la arena y las actividades culturales que esta hermosa ciudad costera tiene para ofrecer.', 'Mar del Plata', 'static/assets/hotel-mar-del-plata.jpg'),
  ('Hotel Estrella', '789 Calle Norte, Ciudad', 'Situado en el pintoresco escenario de la Patagonia, este hotel es ideal para los amantes de la naturaleza y los deportes de invierno. Disfrute de vistas impresionantes, actividades al aire libre y la hospitalidad cálida de siempre.', 'Bariloche', 'static/assets/hotel-bariloche.jpg'); 

INSERT INTO habitaciones
  (id_hotel, numero, tipo, precio)
VALUES
  (1, 101, 'Suite', 150),
  (1, 102, 'Doble', 100),
  (1, 103, 'Individual', 75),
  (2, 201, 'Suite', 120),
  (2, 202, 'Doble', 85),
  (3, 301, 'Suite', 200),
  (3, 302, 'Individual', 90);

INSERT INTO servicios
  (servicio, tipo) 
VALUES
  ('WiFi', 'Conectividad'),
  ('Desayuno', 'Alimentación'),
  ('Gimnasio', 'Entretenimiento'),
  ('Spa', 'Relajación'),
  ('Piscina', 'Entretenimiento');

INSERT INTO hotel_servicio
  (id_hotel, id_servicio, precio)
VALUES
  (1, 1, 0),
  (1, 2, 15),
  (1, 3, 20),
  (2, 1, 0),
  (2, 2, 10),
  (3, 1, 0),
  (3, 4, 50),
  (3, 5, 30);

INSERT INTO habitacion_servicio
  (id_habitacion, id_servicio, precio)
VALUES
  (1, 1, 0),
  (1, 4, 45),
  (2, 1, 0),
  (2, 2, 15),
  (5, 2, 10),
  (6, 3, 25),
  (6, 5, 20);
