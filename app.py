from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def helloWorld():
  return render_template('home.html')
@app.route("/członek")
def członek():
  return render_template('członek.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)