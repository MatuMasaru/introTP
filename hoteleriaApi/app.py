from flask import Flask, jsonify, request
import hoteles

app = Flask(__name__)

@app.route("/")
def hola():
    return jsonify({"Saludo": "La api funciona"}), 200

#---------------------------------#
#------------HOTELES--------------#
#---------------------------------#

def crear_respuesta_hoteles(resultado):
    respuesta = []
    for fila in resultado:
        respuesta.append(
            {
                "id": fila[0],
                "nombre": fila[1],
                "direccion": fila[2],
                "descripcion": fila[3],
                "url_img": fila[4],
                "region": fila[5],
            }
        )
    return respuesta

@app.route("/api/hoteles/", methods=["GET"])
def obtener_todos_los_hoteles():
    try:
        resultado = hoteles.todos_los_hoteles()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    respuesta = crear_respuesta_hoteles(resultado)
    return jsonify(respuesta), 200

@app.route("/api/hoteles/<int:id>", methods=["GET"])
def obtener_hotel_por_id(id):
    try:
        resultado = hoteles.hoteles_por_id(id)
        if len(resultado) == 0:
            return jsonify({"Error": "El id es inexistente"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_hoteles(resultado)
    return jsonify(respuesta), 200

@app.route("/api/hoteles/<region>", methods=["GET"])
def obtener_hotel_por_region(region):
    try:
        resultado = hoteles.hoteles_por_region(region)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay hotel con esa region"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_hoteles(resultado)
    return jsonify(respuesta), 200

@app.route("/api/hoteles/regiones/", methods=["GET"])
def obtener_todas_las_regiones():
    try:
        resultado = hoteles.todas_las_regiones()
        if len(resultado) == 0:
            return jsonify({"Error": "No hay regiones"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    respuesta = []
    for fila in resultado:
        respuesta.append(fila[0])
    return jsonify(respuesta), 200


#---------------------------------#
#-----------ADMIN HOTELES----------#
#---------------------------------#

@app.route("/api/create_hotel/", methods=["POST"])
def create_hotel():
    data = request.get_json()

    keys = ('nombre', 'direccion', 'descripcion', 'url_img', 'region')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Falta el dato {key}'}), 400
    
    try:
        hoteles.insert_hotel(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201

@app.route('/api/delete_hotel', methods=['DELETE'])
def delete_hotel():
    try:
        id_hotel = request.get_json()
        int_id_hotel = id_hotel['id']

        resultado = hoteles.hoteles_por_id(int_id_hotel)
        if len(resultado) == 0:
            return jsonify({'error': 'No se encontró el hotel'}), 404
        
        hoteles.borrar_hotel(int_id_hotel)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    resultado = resultado[0]
    return jsonify({'nombre': resultado[1], 'direccion': resultado[2], 'descripcion': resultado[3], 'url_img': resultado[4], 'region': resultado[5], 'id': int_id_hotel}), 200


app.route("/api/update_hotel/", methods=["PUT"])
def update_hotel():
    data = request.get_json()
    int_id_hotel = data['id']

    keys = ('nombre', 'direccion', 'descripcion', 'url_img', 'region')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Falta el dato {key}'}), 400
    
    try:
        resultado = hoteles.hoteles_por_id(int_id_hotel)
        if len(resultado) == 0:
            return jsonify({'error': 'No se encontró el hotel'}), 404

        hoteles.actualizar_hotel(int_id_hotel, data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201


#---------------------------------#
#-----------HABITACIONES----------#
#---------------------------------#

def crear_respuesta_habitaciones(resultado):
    respuesta = []
    for fila in resultado:
        respuesta.append(
            {
                "id": fila[0],
                "numero": fila[1],
                "url_img": fila[2],
                "tipo": fila[3],
                "precio": fila[4],
                "id_hotel": fila[5],
                "nombre": fila[6]
            }
        )
    return respuesta

@app.route("/api/habitaciones/", methods=["GET"])
def obtener_habitaciones():
    try:
        resultado = hoteles.todas_las_habitaciones()
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200

@app.route("/api/habitaciones/<int:id_hotel>", methods=["GET"])
def obtener_habitaciones_por_id_hotel(id_hotel):
    try:
        resultado = hoteles.habitacion_por_id_hotel(id_hotel)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_hotel es inexistente."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200

@app.route("/api/habitaciones/disponibles", methods=["GET"])
def obtener_habitaciones_disponibles():
    region = request.args.get("region")
    llegada = request.args.get("llegada")
    salida = request.args.get("salida")
    tipo = request.args.get("tipo")
    
    if llegada is None or salida is None:
        return jsonify({"Error": "Faltan datos"}), 400

    try:
        resultado = hoteles.obtener_habitaciones_disponibles(region, llegada, salida, tipo)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay habitaciones disponibles"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200

@app.route("/api/habitacion/<int:id>", methods=["GET"])
def obtener_habitacion_por_id(id):
    try:
        resultado = hoteles.habitacion_por_id(id)
        if len(resultado) == 0:
            return jsonify({"Error": "El id es inexistente."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200

@app.route("/api/habitaciones/<tipo>", methods=["GET"])
def obtener_habitaciones_por_tipo(tipo):
    try:
        resultado = hoteles.habitacion_por_tipo(tipo)
        if len(resultado) == 0:
            return jsonify({"Error": "El tipo de habitacion es inexistente."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200


#---------------------------------#
#-----------ADMIN HABITACIONES----------#
#---------------------------------#

@app.route('/api/habitaciones/admin', methods=['POST'])
def create_habitacion():
    data = request.get_json()

    """
        data =  {
                "numero": numero,
                "url_img": url_img,
                "tipo": tipo,
                "precio": precio,
                "id_hotel": id_hotel,
            } 
    """

    keys = ('numero', 'url_img', 'tipo', 'precio', 'id_hotel')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400
        
    try:
        result = hoteles.hoteles_por_id(data['id_hotel'])
        if len(result) == 0:
            return jsonify({'error': 'La habitacion no pertenece a ningun hotel'}), 400

        hoteles.insert_habitacion(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201


@app.route('/api/habitaciones/admin/<int:id>', methods=['DELETE'])
def delete_habitacion(id):
    try:
        result = hoteles.habitacion_por_id(id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró la habitacion'}), 404

        hoteles.borrar_habitacion(id)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return jsonify({'numero': result[1], 'url_img': result[2], 'tipo': result[3], 'precio': result[4], 'id_hotel': result[5], 'id': id}), 200


@app.route('/api/habitaciones/admin/<int:id>', methods=['PUT'])
def update_habitacion(id):
    data = request.get_json()

    """
        data =  {
                "numero": numero,
                "url_img": url_img,
                "tipo": tipo,
                "precio": precio,
                "id_hotel": id_hotel,
            } 
    """

    keys = ('numero', 'url_img', 'tipo', 'precio', 'id_hotel')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400

    try:
        result = hoteles.hoteles_por_id(data['id_hotel'])
        if len(result) == 0:
            return jsonify({'error': 'La habitacion no pertenece a ningun hotel'}), 400
        
        hoteles.actualizar_habitacion(id, data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'id': id, **data}), 200

#------------------------------------------------#
#------------HABITACION REGION Y TIPO------------#
#------------------------------------------------#
@app.route("/api/habitacion/<tipo>/<region>", methods=["GET"])
def obtener_habitacion_por_region_tipo(tipo, region):
    try:
        resultado = hoteles.habitacion_por_region_y_tipo(tipo, region)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay habitaciones con esas caracteristicas"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_habitaciones(resultado)
    return jsonify(respuesta), 200
    
#---------------------------------#
#------------SERVICIOS------------#
#---------------------------------#

def crear_respuesta_servicios(resultado):
    respuesta = []
    for fila in resultado:
        if len(resultado[0]) == 3:
            respuesta.append({"id": fila[0], "servicio": fila[1], "tipo": fila[2]})
        else:
            respuesta.append({"servicio": fila[0], "tipo": fila[1], "precio": fila[2], "id_servicio": fila[3]})
    return respuesta

@app.route("/api/servicios/", methods=["GET"])
def obtener_todos_los_servicios():
    try:
        resultado = hoteles.todos_los_servicios()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    respuesta = crear_respuesta_servicios(resultado)
    return jsonify(respuesta), 200

@app.route("/api/servicios/<int:id>", methods=["GET"])
def obtener_servicio_por_id(id):
    try:
        resultado = hoteles.servicios_por_id(id)
        if len(resultado) == 0:
            return jsonify({"Error": "El id es inexistente"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    respuesta = crear_respuesta_servicios(resultado)
    return jsonify(respuesta), 200

@app.route("/api/servicios/hotel/<int:id_hotel>", methods=["GET"])
def obtener_servicios_por_hotel(id_hotel):
    try:
        resultado = hoteles.hoteles_por_id(id_hotel)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_hotel es inexistente"}), 404
        resultado = hoteles.servicio_por_hotel(id_hotel)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay servicios incluidos en este hotel"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_servicios(resultado)
    return jsonify(respuesta), 200

@app.route("/api/servicios/hotel/<int:id_hotel>/<int:id_servicio>", methods=["GET"])
def obtener_precio_servicio_hotel(id_hotel, id_servicio):
    try:
        resultado = hoteles.hoteles_por_id(id_hotel)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_hotel es inexistente"}), 404
        resultado = hoteles.servicios_por_id(id_servicio)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay servicio con ese id_servicio"}), 404
        resultado = hoteles.servicio_id_hotel_id_servicio(id_hotel, id_servicio)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay servicio en el id_hotel con ese id_servicio"})
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    respuesta = crear_respuesta_servicios(resultado)
    return jsonify(respuesta), 200

@app.route("/api/servicios/habitacion/<int:id_habitacion>", methods=["GET"])
def obtener_servicios_por_habitacion(id_habitacion):
    try:
        resultado = hoteles.habitacion_por_id(id_habitacion)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_habitacion es inexistente"}), 404
        resultado = hoteles.servicio_por_habitacion(id_habitacion)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay servicios incluidos en esta habitacion"}), 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    respuesta = crear_respuesta_servicios(resultado)
    return jsonify(respuesta), 200


#---------------------------------#
#-----------ADMIN SERVICIOS----------#
#---------------------------------#

@app.route("/api/servicios/admin", methods=['POST'])
def create_servicios():
    data = request.get_json()
    """
        data =  {
                "servicio": servicio,
                "tipo": tipo
            } 
    """
    keys = ('servicio', 'tipo')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400

    try:
      hoteles.insert_servicio(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201

@app.route("/api/servicios/admin/<int:id>", methods=['DELETE'])
def delete_servicio(id):
    try:
        result = hoteles.servicios_por_id(id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio'}), 404

        hoteles.borrar_servicio(id)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return jsonify({'servicio': result[1], 'tipo': result[2], 'id': id}), 200


@app.route("/api/servicios/admin/<int:id>", methods=['PUT'])
def update_servicio(id):
    data = request.get_json()
    """
        data =  {
                "servicio": servicio,
                "tipo": tipo
            } 
    """
    keys = ('servicio', 'tipo')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400

    try:
        result = hoteles.hoteles_por_id(id)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio'}), 404

        hoteles.actualizar_servicio(id, data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'id': id, **data}), 200


#---------------------------------#
#-----------ADMIN HOTEL_SERVICIO----------#
#---------------------------------#

@app.route("/api/hotel_servicio/admin", methods=['POST'])
def add_hotel_servicio():
    data = request.get_json()

    """
        data =  {
                "id_hotel": id_hotel,
                "id_servicio": id_servicio,
                "precio": precio,
            } 
    """
    
    keys = ('id_hotel', 'id_servicio', 'precio')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400

    try:
        result_1 = hoteles.servicios_por_id(data['id_servicio'])
        if len(result_1) == 0:
            return jsonify({'error': 'No se encontró el servicio'})

        result_2 = hoteles.hoteles_por_id(data['id_hotel'])
        if len(result_2) == 0:
            return jsonify({'error': 'El servicio no pertence a ningun hotel'}), 400

        hoteles.insert_servicio_hotel(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(data), 201


@app.route("/api/hotel_servicio/admin/<int:id_hotel>/<int:id_servicio>", methods=['DELETE'])
def delete_hotel_servicio(id_hotel, id_servicio):
    try:
        result = hoteles.servicio_id_hotel_id_servicio(id_hotel, id_servicio)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio del hotel'}), 404
        
        hoteles.borrar_servicio_hotel(id_hotel, id_servicio)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    result = result[0]
    return jsonify({'servicio': result[0], 'tipo': result[1], 'precio':[2], 'id': id_servicio}), 200

@app.route("/api/hotel_servicio/admin/<int:id_hotel>/<int:id_servicio>", methods=['PUT'])
def update_hotel_servicio(id_hotel, id_servicio):
    data = request.get_json()

    """
        data =  {
                "id_hotel": id_hotel,
                "id_servicio": id_servicio,
                "precio": precio,
            } 
    """

    keys = ('id_hotel', 'id_servicio', 'precio')
    for key in keys:
        if key not in data:
            return jsonify({'error': f'Faltan el dato {key}'}), 400
        
    try:
        result = hoteles.servicio_id_hotel_id_servicio(id_hotel, id_servicio)
        if len(result) == 0:
            return jsonify({'error': 'No se encontró el servicio del hotel'}), 404
        
        hoteles.actualizar_servicio_hotel(id_hotel, id_servicio, data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'id_hotel': id_hotel, 'id_servicio': id_servicio, **data}), 200

#-----------------------------------------------------------#----------------------#
#-------------RESERVAS DE HABITACION Y SERVICIOS------------#-------GET------------#
#-----------------------------------------------------------#----------------------#

@app.route("/api/reserva/<int:id>/<cliente>/", methods=["GET"])
def obtener_reserva_por_id_y_cliente(id, cliente):
    try:
        resultado = hoteles.obtener_reserva_por_id_y_cliente(id, cliente)
        if len(resultado) == 0:
            return jsonify({"Error": "El id o el cliente es incorrecto"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    respuesta = []
    for fila in resultado:
        respuesta.append(
            {
                "id": fila[0],
                "id_habitacion": fila[1],
                "llegada": fila[2],
                "salida": fila[3],
                "cliente_apellido": fila[4],
                "estado": fila[5],
                "precio": fila[6],
                "fecha_cancelacion": fila[7],
            }
        )
    return jsonify(respuesta), 200

@app.route("/api/reserva/servicios/<int:id_reserva>", methods=["GET"])
def obtener_reserva_servicio(id_reserva):
    try:
        resultado = hoteles.obtener_reserva_por_id(id_reserva)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_reserva no existe."}), 404
        resultado = hoteles.obtener_reserva_servicio_por_id_reserva(id_reserva)
        if len(resultado) == 0:
            return jsonify({"Error": "No hay servicios reservados."}), 400
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    respuesta = []
    for fila in resultado:
        respuesta.append(
            {
                "id": fila[0],
                "id_reserva": fila[1],
                "id_servicio": fila[2],
                "estado": fila[3],
                "precio": fila[4],
            }
        )
    return jsonify(respuesta), 200

#-----------------------------------------------------------#-----------------------#
#-------------RESERVAS DE HABITACION Y SERVICIOS------------#-------POST------------#
#-----------------------------------------------------------#-----------------------#

@app.route("/api/reserva/", methods=["POST"])
def ingresar_reserva():
    datos = request.get_json()
    keys = ("id_habitacion", "llegada", "salida", "cliente_apellido", "precio")
    for key in keys:
        if key not in datos:
            return jsonify({"Error": f"Falta el dato {key}"}), 400
    try:
        resultado = hoteles.comprobar_disponibilidad_habitacion(datos["id_habitacion"], datos["salida"], datos["llegada"])
        if len(resultado) != 0:
            return jsonify({"Error": "La habitacion no esta disponible en esas fechas"}), 400
        resultado = hoteles.habitacion_por_id(datos["id_habitacion"])
        if len(resultado) == 0:
            return jsonify({"Error": "El id de habitacion es inexistente"}), 404
        resultado = hoteles.ingresar_reserva(datos)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    return jsonify({"Exito": f"Los datos se cargaron exitosamente, el id de la reserva es {resultado}"}), 200

@app.route("/api/reserva/servicios/", methods=["POST"])
def ingresar_reserva_de_servicio():
    datos = request.get_json()
    keys = ("id_reserva", "id_servicio", "precio")
    for key in keys:
        if key not in datos:
            return jsonify({"Error": f"Falta el dato {key}"}), 400
    try:
        resultado_reserva = hoteles.obtener_reserva_por_id(datos["id_reserva"])
        resultado_servicio = hoteles.servicios_por_id(datos["id_servicio"])
        resultado_duplicados = hoteles.duplicados_reserva_servicio(datos["id_reserva"], datos["id_servicio"])
        if len(resultado_reserva) == 0:
            return jsonify({"Error": f"El id_reserva {datos["id_reserva"]} no existe."}), 404
        elif len(resultado_servicio) == 0:
            return jsonify({"Error": f"El id_servicio: {datos["id_servicio"]} no existe."}), 404
        elif len(resultado_duplicados) != 0:
            return jsonify({"Error": f"El servicio con id: {datos["id_servicio"]} ya se encuentra reservado para la reserva con id: {datos["id_reserva"]} "}), 404
        hoteles.reservar_servicio_por_id_reserva(datos)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return jsonify({"Exito": "Los datos se cargaron exitosamente"}), 200

#-----------------------------------------------------------#-----------------------#
#-------------RESERVAS DE HABITACION Y SERVICIOS------------#-------PUT------------#
#-----------------------------------------------------------#-----------------------#

@app.route("/api/reserva/<int:id>/<cliente>/", methods=["PUT"])
def actualizar_estado_reserva(id, cliente):
    try:
        resultado = hoteles.obtener_reserva_por_id_y_cliente(id, cliente)
        if len(resultado) == 0:
            return jsonify({"Error": "El id de reserva es inexistente."}), 404
        elif resultado[0][5] == "cancelado":
            return jsonify({"Error": "La reserva ya se encuentra cancelada"}), 400
        hoteles.cancelar_reserva(id, cliente)
        cancelar_reserva_servicios(id)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return jsonify({"Exito": f"El estado de la reserva paso a cancelado, asi como los servicio relacionados a esa reserva"}), 200

def comprobar_reserva_servicio(id_reserva):
    resultado = hoteles.obtener_reserva_por_id(id_reserva)
    if len(resultado) == 0:
        return jsonify({"Error": "El id_reserva no existe"}), 404
    resultado = hoteles.obtener_reserva_servicio_por_id_reserva(id_reserva)
    if len(resultado) == 0:
        return jsonify({"Error" : f"No hay servicios reservados con id {id_reserva}, o todos se encuentran cancelados"})
    return True
        
@app.route("/api/reserva/servicios/<int:id_reserva>", methods=["PUT"])
def cancelar_reserva_servicios(id_reserva):
    try:
        resultado = comprobar_reserva_servicio(id_reserva)
        if resultado == True:
            hoteles.cancelar_reserva_servicio_por_id_reserva(id_reserva)
        else:
            return resultado

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    return jsonify({"Aviso": "El estado de la reserva de servicios = cancelado"}), 200

@app.route("/api/reserva/servicios/<int:id_reserva>/<int:id_servicio>", methods=["PUT"])
def cancelar_reserva_servicio_individual(id_reserva, id_servicio):
    try:
        resultado = comprobar_reserva_servicio(id_reserva)
        if resultado == True:
            hoteles.cancelar_reserva_servicio_individual(id_reserva, id_servicio)
        else:
            return resultado
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    return jsonify({"message": "Servicio cancelado exitosamente"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=3648)

