from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import credit_controller
from db import create_tables

app = Flask(__name__)

app.secret_key = "tu_clave_secreta_super_segura"


@app.route('/')
def index():
    credits = credit_controller.get_credits()
    return render_template('index.html', credits=credits)

@app.route('/credits', methods=["GET"])
def get_credits():
    credits = credit_controller.get_credits()
    return jsonify(credits)

@app.route("/credit", methods=["POST"])
def insert_credit():
    cliente = request.form["cliente"]
    monto = float(request.form["monto"])  # Convertir a número
    tasa_interes = float(request.form["tasa_interes"])  # Convertir a número
    plazo = request.form["plazo"]
    fecha_otorgamiento = request.form["fecha_otorgamiento"]

    result = credit_controller.insert_credit(cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
    
    flash("Crédito guardado correctamente", "success")  # Mensaje de éxito
    return redirect(url_for("index"))  # Redirige al index

@app.route("/credit", methods=["PUT"])
def update_credit():
    credit_details = request.get_json()
    id = credit_details["id"]
    cliente = credit_details["cliente"]
    monto = credit_details["monto"]
    tasa_interes = credit_details["tasa_interes"]
    plazo = credit_details["plazo"]
    fecha_otorgamiento = credit_details["fecha_otorgamiento"]
    result = credit_controller.update_credit(id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
    return jsonify(result)

@app.route("/credit/<id>", methods=["DELETE"])
def delete_credit(id):
    result = credit_controller.delete_credit(id)
    return jsonify({"success": result})

@app.route("/credits/<id>", methods=["GET"])
def get_credit_by_id(id):
    credit = credit_controller.get_by_id(id)
    return jsonify(credit)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route("/credit_data")
def credit_data():
    data = credit_controller.get_credit_data()
    return jsonify(data)  # Retorna los datos en formato JSON

if __name__ == "__main__":
    create_tables()
    
    app.run(host='0.0.0.0', port=8000, debug=False)