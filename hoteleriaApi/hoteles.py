from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

# HOTELES QUERYS

QUERY_TODOS_LOS_HOTELES = (
    "SELECT id, nombre, direccion, descripcion, url_img, region FROM hotel"
)

QUERY_HOTEL_POR_ID = "SELECT id, nombre, direccion, descripcion, url_img, region FROM hotel WHERE id = :id"

# SERVICIOS QUERYS

QUERY_TODOS_LOS_SERVICIOS = "SELECT id, servicio, tipo FROM servicios"

QUERY_SERVICIO_POR_ID = "SELECT id, servicio, tipo FROM servicios WHERE id = :id"

QUERY_SERVICIO_POR_ID_HABITACION = "SELECT s.servicio, s.tipo, sh.precio FROM servicios s JOIN habitacion_servicio sh ON s.id = sh.id_servicio WHERE sh.id_habitacion = :id_habitacion;"

QUERY_SERVICIO_POR_ID_HOTEL = "SELECT s.servicio, s.tipo, sh.precio FROM servicios s JOIN hotel_servicio sh ON s.id = sh.id_servicio WHERE sh.id_hotel = :id_hotel;"

# HABITACIONES QUERYS

QUERY_HABITACION_POR_ID_HOTEL = "SELECT id, numero, url_img, tipo, precio, id_hotel FROM habitaciones WHERE id_hotel = :id_hotel"

QUERY_HABITACION_POR_ID = "SELECT id, numero, url_img, tipo, precio, id_hotel FROM habitaciones WHERE id = :id"

# RESERVA HABITACION QUERYS --GET---

QUERY_RESERVA_POR_ID_Y_CLIENTE = "SELECT id, id_habitacion, llegada, salida, cliente_apellido, estado, precio, fecha_cancelacion FROM reserva WHERE id= :id AND cliente_apellido = :cliente_apellido"

QUERY_RESERVA_POR_ID = "SELECT id, id_habitacion, llegada, salida, cliente_apellido, estado, precio FROM reserva WHERE id= :id"

# RESERVA HABITACION QUERYS --INSERT---

QUERY_INGRESAR_RESERVA = "INSERT INTO reserva (id_habitacion, llegada, salida, cliente_apellido, estado, precio) VALUES (:id_habitacion, :llegada, :salida, :cliente_apellido, 'activo', :precio)"

QUERY_DISPONIBILIDAD_HABITACION = "SELECT estado FROM reserva WHERE id_habitacion = :id_habitacion AND (llegada < :salida AND salida > :llegada) AND estado = 'activo'"

"""Explicacion

Cuando solicitamos una reserva verficia que
la nueva_salida sea menor a la llegada ya reservada si es menor no importa la segunda
ahora si es mayor debemos verificar que la nueva_llegada sea mayor a la salida reservada
este proceso verifica que no habra solapamiento de reservas.
Puedo hacer comparaciones ya que el type date lo permite

"""

# CANCELAR RESERVA --UPDATE---

QUERY_CANCELAR_RESERVA = "UPDATE reserva SET estado = 'cancelado', fecha_cancelacion  = NOW() WHERE id = :id AND cliente_apellido =:cliente_apellido AND estado = 'activo'"

# RESERVA DE SERVICIO POR CLIENTE
QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA = "INSERT INTO reserva_servicios (id_reserva, id_servicio, estado, precio) VALUES (:id_reserva, :id_servicio, 'activo', :precio)"

# VER RESERVA SERVICIO POR ID RESERVA

QUERY_RESERVA_SERVICIO_POR_ID_RESERVA = "SELECT id, id_reserva, id_servicio, estado, precio FROM reserva_servicios WHERE id_reserva= :id_reserva"

# CANCELAR SERVICIO
QUERY_CANCELAR_SERVICIOS_POR_ID_RESERVA = (
    "UPDATE reserva_servicios SET estado = 'cancelado' WHERE id_reserva = :id_reserva"
)


engine = create_engine(
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:3306/{os.getenv('MYSQL_DB')}?charset=utf8mb4&collation=utf8mb4_unicode_ci"
)


def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()

    return result


def todos_los_hoteles():
    return run_query(QUERY_TODOS_LOS_HOTELES).fetchall()


def hoteles_por_id(id):
    return run_query(QUERY_HOTEL_POR_ID, {"id": id}).fetchall()


def todos_los_servicios():
    return run_query(QUERY_TODOS_LOS_SERVICIOS).fetchall()


def servicios_por_id(id):
    return run_query(QUERY_SERVICIO_POR_ID, {"id": id}).fetchall()


def servicio_por_habitacion(id_habitacion):
    return run_query(
        QUERY_SERVICIO_POR_ID_HABITACION, {"id_habitacion": id_habitacion}
    ).fetchall()


def servicio_por_hotel(id_hotel):
    return run_query(QUERY_SERVICIO_POR_ID_HOTEL, {"id_hotel": id_hotel}).fetchall()


def habitacion_por_id_hotel(id_hotel):
    return run_query(QUERY_HABITACION_POR_ID_HOTEL, {"id_hotel": id_hotel}).fetchall()


def habitacion_por_id(id):
    return run_query(QUERY_HABITACION_POR_ID, {"id": id}).fetchall()


def obtener_reserva_por_id_y_cliente(id, cliente_apellido):
    return run_query(
        QUERY_RESERVA_POR_ID_Y_CLIENTE, {"id": id, "cliente_apellido": cliente_apellido}
    ).fetchall()


def obtener_reserva_por_id(id):
    return run_query(QUERY_RESERVA_POR_ID, {"id": id}).fetchall()


def comprobar_disponibilidad_habitacion(id_habitacion, salida, llegada):
    return run_query(
        QUERY_DISPONIBILIDAD_HABITACION,
        {"id_habitacion": id_habitacion, "salida": salida, "llegada": llegada},
    ).fetchall()


def ingresar_reserva(datos):
    run_query(QUERY_INGRESAR_RESERVA, datos)
    return run_query("SELECT LAST_INSERT_ID();").scalar()


def cancelar_reserva(id, cliente_apellido):
    run_query(QUERY_CANCELAR_RESERVA, {"id": id, "cliente_apellido": cliente_apellido})


def reservar_servicio_por_id_reserva(datos):
    run_query(QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA, datos)


def obtener_reserva_servicio_por_id_reserva(id_reserva):
    return run_query(
        QUERY_RESERVA_SERVICIO_POR_ID_RESERVA, {"id_reserva": id_reserva}
    ).fetchall()


def cancelar_reserva_servicio_por_id_reserva(id_reserva):
    run_query(QUERY_CANCELAR_SERVICIOS_POR_ID_RESERVA, {"id_reserva": id_reserva})
