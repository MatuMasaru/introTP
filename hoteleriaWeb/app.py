from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://localhost:3648/api"


def get_data(endpoint):
    try:
        response = requests.get(API_URL + endpoint)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = []

    return data


@app.route("/")
def index():
    hotels = get_data("/hoteles")
    regions = get_data("/hoteles/regiones")

    return render_template("index.html", hotels=hotels, regions=regions)


@app.route("/mi_reserva")
def mi_reserva():
    return render_template("login_mis_reservas.html", error = " ")


@app.route("/informacion_reserva", methods = ['POST' , 'GET'])
def informacion_reserva():
    if request.method == "POST":
        id_reserva = request.form.get("nreserva")
        apellido_cliente = request.form.get("acliente")
        if len(id_reserva) == 0  or len(apellido_cliente) == 0:
            return render_template("login_mis_reservas.html", error = "Complete los campos para continuar.")
        if not id_reserva.isdigit():
             return render_template("login_mis_reservas.html", error = "El ID de la reserva solo puede tener numeros.")
        sa = []
        try:

            response_reserva = requests.get(API_URL + f"/reserva/{id_reserva}/{apellido_cliente}")
            response_reserva.raise_for_status()
            reserva = response_reserva.json()
                
            response_servicios_reserva = requests.get(API_URL + f"/reserva/servicios/{id_reserva}")
            response_servicios_reserva.raise_for_status()
            servicios_aparte = response_servicios_reserva.json()
            for s in servicios_aparte:
                response_sa = requests.get(API_URL + f"/servicios/{s['id_servicio']}")
                response_sa.raise_for_status()
                rsa = response_sa.json()
                sa.append(rsa[0]['servicio'])

            response_habitacion = requests.get(API_URL + f"/habitacion/{reserva[0]['id_habitacion']}")
            response_habitacion.raise_for_status()
            habitacion = response_habitacion.json()

            response_servicios_por_habitacion = requests.get(API_URL + f"/servicios/habitacion/{habitacion[0]['id']}")
            response_servicios_por_habitacion.raise_for_status()
            servicios_incluidos = response_servicios_por_habitacion.json()

            id_hotel = habitacion[0]['id_hotel']
            response_hotel = requests.get(API_URL + f"/hoteles/{id_hotel}")
            response_hotel.raise_for_status()
            hotel = response_hotel.json()

        except requests.exceptions.RequestException as e:
            return render_template("login_mis_reservas.html", error = "Hubo un error en la busqueda. Intente nuevamente.")
        
    return render_template("ver_mis_reservas.html", reserva = reserva, servicios_aparte = sa, servicios_incluidos = servicios_incluidos,habitacion = habitacion, hotel = hotel)


@app.route("/hoteles")
@app.route("/hoteles/<id_hotel>")
def hoteles(id_hotel):
    id_hotel = int(id_hotel)
    try:
            #------------------INFORMACION DE TODOS LOS HOTELES------------------
            if id_hotel == 0:

                response_todos_los_hoteles = requests.get(API_URL + "/hoteles")
                response_todos_los_hoteles.raise_for_status()
                hoteles = response_todos_los_hoteles.json()

                response_todos_los_servicios = requests.get(API_URL + "/servicios")
                response_todos_los_servicios.raise_for_status()
                servicios = response_todos_los_servicios.json()

            else:
            #----------------------INFORMACION DE UN SOLO HOTEL----------------------
                response_hotel = requests.get(API_URL + f"/hoteles/{id_hotel}")
                response_hotel.raise_for_status()
                hoteles = response_hotel.json()
                
                response_servicio_hotel = requests.get(API_URL + f"/servicios/hotel/{id_hotel}")
                response_servicio_hotel.raise_for_status()
                servicios = response_servicio_hotel.json()

    except requests.exceptions.RequestException as e:
        params = []
        servicios = []
    params = []
    for hotel in hoteles:
            if hotel not in params:
                params.append(hotel)
                
    return render_template("info_hotel.html", params = params, servicios = servicios)


@app.route("/habitaciones", methods=["GET", "POST"])
def habitaciones():
    rooms = []
    meta_region = ""
    meta_start_date = ""
    meta_end_date = ""
    meta_room_type = ""

    if request.method == "POST":
        query_string = ""
        query = []
        if request.form.get("region") is not None:
            meta_region = request.form.get("region")
            query.append(f"region={meta_region}")

        if request.form.get("dates") is not None:
            dates = request.form.get("dates").split(" a ")
            meta_start_date = dates[0]
            meta_end_date = dates[1]
            query.append(f"llegada={meta_start_date}")
            query.append(f"salida={meta_end_date}")

        if request.form.get("type") is not None:
            meta_room_type = request.form.get("type")
            query.append(f"tipo={meta_room_type}")

        if len(query) > 0:
            query_string = "?" + "&".join(query)

        rooms = get_data("/habitaciones/disponibles" + query_string)

        for room in rooms:
            room["servicios"] = get_data("/servicios/habitacion/" + str(room["id"]))

    regions = get_data("/hoteles/regiones")
    room_types = get_data("/habitaciones/tipos/")

    return render_template(
        "habitaciones.html",
        regions=regions,
        room_types=room_types,
        rooms=rooms,
        meta_region=meta_region,
        meta_start_date=meta_start_date,
        meta_end_date=meta_end_date,
        meta_room_type=meta_room_type
    )


@app.route("/reservar/<id_room>")
def reservar(id_room):
    rooms = {
        "0": {"id_hotel": 0, "number": 150, "persons": 4, "price": 40000},
        "1": {"id_hotel": 2, "number": 300, "persons": 4, "price": 40000},
    }
    return render_template("reservas.html", room = rooms[id_room], id_room=id_room)


@app.errorhandler(404)
def page_notfound(e):
    return render_template("error.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html"), 500
if __name__ == "__main__":
    app.run(debug=True)
