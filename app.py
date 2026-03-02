from flask import Flask, render_template, request, jsonify, make_response, session

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/ventas')
def ventas():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005366_usr",
        password="!|F>1$H1p",
        database="u760464709_24005366_bd"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Ventas")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

@app.post('/ventas')
def ventas():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005366_usr",
        password="!|F>1$H1p",
        database="u760464709_24005366_bd"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO Ventas (ciudad, estado, codigo_postal, referencia) VALUES (%s, %s, %s, %s)"
    val = (request.form['ciudad'], request.form['estado'], request.form['codigo_postal'], request.form['referencia'])
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"
