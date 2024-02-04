from flask import Flask, redirect, url_for, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return "Practicando con Flask"

@app.route('/información')
@app.route('/información/<nombre>')
@app.route('/información/<nombre>/<apellidos>')
def informacion(nombre = None, apellidos = None):
    
    texto = ""
    if nombre != None and apellidos != None:
        texto = f"<p3> Bienvenido, {nombre} {apellidos} </p3>"
        
    return f"""
            <h1>Página de información </h1>
            <p> Esta es la página de información</p>
            {texto}         
            """

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def  contacto(redireccion = None):
    
    if redireccion != None:
        return redirect(url_for('lenguajes'))
    
    return "<h1> Página de contacto </h1>"

@app.route('/lenguajes-de-programación')
def lenguajes():
    return "<h1> Página de lenguajes </h1>"

if __name__ == '__main__':
        app.run(debug=True)