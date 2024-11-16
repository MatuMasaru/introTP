from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

QUERY_CANCELAR_RESERVA = "UPDATE reservas SET estado = 'cancelado' WHERE id_reservas = :id_reservas AND nombre = :nombre AND estado = 'reservado'"
QUERY_DETALLES_POR_ID_RESERVA =  "SELECT nombre, salida, llegada, correo ,estado FROM reservas WHERE id_reservas= :id_reservas"
engine = create_engine("mysql+mysqlconnector://root@localhost:3307/IDS_SQL")

def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
    return result


def todos_los_detalles(id_reservas):
    return run_query(QUERY_DETALLES_POR_ID_RESERVA,{'id_reservas':id_reservas}).fetchall()

def cancelar_reserva(id_reservas, nombre):
    resultado = run_query(QUERY_CANCELAR_RESERVA, {'id_reservas': id_reservas, 'nombre': nombre})
    return resultado.rowcount
