from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost/nombre_base_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear el motor de SQLAlchemy
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])


#Obtener los hoteles

"""
Tabla esperada

nombre, direccion_img, ubicacion

"""


@app.route('/sucursales', methods=['GET'])
def obtener_registros():
    query = text("SELECT nombre, direccion_img, ubicacion FROM sucursales")
    with engine.connect() as connection:
        resultado = connection.execute(query)
        sucursales = [dict(fila) for fila in resultado]
    return jsonify(sucursales)

#Obtener los hoteles

"""
Tabla esperada

nombre, direccion_img, ubicacion

"""


@app.route('/servicios', methods=['GET'])
def obtener_registros():
    query = text("SELECT nombre, direccion_img, ubicacion FROM sucursales")
    with engine.connect() as connection:
        resultado = connection.execute(query)
        sucursales = [dict(fila) for fila in resultado]
    return jsonify(sucursales)


if __name__ == "__main__":
    app.run()