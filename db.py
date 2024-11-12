#ESTA ES UNA DB PARA PROBAR LA API ---> NECESITAS MYSQL USUARIO Y CONTRASEÑA
import mysql.connector

conexion = mysql.connector.connect(
    #PARA USARLO DEBEN CREAR LA BASE CON CREATE DATABASE hoteles;
    #REGISTRAR UN USUARIO Y COLOCARLE UNA CONTRASEÑA
    host="localhost",
    user="usuario",
    password="contraseña",
    database="hoteles"
)
cursor = conexion.cursor()

def crear_tabla():
    cursor.execute("""
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
    CREATE TABLE reserva(
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
    """
    )
    

def insertar_hoteles():
    
    hoteles = [
    ('Hotel Sol', '123 Calle Principal, Ciudad', 'Hotel de lujo con vista al mar y todos los servicios.'),
    ('Hotel Luna', '456 Avenida Central, Ciudad', 'Hotel económico ideal para familias.'),
    ('Hotel Estrella', '789 Calle Norte, Ciudad', 'Hotel boutique con un diseño único y personalizado.')
    ]

    query = """INSERT INTO hotel (nombre, direccion, descripcion)
                VALUES (%s, %s, %s)"""

    for hotel in hoteles:
        cursor.execute(query, hotel)
    conexion.commit()

def insertar_habitaciones():
    
    habitaciones_x_hotel = [
    (1, 101, 'Suite', 150),
    (1, 102, 'Doble', 100),
    (1, 103, 'Individual', 75),
    (2, 201, 'Suite', 120),
    (2, 202, 'Doble', 85),
    (3, 301, 'Suite', 200),
    (3, 302, 'Individual', 90)
    ]

    query = ("""INSERT INTO habitaciones (id_hotel, numero, tipo, precio)
            VALUES (%s, %s, %s, %s)""")

    for habitaciones in habitaciones_x_hotel:
        cursor.execute(query, habitaciones)
        conexion.commit()



def insertar_servicios():
    servicios = [
        ('WiFi', 'Conectividad'),
        ('Desayuno', 'Alimentación'),
        ('Gimnasio', 'Entretenimiento'),
        ('Spa', 'Relajación'),
        ('Piscina', 'Entretenimiento')
    ]
    
    query = ("""INSERT INTO servicios (servicio, tipo)
            VALUES (%s, %s)""")
    
    for servicio in servicios:
        cursor.execute(query, servicio)
        conexion.commit()

def insertar_servicios_hotel():
    servicios_hotel = [
    (1, 1, 0),  #WiFi gratuito para Hotel Sol
    (1, 2, 15), #Desayuno con costo en Hotel Sol
    (1, 3, 20), #Acceso a Gimnasio en Hotel Sol
    (2, 1, 0),  #WiFi gratuito en Hotel Luna
    (2, 2, 10), #Desayuno en Hotel Luna
    (3, 1, 0),  #WiFi gratuito en Hotel Estrella
    (3, 4, 50), #Spa en Hotel Estrella
    (3, 5, 30) #Piscina en Hotel Estrella
    ]
    
    query = ("""INSERT INTO hotel_servicio (id_hotel, id_servicio, precio)
            VALUES (%s, %s, %s)""")
    
    for servicio_hotel in servicios_hotel:
        cursor.execute(query, servicio_hotel)
        conexion.commit()

def insertar_habitacion_servicios():
    habitacion_servicios = [
        (1, 1, 0),  #WiFi gratuito en la suite de Hotel Sol
        (1, 4, 45), #Spa en la suite de Hotel Sol
        (2, 1, 0),  #WiFi gratuito en la habitación doble de Hotel Sol
        (2, 2, 15), #Desayuno en la habitación doble de Hotel Sol
        (5, 2, 10), #Desayuno en la suite de Hotel Luna
        (6, 3, 25), #Gimnasio en la suite de Hotel Estrella
        (6, 5, 20) #Piscina en la suite de Hotel Estrella
    ]
    
    query = ("""INSERT INTO habitacion_servicio (id_habitacion, id_servicio, precio)
            VALUES (%s, %s, %s)""")
    
    for habitacion_servicio in habitacion_servicios:
        cursor.execute(query, habitacion_servicio)
        conexion.commit()

crear_tabla()
insertar_hoteles()
insertar_habitaciones()
insertar_servicios()
insertar_habitacion_servicios()
insertar_servicios_hotel()

cursor.close()
conexion.close()
