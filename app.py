from flask import Flask, jsonify, request
import hoteles

app = Flask(__name__)

@app.route('/api/hoteles/', methods=['GET'])
def obtener_todos_los_hoteles():
    try:
        resultado = hoteles.todos_los_hoteles()
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    json_hoteles = [dict(fila) for fila in resultado]
    return jsonify(json_hoteles), 200

@app.route('/api/hoteles/<int:id>', methods=['GET'])
def obtener_hotel_por_id(id):
    try:
        resultado = hoteles.hoteles_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro el hotel.'}), 404
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    json_hotel = dict(resultado)
    return jsonify(json_hotel), 200

@app.route('/api/servicios/', methods=['GET'])
def obtener_todos_los_servicios():
    try:
        resultado = hoteles.todos_los_servicios()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    json_servicios = [dict(fila) for fila in resultado]
    return jsonify(json_servicios), 200

@app.route('/api/servicios/<int:id>', methods=['GET'])
def obtener_servicio_por_id(id):
    try:
        resultado = hoteles.servicios_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro el servicio.'}), 404
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    json_servicio = dict(resultado)
    return jsonify(json_servicio), 200
    
@app.route('/api/habitaciones/<int:id_hotel>', methods=['GET'])
def obtener_habitaciones_por_id_hotel(id_hotel):
    try:
        resultado = hoteles.habitacion_por_id_hotel(id_hotel)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se econtro las habitaciones.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}),500
    
    json_habitaciones = [dict(fila) for fila in resultado]
    return jsonify(json_habitaciones), 200
    
@app.route('/api/habitaciones/<int:id>', methods=['GET'])
def obtener_habitacion_por_id(id):
    try:
        resultado = hoteles.habitacion_por_id(id)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la habitacion.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    json_habitacion = dict(resultado)
    return jsonify(json_habitacion), 200
    
@app.route('/api/reserva/<int:id>/<cliente>/', methods=['GET'])
def obtener_reserva_por_id_y_cliente(id, cliente):
    try:
        resultado = hoteles.obtener_reserva_por_id_y_cliente(id, cliente)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la reserva.'}), 404
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    if len(resultado) == 1:
        json_reserva = dict(resultado)
        return jsonify(json_reserva), 200
    else:
        json_reservas = [dict(fila) for fila in resultado]
        return jsonify(json_reservas), 200
    
#Hacer la solicitud POST a la API
    #respuesta = requests.post(url, json=datos)

@app.route('/api/reserva/', methods=['POST'])
def ingresar_reserva():
    datos = request.get_json()
    
    keys = ('id_habitacion', 'llegada', 'salida', 'cliente', 'precio')
    
    for key in keys:
        if key not in datos:
            return jsonify({'Error': f"Falta el dato {key}"}), 400
        
    try:
        resultado = hoteles.habitacion_por_id(datos['id_habitacion'])
        if len(resultado) == 0:
            return jsonify({'Error' : 'La habitacion no existe'}), 400
        
        hoteles.ingresar_reserva(datos)
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Exito' : 'Los datos se cargaron exitosamente'}), 200
    
#Hacer la solicitud PUT a la API
    #respuesta = requests.put(url)
    
@app.route('/api/reserva/<int:id>/<cliente>/', methods=['PUT'])
def actualizar_estado_reserva(id, cliente):
    try:
        resultado = hoteles.obtener_reserva_por_id_y_cliente(id, cliente)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la reserva.'}), 404
        
        hoteles.cancelar_reserva(id, cliente)
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Exito' : f'Los datos fueron actualizados correctamente'}), 200
    
@app.route('/api/reserva_servicios/', methods=['POST'])
def ingresar_reserva_de_servicio():
    datos =  request.get_json()
    
    keys = ('id_reserva', 'id_servicio', 'estado', 'precio')
    
    for key in keys:
        if key not in datos:
            return jsonify({'Error': f"Falta el dato {key}"}), 400
    try:
        resultado_reserva = hoteles.obtener_reserva_por_id(datos['id_reserva'])
        resultado_servicio = hoteles.servicios_por_id(datos['id_servicio'])
        if len(resultado_reserva) == 0:
            return jsonify({'Error': 'No se encontro la reserva.'}), 404
        elif len(resultado_servicio) == 0:
            return jsonify({'Error': 'No se encontro el servicio.'}), 404
        
        hoteles.reservar_servicio_por_id_reserva(datos)
        
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Exito' : 'Los datos se cargaron exitosamente'}), 200
            
@app.route('/api/reserva_servicios/<int:id_reserva>', methods=['PUT'])
def cancelar_reserva_servicios(id_reserva):
    try:
        resultado = hoteles.obtener_reserva_por_id(id_reserva)
        if len(resultado) == 0:
            return jsonify({'Error': 'No se encontro la reserva.'}), 404
        
        hoteles.cancelar_reserva_servicio_por_id_reserva(id_reserva)
    
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
    return jsonify({'Aviso', 'El estado de la reserva de servicios = cancelado'})

if __name__ == "__main__":
    app.run()
