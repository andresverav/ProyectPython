from flask import Flask, request, make_response, redirect

app = Flask(__name__)#importa la clase main.py

@app.route("/Index")
def index():
    user_ip_information=request.remote_addr
    response= make_response(redirect("/show_information_addres")) #Redirecciona pagina
    response.set_cookie("user_ip_information", user_ip_information)
    return response

@app.route("/show_information_addres")
def sohw_informatio():
    user_ip=request.cookies.get("user_ip_information") #captura objeto request y toma variable creada
    return f"Hola MUNDO, tu ip es: {user_ip} "

app.run (host='0.0.0.0', port=8081, debug=True)
# python3 main.py    ---levanta el servidor de la pagina
    