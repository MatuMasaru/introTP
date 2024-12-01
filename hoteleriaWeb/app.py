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
    hotels = get_data("/hoteles")[:3]
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
        if not id_reserva.isdigit():
             return render_template("login_mis_reservas.html", error = "El ID de la reserva solo puede tener numeros.")
        sa = []
        try:

            response_reserva = requests.get(API_URL + f"/reserva/{id_reserva}/{apellido_cliente}")
            response_reserva.raise_for_status()
            reserva = response_reserva.json()
            servicios_reserva = get_data(f"/reserva/servicios/{id_reserva}")

            for s in servicios_reserva:
                sr = get_data(f"/servicios/{s['id_servicio']}")
                sa.append(sr[0]['servicio'])

            habitacion = get_data(f"/habitacion/{reserva[0]['id_habitacion']}")

            servicios_incluidos = get_data(f"/servicios/habitacion/{habitacion[0]['id']}")

            id_hotel = habitacion[0]['id_hotel']
            hotel = get_data(f"/hoteles/{id_hotel}")
        except requests.exceptions.RequestException as e:
            return render_template("login_mis_reservas.html", error = "El ID de la reserva o el apellido son incorrectos. Intente nuevamente.")
        except UnboundLocalError or IndexError as e:
             return render_template("error.html", error_code="500", error_description="Error del servidor"), 500
    return render_template("ver_mis_reservas.html", reserva = reserva, servicios_aparte = sa, servicios_incluidos = servicios_incluidos,habitacion = habitacion, hotel = hotel)


@app.route("/hoteles/<id_hotel>")
def hoteles(id_hotel):
    if not id_hotel.isdigit():
        return render_template("info_hotel.html", params = [], servicios = [])
    id_hotel = int(id_hotel)
    try:
            #------------------INFORMACION DE TODOS LOS HOTELES------------------
            if id_hotel == 0:

                hoteles = get_data("/hoteles")

                id_hoteles = [hotel["id"] for hotel in hoteles]
                servicios = []
                
                for id in id_hoteles:
                    servicios_hotel = get_data(f"/servicios/hotel/{id}")
                    for servicio in servicios_hotel:
                        servicio["id_hotel"] = id
                        servicios.append(servicio)
            else:
            #----------------------INFORMACION DE UN SOLO HOTEL----------------------
                hoteles = get_data(f"/hoteles/{id_hotel}")
                
                servicios_hotel = get_data(f"/servicios/hotel/{id_hotel}")
                servicios = []
                for servicio in servicios_hotel:
                    servicio["id_hotel"] = id_hotel
                    servicios.append(servicio)

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
    return render_template("error.html", error_code="404", error_description="Página no encontrada"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", error_code="500", error_description="Error del servidor"), 500


if __name__ == "__main__":
    app.run(debug=True)
