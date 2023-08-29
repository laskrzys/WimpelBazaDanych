from flask import Flask, render_template, request
from database import returnOsobaTableDict, addosobatodb, droposobaindp

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
def doneaddosoba():
  data = request.form
  addosobatodb(data)
  return render_template('doneaddosoba.html', osobadata=data)

@app.route("/bosman/listaosob")
def listaosob():
  return render_template('listaosob.html', osobaTable=returnOsobaTableDict())

@app.route("/bosman/deleteosoba")
def deleteosoba():
  return render_template('deleteosoba.html', osobaTable=returnOsobaTableDict())

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
