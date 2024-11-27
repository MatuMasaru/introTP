from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()


# HOTELES QUERYS

QUERY_TODOS_LOS_HOTELES = "SELECT id, nombre, direccion, descripcion, url_img, region FROM hotel"

QUERY_HOTEL_POR_ID = "SELECT id, nombre, direccion, descripcion, url_img, region FROM hotel WHERE id = :id"

QUERY_HOTEL_POR_REGION = "SELECT id, nombre, direccion, descripcion, url_img, region FROM hotel WHERE region = :region"

QUERY_REGIONES = "SELECT DISTINCT region FROM hotel"
# HABITACIONES QUERYS

QUERY_TODAS_LAS_HABITACIONES = "SELECT h.id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre FROM habitaciones h JOIN hotel ho ON h.id_hotel = ho.id;"

QUERY_HABITACION_POR_ID_HOTEL = "SELECT h.id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre FROM habitaciones h JOIN hotel ho ON h.id_hotel = ho.id WHERE id_hotel= :id_hotel;"

QUERY_HABITACION_POR_ID = "SELECT h.id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre FROM habitaciones h JOIN hotel ho ON h.id_hotel = ho.id WHERE h.id = :id"

QUERY_HABITACION_POR_TIPO = "SELECT h.id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre FROM habitaciones h JOIN hotel ho ON h.id_hotel = ho.id WHERE tipo = :tipo"

QUERY_OBTENER_HABITACIONES_DISPONIBLES = """
SELECT
    h.id AS habitacion_id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre
FROM
    habitaciones h
JOIN
    hotel ho ON h.id_hotel = ho.id
LEFT JOIN
    reserva r ON h.id = r.id_habitacion AND r.estado != 'cancelado'
    AND (
        (:llegada BETWEEN r.llegada AND r.salida)
        OR (:salida BETWEEN r.llegada AND r.salida)
    )
WHERE
    (ho.region = :region OR :region IS NULL OR :region = '')
    AND (h.tipo = :tipo OR :tipo IS NULL OR :tipo = '')
    AND r.id IS NULL;
"""

QUERY_TIPOS_HABITACIONES = "SELECT DISTINCT tipo FROM habitaciones"

# QUERY PARA FILTRAR HABITACIONES POR REGION Y TIPO

QUERY_HABITACION_REGION_TIPO = "SELECT h.id, h.numero, h.url_img, h.tipo, h.precio, h.id_hotel, ho.nombre FROM habitaciones h JOIN hotel ho ON h.id_hotel = ho.id WHERE tipo = :tipo AND ho.region = :region"

# SERVICIOS QUERYS

QUERY_TODOS_LOS_SERVICIOS = "SELECT id, servicio, tipo FROM servicios"

QUERY_SERVICIO_POR_ID = "SELECT id, servicio, tipo FROM servicios WHERE id = :id"

QUERY_SERVICIO_POR_ID_HABITACION = "SELECT s.servicio, s.tipo, sh.precio, s.id  FROM servicios s JOIN habitacion_servicio sh ON s.id = sh.id_servicio WHERE sh.id_habitacion = :id_habitacion;"

QUERY_SERVICIO_POR_ID_HOTEL = "SELECT s.servicio, s.tipo, sh.precio, s.id  FROM servicios s JOIN hotel_servicio sh ON s.id = sh.id_servicio WHERE sh.id_hotel = :id_hotel;"

QUERY_OBTENER_PRECIO_SERVICIO_ID_HOTEL_ID_SERVICIO = "SELECT s.servicio, s.tipo, sh.precio, s.id  FROM servicios s JOIN hotel_servicio sh ON s.id = sh.id_servicio WHERE sh.id_hotel = :id_hotel AND sh.id_servicio = :id_servicio;"

# RESERVA HABITACION QUERYS --GET---

QUERY_RESERVA_POR_ID_Y_CLIENTE = "SELECT id, id_habitacion, llegada, salida, cliente_apellido, estado, precio, fecha_cancelacion FROM reserva WHERE id= :id AND cliente_apellido = :cliente_apellido"

QUERY_RESERVA_POR_ID = "SELECT id, id_habitacion, llegada, salida, cliente_apellido, estado, precio FROM reserva WHERE id= :id"

# RESERVA HABITACION QUERYS --INSERT---

QUERY_INGRESAR_RESERVA = "INSERT INTO reserva (id_habitacion, llegada, salida, cliente_apellido, estado, precio) VALUES (:id_habitacion, :llegada, :salida, :cliente_apellido, 'activo', :precio)"

QUERY_DISPONIBILIDAD_HABITACION = "SELECT estado FROM reserva WHERE id_habitacion = :id_habitacion AND (llegada < :salida AND salida > :llegada) AND estado = 'activo'"

# CANCELAR RESERVA --UPDATE---

QUERY_CANCELAR_RESERVA = "UPDATE reserva SET estado = 'cancelado', fecha_cancelacion  = NOW() WHERE id = :id AND cliente_apellido =:cliente_apellido AND estado = 'activo'"


######################################
######-----SERVICIOS
######################################

# RESERVA DE SERVICIO ---INSERT---

QUERY_EVITAR_DUPLICADOS_RESERVA_SERVICIO ="SELECT id, id_reserva, id_hotel_servicio FROM reserva_hotel_servicio WHERE id_reserva= :id_reserva AND id_hotel_servicio= :id_hotel_servicio"

QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA = "INSERT INTO reserva_hotel_servicio (id_reserva, id_hotel_servicio) VALUES (:id_reserva, :id_hotel_servicio)"

# VER RESERVA SERVICIO POR ID RESERVA

