from flask import Flask, render_template, request
from database import returnOsobaTableDict, addosobatodb, droposobaindp, raport1indb, raport2indb, raport3p1indb, raport3p2indb, returnStanicaTableDict

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


@app.route("/bosman/deleteosoba/delete", methods=['post'])
def donedeletosoba():
  idOsoba = request.form
  droposobaindp(idOsoba)
  print(idOsoba)
  return render_template('donedeleteosoba.html', osobadata=idOsoba)


@app.route("/bosman/raport1")
def raport1():
  return render_template('raport1.html', osobaTable=returnOsobaTableDict())


@app.route("/bosman/bosman/raport1/raport", methods=['post'])
def raport1raport():
  data = request.form
  result = raport1indb(data)
  result2 = result[0]
  return render_template('raport1raport.html', result=result2)


@app.route("/bosman/raport2")
def raport2():
  return render_template('raport2.html', osobaTable=returnOsobaTableDict())


@app.route("/bosman/bosman/raport2/raport", methods=['post'])
def raport2raport():
  data = request.form
  result = raport2indb(data)
  result2 = result[0]
  return render_template('raport2raport.html', result=result2)


@app.route("/bosman/raport3")
def raport3():
  return render_template('raport3.html', stanicaTable=returnStanicaTableDict())


@app.route("/bosman/bosman/raport3/raport", methods=['post'])
def raport3raport():
  raport3p1indb()
  data = request.form
  result = raport3p2indb(data)
  result2 = result[0]
  return render_template('raport3raport.html', result=result2)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
