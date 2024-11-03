from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(_name_)

app.config['SQLALCHEMY_DATABASE_URI'] = "#"  # Agrega direccion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


# Obtener los hoteles (sucursales)
@app.route('/sucursales', methods=['GET'])
def obtener_sucursales():
    query = text("SELECT * FROM sucursales")
    with engine.connect() as connection:
        resultado = connection.execute(query)
        sucursales = [dict(fila) for fila in resultado]
    return jsonify(sucursales)


# Obtener habitaciones por id_sucursal
@app.route('/habitaciones/<id_sucursal>', methods=['GET'])
def obtener_habitaciones(id_sucursal):
    query = text("SELECT * FROM habitaciones WHERE id_sucursal = :id_sucursal")
    with engine.connect() as connection:
        resultado = connection.execute(query, {"id_sucursal": id_sucursal})
        habitaciones = [dict(fila) for fila in resultado]
    return jsonify(habitaciones)


# Obtener servicios
@app.route('/servicios', methods=['GET'])
def obtener_servicios():
    query = text("SELECT * FROM servicios")
    with engine.connect() as connection:
        resultado = connection.execute(query)
        servicios = [dict(fila) for fila in resultado]
    return jsonify(servicios)


# Obtener reserva por código y nombre de reserva
@app.route('/reservas/<nombre>/<codigo>', methods=['GET'])
def obtener_reserva(nombre, codigo):
    query = text("SELECT * FROM reserva WHERE codigo = :codigo AND nombre = :nombre")
    with engine.connect() as connection:
        resultado = connection.execute(query, {"codigo": codigo, "nombre": nombre})
        reserva = dict(resultado) #Puede dar error
    return jsonify(reserva)


# Cancelar reserva
@app.route('/reservas/<codigo>/<nombre>', methods=['PUT'])
def cancelar_reserva(codigo, nombre):
    query = text("UPDATE reserva SET estado = :estado WHERE codigo = :codigo AND nombre = :nombre")
    with engine.connect() as connection:
        connection.execute(query, {"estado": 0, "codigo": codigo, "nombre": nombre})
    return jsonify({"mensaje": "Reserva cancelada"})


if _name_ == "_main_":
    app.run()
