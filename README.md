Explicacion de como usar la api

Los GET devuelven: 

JSON = [{ 
“columna1”: dato, 
“columna2”: dato, 
..., 
“columnaN”: dato}
] 
Lista = [ {}, {}, {}, ..., {}] 
Individual = [{}] 

Los ERRORES U MSJ:

{ 
“tipo”: “descripcion” 
} 

Al enviar datos JSON en POST 
[{ 
“columna1”: dato, 
“columna2”: dato, 
..., 
“columnaN”: dato}
]

IMPORTANTE EN hoteles.py

#NOMBRE DE LA BASE DE DATOS hoteles

#pip install pymysql

#cambiar usuario y contraseña por el de ustedes:
    engine = create_engine('mysql+pymysql://usuario:constraseña@localhost:3306/hoteles')


.../api/hola/ 
    GET 
        Un saludo 

... /api/hoteles/ 
    GET 
        Una lista de hoteles, cada elemento es un hotel distinto 
    ERRORES 
        Interno (código: 500) 

.../api/hoteles/<id> 
    GET 
        El hotel relacionado al id 
    ERRORES 
        El id es inexistente (código:  404) 
        Interno (código: 500) 

.../api/servicios/ 
    GET 
        Una lista de servicios 
    ERRORES 
        Interno (código : 500) 

.../api/servicios/id 
    GET 
        El servicio relacionado al id 
    ERRORES 
        El id es inexistente (código: 404) 
        Interno (código: 500) 

.../api/servicios/hotel/id_hotel 
    GET 
        Devuelve servicios, tipos y precios relacionado al id_hotel
    ERRORES 
        No hay servicios incluidos en este hotel (código 400)
        El id es inexistente (código: 404) 
        Interno (código: 500) 

.../api/servicios/habitacion/id_habitacion 
    GET 
        Devuelve servicios, tipos y precios relacionado al id_habitacion
    ERRORES 
        No hay servicios incluidos en este hotel (código 400)
        El id es inexistente (código: 404) 
        Interno (código: 500)

.../api/habitaciones/id_hotel 
    GET 
        Una lista de habitaciones que tiene un hotel 
    ERRORES 
        El id es inexistente (código: 404) 
        Interno (código: 500) 

.../api/habitacion/id 
    GET 
        La habitacion relacionada al id 
    ERRORES 
        El id es inexistente (código: 404) 
        Interno (código: 500) 

.../api/reserva/id/cliente 
    GET 
        La información de la reserva 
    ERRORES 
        El id o el cliente es incorrecto. (código: 404) 
        Interno (código: 500) 

.../api/reserva/ 
    POST 
        Json con las keys = ('id_habitacion', 'llegada', 'salida', 'cliente_apellido', 'precio') 
        (Código: 200) ‘Los datos se cargaron exitosamente, el id de la reserva es id_reserva' 
    ERRORES 
        La habitacion no está disponible en esas fechas (código: 400) 
        El id de habitacion es inexistente (código: 404) 
        Interno (código: 500) 

.../api/reserva/id/cliente 
    PUT 
        Cambia el estado de la reserva a “cancelado”, en la reserva y los servicios relacionados a la reserva 
    ERRORES 
        Falta el dato {key} (código: 400) 
        El id o el cliente es inexistente. (código: 404) 
        La reserva ya se encuentra cancelada (código: 400) 
        Interno (código: 500) 

... /api/reserva/servicios/ 
    POST 
        Json con las keys = ('id_reserva', 'id_servicio', 'precio') 
    (Código: 200) Los datos se cargaron exitosamente 
    ERRORES 
        Falta el dato {key} (código: 400) 
        El id_reserva no existe (código: 404) 
        El id_servicio no existe (código: 404) 
        Interno (código: 500) 

... /api/reserva/servicios/<id_reserva> 
    GET     
        La información de la reserva de servicio 
    ERRORES 
        El id_reserva no existe. (código: 404) 
        No hay servicios reservados (código: 400) 
        Interno (código: 500) 

... /api/reserva/servicios/<id_reserva> 
    PUT 
        El estado de la reserva de servicio pasa a cancelado 
    ERRORES 
        El id_reserva no existe (código: 404) 
        La reserva ya se encuentra cancelada (código: 400) 
        Interno (código: 500) 
