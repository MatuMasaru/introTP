# TP - Introducción al Desarrollo de Software
.../api/hola/ 

GET un saludo 

... /api/hoteles/ 

GET una lista de hoteles, cada elemento es un hotel distinto 

ERRORES 

Interno (código: 500) 

.../api/hoteles/<id> 

GET el hotel relacionado al id 

ERRORES 

El id es inexistente (código:  404) 

Interno (código: 500) 

.../api/servicios/ 

GET una lista de servicios 

id, servicio, tipo 

ERRORES 

Interno (código : 500) 

.../api/servicios/id 

GET el servicio relacionado al id 

ERRORES 

El id es inexistente (código: 404) 

Interno (código: 500) 

.../api/servicios/hotel/id_hotel 

GET 

ERRORES 

El id es inexistente (código: 404) 

Interno (código: 500) 

.../api/servicios/habitacion/id_habitacion 

GET 

ERRORES 

El id es inexistente (código: 404) 

Interno (código: 500) 

.../api/habitaciones/id_hotel 

GET una lista de habitaciones que tiene un hotel 

ERRORES 

El id es inexistente (código: 404) 

Interno (código: 500) 

.../api/habitacion/id 

GET la habitacion relacionada al id 

ERRORES 

El id es inexistente (código: 404) 

Interno (código: 500) 

.../api/reserva/id/cliente 

GET la información de la reserva 

ERRORES 

El id o el cliente es incorrecto. (código: 404) 

Interno (código: 500) 

.../api/reserva/ 

POST json con las keys = ('id_habitacion', 'llegada', 'salida', 'cliente_apellido', 'precio') 

(Código: 200) ‘Los datos se cargaron exitosamente, el id de la reserva es id_reserva' 

ERRORES 

La habitacion no está disponible en esas fechas (código: 400) 

El id de habitacion es inexistente (código: 404) 

Interno (código: 500) 

.../api/reserva/id/cliente 

PUT cambia el estado de la reserva a “cancelado”, en la reserva y los servicios relacionados a la reserva 

ERRORES 

Falta el dato {key} (código: 400) 

El id o el cliente es inexistente. (código: 404) 

La reserva ya se encuentra cancelada (código: 400) 

Interno (código: 500) 

... /api/reserva/servicios/ 

POST json con las keys = ('id_reserva', 'id_servicio', 'precio') 

(Código: 200) Los datos se cargaron exitosamente 

ERRORES 

Falta el dato {key} (código: 400) 

El id_reserva no existe (código: 404) 

El id_servicio no existe (código: 404) 

Interno (código: 500) 

 

... /api/reserva/servicios/<id_reserva> 

GET la información de la reserva de servicio 

ERRORES 

El id_reserva no existe. (código: 404) 

No hay servicios reservados (código: 400) 

Interno (código: 500) 

... /api/reserva/servicios/<id_reserva> 

PUT el estado de la reserva de servicio pasa a cancelado 

ERRORES 

El id_reserva no existe (código: 404) 

La reserva ya se encuentra cancelada (código: 400) 

Interno (código: 500) 
