from flask import Flask, render_template, jsonify, request
from database import returnOsobaTableDict

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')


@app.route("/członek")
def członek():
  return render_template('członek.html')


@app.route("/admin")
def admin():
  return render_template('admin.html')


@app.route("/bosman")
def bosman():
  return render_template('bosman.html')


@app.route("/bosman/addosoba")
def addosoba():
  return render_template('addosoba.html')

@app.route("/bosman/bosman/addosoba/add", methods=['post'])
def addosobaAdd():
  data = request.form
  return jsonify(data)

@app.route("/bosman/listaosob")
def listaosob():
  return render_template('listaosob.html', osobaTable=returnOsobaTableDict())


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
