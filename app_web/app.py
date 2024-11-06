from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def index():    
    return render_template('characters.html')

@app.route('/reservas',methods=["GET","POST"])
def reservas():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        return redirect(url_for("detalle",nombre=nombre))
    return render_template('reservas.html')


@app.route('/detalle')
def detalle():
    return render_template('detalle.html')

if __name__=="__main__":
    app.run(debug=True)
