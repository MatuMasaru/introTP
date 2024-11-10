from flask import Flask, jsonify, request
import hoteles

app = Flask(__name__)

@app.route('/api/hoteles/', methods=['GET'])
def obtener_todos_los_hoteles():
    try:
        resultado = hoteles.todos_los_hoteles()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/hoteles/<int:id>', methods=['GET'])
def obtener_hotel_por_id(id):
    try:
        resultado = hoteles.hoteles_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro el hotel.'}), 404
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

@app.route('/api/servicios/', methods=['GET'])
def obtener_todos_los_servicios():
    try:
        resultado = hoteles.todos_los_servicios()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/servicios/<int:id>', methods=['GET'])
def obtener_servicio_por_id(id):
    try:
        resultado = hoteles.servicios_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro el servicio.'}), 404
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@app.route('/api/habitaciones/<int:id_hotel>', methods=['GET'])
def obtener_habitaciones_por_id_hotel(id_hotel):
    try:
        resultado = hoteles.habitacion_por_id_hotel(id_hotel)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se econtro las habitaciones.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}),500
    
@app.route('/api/habitaciones/<int:id>', methods=['GET'])
def obtener_habitacion_por_id(id):
    try:
        resultado = hoteles.habitacion_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la habitacion.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
@app.route('/api/reserva/<int:id>/<cliente>/')
def obtener_reserva_por_id_y_cliente(id, cliente):
    try:
        resultado = hoteles.obtener_reserva_por_id_y_cliente(id, cliente)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la reserva.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500

if __name__ == "__main__":
    app.run()