QUERY_VER_RESERVA_SERVICIO_POR_ID_RESERVA = "SELECT id, id_reserva, id_hotel_servicio FROM reserva_hotel_servicio WHERE id_reserva= :id_reserva"

# ELIMINAR SERVICIO
QUERY_ELIMINAR_SERVICIOS_POR_ID_RESERVA = "DELETE FROM reserva_hotel_servicio WHERE id_reserva = :id_reserva"

QUERY_ELIMINAR_RESERVA_SERVICIOS_POR_ID_RESERVA_Y_ID_HOTEL_SERVICIO = "DELETE FROM reserva_hotel_servicio WHERE id_reserva = :id_reserva AND id_hotel_servicio = :id_hotel_servicio"


engine = create_engine(f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:3306/{os.getenv('MYSQL_DB')}?charset=utf8mb4&collation=utf8mb4_unicode_ci")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
    return result

#-----HOTELES FUNCIONES

def todos_los_hoteles():
    return run_query(QUERY_TODOS_LOS_HOTELES).fetchall()

def hoteles_por_id(id):
    return run_query(QUERY_HOTEL_POR_ID, {"id": id}).fetchall()

def hoteles_por_region(region):
    return run_query(QUERY_HOTEL_POR_REGION, {"region": region}).fetchall()

def todas_las_regiones():
    return run_query(QUERY_REGIONES).fetchall()

#----HABITACIONES FUNCIONES

def todas_las_habitaciones():
    return run_query(QUERY_TODAS_LAS_HABITACIONES).fetchall()

def habitacion_por_id_hotel(id_hotel):
    return run_query(QUERY_HABITACION_POR_ID_HOTEL, {"id_hotel": id_hotel}).fetchall()

def habitacion_por_id(id):
    return run_query(QUERY_HABITACION_POR_ID, {"id": id}).fetchall()

def habitacion_por_tipo(tipo):
    return run_query(QUERY_HABITACION_POR_TIPO, {"tipo": tipo}).fetchall()

def comprobar_disponibilidad_habitacion(id_habitacion, salida, llegada):
    return run_query(QUERY_DISPONIBILIDAD_HABITACION,{"id_habitacion": id_habitacion, "salida": salida, "llegada": llegada},).fetchall()

def obtener_habitaciones_disponibles(region, salida, llegada, tipo):
    return run_query(QUERY_OBTENER_HABITACIONES_DISPONIBLES, {"region": region, "salida": salida, "llegada": llegada, "tipo": tipo}).fetchall()

def todos_los_tipos_de_habitacion():
    return run_query(QUERY_TIPOS_HABITACIONES).fetchall()

#----FILTRO HABITACION POR REGION Y TIPO

def habitacion_por_region_y_tipo(tipo, region):
    return run_query(QUERY_HABITACION_REGION_TIPO, {"tipo": tipo, "region": region}).fetchall()

#----SERVICIOS FUNCIONES
def todos_los_servicios():
    return run_query(QUERY_TODOS_LOS_SERVICIOS).fetchall()

def servicios_por_id(id):
    return run_query(QUERY_SERVICIO_POR_ID, {"id": id}).fetchall()

def servicio_por_habitacion(id_habitacion):
    return run_query(QUERY_SERVICIO_POR_ID_HABITACION, {"id_habitacion": id_habitacion}).fetchall()

def servicio_por_hotel(id_hotel):
    return run_query(QUERY_SERVICIO_POR_ID_HOTEL, {"id_hotel": id_hotel}).fetchall()

def servicio_id_hotel_id_servicio(id_hotel, id_servicio):
    return run_query(QUERY_OBTENER_PRECIO_SERVICIO_ID_HOTEL_ID_SERVICIO, {"id_hotel": id_hotel, "id_servicio": id_servicio}).fetchall()

#----RESERVA FUNCIONES 

#----GET----

def obtener_reserva_por_id_y_cliente(id, cliente_apellido):
    return run_query(QUERY_RESERVA_POR_ID_Y_CLIENTE, {"id": id, "cliente_apellido": cliente_apellido}).fetchall()

def obtener_reserva_por_id(id):
    return run_query(QUERY_RESERVA_POR_ID, {"id": id}).fetchall()

def obtener_reserva_servicio_por_id_reserva(id_reserva):
    return run_query(QUERY_VER_RESERVA_SERVICIO_POR_ID_RESERVA, {"id_reserva": id_reserva}).fetchall()

def verificar_reserva_servicio(id_reserva, id_servicio):
    return run_query(QUERY_EVITAR_DUPLICADOS_RESERVA_SERVICIO, {"id_reserva": id_reserva, "id_hotel_servicio": id_servicio}).fetchall()

#----POST----

def ingresar_reserva(datos):
    run_query(QUERY_INGRESAR_RESERVA, datos)
    return run_query("SELECT LAST_INSERT_ID();").scalar()

def reservar_servicio_por_id_reserva(id_reserva, id_servicio):
    run_query(QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA, {"id_reserva": id_reserva, "id_hotel_servicio": id_servicio})
    
#----PUT----

def cancelar_reserva(id, cliente_apellido):
    run_query(QUERY_CANCELAR_RESERVA, {"id": id, "cliente_apellido": cliente_apellido})

def eliminar_un_solo_servicio(id_reserva, id_servicio):
    run_query(QUERY_ELIMINAR_RESERVA_SERVICIOS_POR_ID_RESERVA_Y_ID_HOTEL_SERVICIO,{"id_reserva": id_reserva, "id_hotel_servicio": id_servicio})

def eliminar_reserva_servicio_por_id_reserva(id_reserva):
    run_query(QUERY_ELIMINAR_SERVICIOS_POR_ID_RESERVA, {"id_reserva": id_reserva})

