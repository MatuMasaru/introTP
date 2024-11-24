from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "http://localhost:3648/api"


@app.route("/")
def index():
    try:
        response = requests.get(API_URL + "/hoteles")
        response.raise_for_status()
        hotels = response.json()
    except requests.exceptions.RequestException as e:
        hotels = []

    regions = []
    for hotel in hotels:
        region = hotel["region"]
        if region not in regions:
            regions.append(region)

    return render_template("index.html", hotels=hotels, regions=regions)


@app.route("/mi_reserva")
def mi_reserva():
    return render_template("login_mis_reservas.html")


@app.route("/informacion_reserva")
def informacion_reserva():
    return render_template("ver_mis_reservas.html")


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


@app.route('/admin')
def admin():
    try:
        response = requests.get(API_URL + "/hoteles")
        response.raise_for_status()
        hotels = response.json()
    except requests.exceptions.RequestException as e:
        hotels = []
    return render_template('admin.html',hotels=hotels)


@app.route('/admin/add_hotel', methods=['GET','POST'])
def admin_add_hotel():
    if request.method == "GET":
        return render_template('add_hotel.html')
    elif request.method == "POST":
        try:
            data = {
                    "nombre": request.form.get("fnombre"),
                    "direccion": request.form.get("fdireccion"),
                    "descripcion": request.form.get("fdescripcion"),
                    "url_img": request.form.get("furl_img"),
                    "region": request.form.get("fregion")
                }
            response = requests.post(API_URL + "/create_hotel", json=data)
            response.raise_for_status()    
        except requests.exceptions.RequestException as e:
            response = []

    return redirect(url_for('admin'))


@app.route('/admin/delete_hotel/<id_hotel>',methods=['GET'])
def admin_delete_hotel(id):
    try:
        hotel_data = {
            "id": id
        }
        response = requests.delete(API_URL + "/delete_hotel",json=hotel_data)
        response.raise_for_status()   
    except requests.exceptions.RequestException as e:
            response = []

    return redirect(url_for('admin'))


@app.route('/admin/update_hotel/<id_hotel>', methods=['GET','POST'])
def admin_update_hotel(id):
    if request.method == "GET":
        try:
            response = requests.get(API_URL + f'/hoteles/{id}')
            response.raise_for_status()
            hotel = response.json()       
            return render_template('update_hotel.html', hotel=hotel)
        except requests.exceptions.RequestException as e:
                hotel = []

    elif requests.method == "POST":
        try:
            data = {
                    "id": id,
                    "nombre": request.form.get("fnombre"),
                    "direccion": request.form.get("fdireccion"),
                    "descripcion": request.form.get("fdescripcion"),
                    "url_img": request.form.get("furl_img"),
                    "region": request.form.get("fregion")
                }
            response = requests.put(API_URL + "/update_hotel", json=data)
            response.raise_for_status()  
            return redirect(url_for('admin'))

        except requests.exceptions.RequestException as e:
            response = []

@app.route("/habitaciones", methods=["GET", "POST"])
def habitaciones():
    rooms = []

    if request.method == "POST":
        query_string = ""
        query = []
        if request.form.get("region") is not None:
            query.append(f"region={request.form.get('region')}")

        if request.form.get("dates") is not None:
            dates = request.form.get("dates").split(" a ")
            query.append(f"llegada={dates[0]}")
            query.append(f"salida={dates[1]}")

        if request.form.get("type") is not None:
            query.append(f"tipo={request.form.get('type')}")

        if len(query) > 0:
            query_string = "?" + "&".join(query)

        try:
            response = requests.get(
                API_URL + "/habitaciones/disponibles" + query_string
            )
            response.raise_for_status()
            rooms = response.json()
        except requests.exceptions.RequestException as e:
            rooms = []

        for room in rooms:
            try:
                response = requests.get(
                    API_URL + "/servicios/habitacion/" + str(room["id"])
                )
                response.raise_for_status()
                services = response.json()
            except requests.exceptions.RequestException as e:
                services = []

            room["servicios"] = services

    try:
        response = requests.get(API_URL + "/hoteles")
        response.raise_for_status()
        hotels = response.json()
    except requests.exceptions.RequestException as e:
        hotels = []

    regions = []
    for hotel in hotels:
        region = hotel["region"]
        if region not in regions:
            regions.append(region)

    room_types = ["suite", "familiar", "doble", "individual"]

    return render_template(
        "habitaciones.html", regions=regions, room_types=room_types, rooms=rooms
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
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
