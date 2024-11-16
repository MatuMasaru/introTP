from flask import Flask, jsonify, request
import hotel



app = Flask(__name__)
@app.route('/api/reserva/detalles/<int:id_reservas>/', methods=['GET'])
def obtener_reserva_por_id_y_cliente(id_reservas):
    try:
        resultado = hotel.todos_los_detalles(id_reservas)
        if len(resultado) == 0:
            return jsonify({'Error': 'El id o el cliente es incorrecto'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    respuesta = []
    for fila in resultado:
        respuesta.append({'llegada': fila[2], 'salida':fila[1], 'nombre':fila[0], 'correo': fila[3], 'estado':fila[4]})
    return jsonify(respuesta), 200



@app.route('/api/reserva/cancelar/<int:id_reservas>/<string:nombre>', methods=['POST'])
def cancelar_reserva(id_reservas, nombre):
    try:
        detalles = hotel.todos_los_detalles(id_reservas)
        if len(detalles) == 0:
            return jsonify({'Error': 'El id_reserva no existe'}), 404
        if detalles[0][4] == "cancelado":  # Verificamos el estado
            return jsonify({'Error': 'La reserva ya se encuentra cancelada'}), 400
        hotel.cancelar_reserva(id_reservas, nombre)
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    return jsonify({'Aviso': 'El estado de la reserva de servicios es "cancelado"'})

if __name__ == '__main__':
    app.run(debug=True, port="3648")
