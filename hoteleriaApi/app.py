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

@app.route("/api/habitaciones/tipos/", methods=["GET"])
def obtener_los_tipos_habitacion():
    try:
        resultado = hoteles.todos_los_tipos_de_habitacion()
        if len(resultado) == 0:
            return jsonify({"Error": "No hay tipos de habitaciones"}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    respuesta = []
    for fila in resultado:
        respuesta.append(fila[0])
    return jsonify(respuesta), 200

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
    
    return jsonify({"Exito": f"Los datos se cargaron exitosamente, el id de la reserva es {resultado}", "id_reserva": f"{resultado}" }), 200


@app.route("/api/servicio/<int:id_reserva>/<int:id_servicio>", methods=["POST"])
def ingresar_reserva_de_servicio(id_reserva, id_servicio):
    try:
        # verifica que el id existe
        resultado_reserva = hoteles.obtener_reserva_por_id(id_reserva)
        if len(resultado_reserva) == 0:
            return jsonify({"Error": "El id_reserva no existe."}), 404
        
        # Verifica si el servicio existe
        resultado_servicio = hoteles.servicios_por_id(id_servicio)
        if len(resultado_servicio) == 0:
            return jsonify({"Error": "El id_servicio no existe."}), 404
        
        # Verificar para no ingresar dos veces los mismos datos        
        resultado = hoteles.verificar_reserva_servicio(id_reserva, id_servicio)
        
        # Aquí verificamos que resultado no esté vacío antes de acceder a sus elementos
        if len(resultado) != 0:
            return jsonify({"Error": "La reserva ya se encuentra agregada"}), 400
        
        # Reservar el servicio
        hoteles.reservar_servicio_por_id_reserva(id_reserva, id_servicio)
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    # Responde que la reserva fue exitosa
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
        eliminar_reserva_servicios(id)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    return jsonify({"Exito": f"El estado de la reserva paso a cancelado, y se eliminaron los servicios de la reserva"}), 200

#-----------------------------------------------------------#-----------------------#
#-------------RESERVAS DE HABITACION Y SERVICIOS------------#-------DELETE------------#
#-----------------------------------------------------------#-----------------------#

@app.route("/api/reserva/servicios/<int:id_reserva>", methods=["DELETE"])
def eliminar_reserva_servicios(id_reserva):
    try:
        resultado = hoteles.obtener_reserva_por_id(id_reserva)
        if len(resultado) == 0:
            return jsonify({"Error": "El id_reserva no existe"}), 404
        resultado = hoteles.obtener_reserva_servicio_por_id_reserva(id_reserva)
        if len(resultado) == 0:
            return jsonify({"Error" : f"No hay servicios reservados con id {id_reserva}"})
        
        hoteles.eliminar_reserva_servicio_por_id_reserva(id_reserva)

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    return jsonify({"Aviso": f"servicios eliminados de id_reserva: {id_reserva}"}), 200

@app.route("/api/reserva/servicio/<int:id_reserva>/<int:id_servicio>", methods=["DELETE"])
def eliminar_un_solo_servicio(id_reserva, id_servicio):
    try:
        resultado_servicio = hoteles.servicios_por_id(id_servicio)
        if len(resultado_servicio) == 0:
            return jsonify({"Error": "El id_servicio no existe"}), 404
        
        resultado = hoteles.verificar_reserva_servicio(id_reserva,id_servicio)
        if len(resultado) == 0:
            return jsonify({"Error": "Su reserva del servicio no se encuentra registrada"}),400
        
        hoteles.eliminar_un_solo_servicio(id_reserva, id_servicio)

        return jsonify({"Mensaje": "Servicio cancelado exitosamente"}), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=3648)

