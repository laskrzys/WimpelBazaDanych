from flask import Flask, render_template
from database import returnOsobaTableDict

app = Flask(__name__)
@app.route("/")
def home():
  return render_template('home.html')
@app.route("/członek")
def członek():
  return render_template('członek.html')
@app.route("/listaosob")
def listaosob():
  return render_template('listaosob.html',
                        osobaTable=returnOsobaTableDict())
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)