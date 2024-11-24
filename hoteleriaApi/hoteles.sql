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
    llegada DATE,
    salida DATE,
    cliente_apellido TEXT,
    estado TEXT,
    precio INT,
    fecha_cancelacion DATE,
    FOREIGN KEY (id_habitacion) REFERENCES habitaciones(id)
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
    (id_hotel, numero, tipo, precio, url_img)
VALUES
    -- Hotel 1
    (1, 101, 'Suite', 150, '/static/assets/habitacion_por_hotel/hotel1_suit.jpeg'),
    (1, 102, 'Doble', 100, '/static/assets/habitacion_por_hotel/hotel1_doble.jpg'),
    (1, 103, 'Individual', 75, '/static/assets/habitacion_por_hotel/hotel1_individual.jpg'),
    (1, 104, 'Familiar', 120, '/static/assets/habitacion_por_hotel/hotel1_familiar.jpeg'),
    -- Hotel 2
    (2, 201, 'Suite', 120, '/static/assets/habitacion_por_hotel/hotel2_suit.jpg'),
    (2, 202, 'Doble', 85, '/static/assets/habitacion_por_hotel/hotel2_doble.jpg'),
    (2, 203, 'Familiar', 100, '/static/assets/habitacion_por_hotel/hotel2_familiar.jpg'),
    (2, 204, 'Individual', 75, '/static/assets/habitacion_por_hotel/hotel2_individual.jpg'),
    -- Hotel 3
    (3, 301, 'Suite', 200, '/static/assets/habitacion_por_hotel/hotel3_suit.jpg'),
    (3, 302, 'Individual', 90, '/static/assets/habitacion_por_hotel/hotel3_individual.jpeg'),
    (3, 303, 'Doble', 120, '/static/assets/habitacion_por_hotel/hotel3_doble.jpg'),
    (3, 304, 'Familiar', 150, '/static/assets/habitacion_por_hotel/hotel3_familiar.jpeg');

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
    -- Hotel 1
    (1, 1, 0),
    (1, 2, 15),
    (1, 3, 20),
    (1, 4, 25),
    (1, 5, 15),
    -- Hotel 2
    (2, 1, 0),
    (2, 2, 20),
    (2, 3, 25),
    (2, 4, 30),
    (2, 5, 20),
    -- Hotel 3
    (3, 1, 0),
    (3, 2, 25),
    (3, 3, 30),
    (3, 4, 40),
    (3, 5, 30);

INSERT INTO habitacion_servicio
    (id_habitacion, id_servicio, precio)
VALUES
    -- Habitaciones del Hotel 1
    (1, 1, 0), (1, 2, 15), (1, 3, 20), (1, 4, 25), (1, 5, 15),
    (2, 1, 0), (2, 2, 15), (2, 3, 20),
    (3, 1, 0), (3, 2, 15),
    (4, 1, 0), (4, 2, 15), (4, 5, 20),
    
    -- Habitaciones del Hotel 2
    (5, 1, 0), (5, 2, 20), (5, 3, 25), (5, 4, 30), (5, 5, 20),
    (6, 1, 0), (6, 2, 20), (6, 3, 25),
    (7, 1, 0), (7, 2, 20), (7, 5, 25),
    (8, 1, 0), (8, 2, 20),
    
    -- Habitaciones del Hotel 3
    (9, 1, 0), (9, 2, 25), (9, 3, 30), (9, 4, 40), (9, 5, 30),
    (10, 1, 0), (10, 2, 25),
    (11, 1, 0), (11, 2, 25), (11, 3, 30),
    (12, 1, 0), (12, 2, 25), (12, 3, 30), (12, 5, 30);