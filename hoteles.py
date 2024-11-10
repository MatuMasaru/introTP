from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

#HOTELES QUERYS

QUERY_TODOS_LOS_HOTELES = "SELECT id, nombre, direccion, descripcion FROM hoteles"

QUERY_HOTELES_POR_ID = "SELECT nombre, direccion, descripcion FROM hoteles WHERE id = :id"

#SERVICIOS QUERYS

QUERY_TODOS_LOS_SERVICIOS = "SELECT id, servicio, tipo, precio FROM servicios"

QUERY_SERVICIO_POR_ID = "SELECT servicio, tipo, precio FROM servicios WHERE id = :id"

#HABITACIONES QUERYS

QUERY_HABITACION_POR_ID_HOTEL = "SELECT id, numero, tipo, precio FROM habitaciones WHERE id_hotel = :id_hotel"

QUERY_HABITACION_POR_ID =  "SELECT id_hotel, numero, tipo, precio FROM habitaciones WHERE id = :id"

#RESERVA HABITACION QUERYS --GET---

QUERY_RESERVA_POR_ID_Y_CLIENTE = "SELECT id, id_habitacion, llegada, salida, cliente, estado, precio FROM reserva WHERE id= :id AND cliente = :cliente"

#RESERVA HABITACION QUERYS --INSERT---

QUERY_INGRESAR_RESERVA = "INSERT INTO reserva (id_habitacion, llegada, salida, cliente, estado, precio) VALUES (:id_habitacion, :llegada, :salida, :cliente, activo, :precio) WHERE id_habitacion = :id_habitacion AND (llegada < :salida AND salida > :llegada)"

"""Explicacion

Cuando solicitamos una reserva verficia que
la nueva_salida sea menor a la llegada ya reservada si es menor no importa la segunda
ahora si es mayor debemos verificar que la nueva_llegada sea mayor a la salida reservada
este proceso verifica que no habra solapamiento de reservas.
Puedo hacer comparaciones ya que el type date lo permite

"""

#CANCELAR RESERVA --UPDATE---

QUERY_CANCELAR_RESERVA = "UPDATE reserva SET estado = cancelado, fecha_cancelacion = :fecha_cancelacion WHERE id = :id AND cliente =:cliente"

#RESERVA DE SERVICIO POR CLIENTE
QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA = "INSERT INTO reserva_servicios id_reserva, id_servicio, estado, precio VALUES (:id_reserva, :id_servicio, activo, :precio)"

#CANCELAR SERVICIO 
QUERY_CANCELAR_SERVICIOS_POR_ID_RESERVA = "UPDATE reserva_servicios SET estado = cancelado WHERE id_reserva = :id_reserva"


engine = create_engine("mysql+pymysql://root@localhost:3308/hoteles.db")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
        
    return result

def todos_los_hoteles():
    return run_query(QUERY_TODOS_LOS_HOTELES).fetchall()

def hoteles_por_id(id):
    return run_query(QUERY_HOTELES_POR_ID, {'id': id}).fetchall()

def todos_los_servicios():
    return run_query(QUERY_TODOS_LOS_SERVICIOS).fetchall()

def servicios_por_id(id):
    return run_query(QUERY_SERVICIO_POR_ID, {'id': id}).fetchall()

def habitacion_por_id_hotel(id_hotel):
    return run_query(QUERY_HABITACION_POR_ID_HOTEL, {'id_hotel': id_hotel}).fetchall()

def habitacion_por_id(id):
    return run_query(QUERY_HABITACION_POR_ID, {'id': id}).fetchall()

def obtener_reserva_por_id_y_cliente(id, cliente):
    return run_query(QUERY_RESERVA_POR_ID_Y_CLIENTE, {'id':id, 'cliente':cliente}).fetchall()

def ingresar_reserva(id_habitacion, llegada, salida, cliente, precio):
    run_query(QUERY_INGRESAR_RESERVA, {'id_habitacion': id_habitacion, 'llegada':llegada, 'salida':salida, 'cliente': cliente, 'precio':precio})
    
def cancelar_reserva(id, cliente):
    run_query(QUERY_CANCELAR_RESERVA, {'id':id, 'cliente':cliente})

def reservar_servicio_por_id_reserva(id_reserva, id_servicio, precio):
    run_query(QUERY_RESERVAR_SERVICIOS_POR_ID_RESERVA, {'id_reserva': id_reserva, 'id_cliente': id_servicio, 'precio': precio})

def cancelar_reserva_servicio_por_id_reserva(id_reserva):
    run_query(QUERY_CANCELAR_SERVICIOS_POR_ID_RESERVA, {'id_reserva': id_reserva})
