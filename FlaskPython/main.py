from flask import Flask, request

app = Flask(__name__)#importa la clase main.py

@app.route("/Home")
def hello():
    user_ip=request.remote_addr
    user= request.cookies
    return f"Hola MUNDO, tu ip es: {user_ip} , usuario: {user}"
app.run (host='0.0.0.0', port=8081, debug=True)
# python3 main.py    ---levanta el servidor de la pagina
    