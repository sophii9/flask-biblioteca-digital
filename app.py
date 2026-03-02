from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005366_usr",
        password="!|F>1$H1p",
        database="u760464709_24005366_bd"
    )

@app.route('/ventas', methods=["GET", "POST"])
def ventas():
    mydb = get_connection()
    mycursor = mydb.cursor()

    if request.method == "GET":
        mycursor.execute("SELECT * FROM Ventas")
        myresult = mycursor.fetchall()
        return make_response(jsonify(myresult))

    elif request.method == "POST":
        sql = "INSERT INTO Ventas (ciudad, estado, codigo_postal, referencia) VALUES (%s, %s, %s, %s)"
        val = (request.form['ciudad'], request.form['estado'], request.form['codigo_postal'], request.form['referencia'])
        mycursor.execute(sql, val)
        mydb.commit()
        return make_response(jsonify({"estado": "ok"}))
