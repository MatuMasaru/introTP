from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    hotels = [
        {
            "id": 1,
            "image_url": "static/assets/hotel-bariloche.jpg",
            "name": "Buenos Aires",
            "description": "Ubicado en el corazón de la vibrante capital, nuestro hotel ofrece un oasis de tranquilidad en medio del bullicio urbano. Ideal para viajeros de negocios y turistas por igual.",
            "link": "#inicio",
        },
        {
            "id": 2,
            "image_url": "static/assets/hotel-bariloche.jpg",
            "name": "Mar del Plata",
            "description": "Perfecto para quienes buscan la combinación ideal de playa y ciudad. Disfrute del sol, la arena y las actividades culturales que esta hermosa ciudad costera tiene para ofrecer.",
            "link": "#inicio",
        },
        {
            "id": 3,
            "image_url": "static/assets/hotel-bariloche.jpg",
            "name": "Bariloche",
            "description": "Situado en el pintoresco escenario de la Patagonia, este hotel es ideal para los amantes de la naturaleza y los deportes de invierno. Disfrute de vistas impresionantes, actividades al aire libre y la hospitalidad cálida de siempre.",
            "link": "#inicio",
        },
    ]
    return render_template("index.html", hotels=hotels)


@app.route("/mi_reserva")
def mi_reserva():
    return render_template('ver_mis_reservas.html')


@app.route("/hoteles")
def hoteles():
    return render_template('info_hotel.html')

@app.errorhandler(404)
def page_notfound(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
