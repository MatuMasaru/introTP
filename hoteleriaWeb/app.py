from flask import Flask, render_template, request
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


@app.route("/hoteles/<id_hotel>")
def hoteles(id_hotel):
    id_hotel = int(id_hotel)
    hotels = [
        {
            "id": 1,
            "image_url": "static/assets/hotel-buenos-aire.jpg",
            "name": "Buenos Aires",
            "ubication": "Avenida de Mayo 123",
            "description": "Ubicado en el corazón de la vibrante capital, nuestro hotel ofrece un oasis de tranquilidad en medio del bullicio urbano. Ideal para viajeros de negocios y turistas por igual.",
            "link": "#inicio",
            "services": ["Gimnasio", "Spa", "Sauna", "Mesas de Pool", "Piscina"],
        },
        {
            "id": 2,
            "image_url": "static/assets/hotel-mar-del-plata.jpg",
            "name": "Mar del Plata",
            "ubication": "Av. de Los Trabajadores 3100",
            "description": "Perfecto para quienes buscan la combinación ideal de playa y ciudad. Disfrute del sol, la arena y las actividades culturales que esta hermosa ciudad costera tiene para ofrecer.",
            "link": "#inicio",
            "services": ["Gimnasio", "Spa", "Piscina"],
        },
        {
            "id": 3,
            "image_url": "static/assets/hotel-bariloche.jpg",
            "name": "Bariloche",
            "ubication": "Cerro Catedral 1450",
            "description": "Situado en el pintoresco escenario de la Patagonia, este hotel es ideal para los amantes de la naturaleza y los deportes de invierno. Disfrute de vistas impresionantes, actividades al aire libre y la hospitalidad cálida de siempre.",
            "link": "#inicio",
            "services": ["Gimnasio", "Sauna", "Mesas de Pool", "Piscina"],
        },
    ]

    if id_hotel == 0:
        return render_template("info_hotel.html", params=hotels)
    params = []
    params.append(hotels[id_hotel])

    return render_template("info_hotel.html", params=params)


@app.route("/habitaciones", methods=['GET','POST'])
def habitaciones():
    try:
        if request.method == "POST":
            region = "" if request.form.get("region") is None else request.form.get("region")
            tipo = "" if request.form.get("tipo") is None else request.form.get("tipo")
            if region == "" and tipo == "":
                response  = requests.get(API_URL + "/habitaciones")
                response.raise_for_status()
                habitaciones = response.json()
            elif region == "" and tipo != "":
                response  = requests.get(API_URL + "/habitaciones/" + tipo)
                response.raise_for_status()
                habitaciones = response.json()
            elif region != "" and tipo == "":
                response  = requests.get(API_URL + "/hoteles/" + region)
                response.raise_for_status()
                hoteles = response.json()
                response  = requests.get(API_URL + "/habitaciones/" + str(hoteles[0]['id']))
                response.raise_for_status()
                habitaciones = response.json()
            else:
                response = requests.get(API_URL + "/habitacion/" + tipo + "/" + region)
                response.raise_for_status()
                habitaciones = response.json()
        else:
            response  = requests.get(API_URL + "/habitaciones")
            response.raise_for_status()
            habitaciones = response.json()
    except requests.exceptions.RequestException as e:
        habitaciones = []
    return render_template("habitaciones.html", rooms=habitaciones)


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
