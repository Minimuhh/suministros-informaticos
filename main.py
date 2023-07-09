from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    jsonify,
    url_for
)
import jwt
from functools import wraps
from datetime import datetime, timedelta

import connection
from models import Usuario

app = Flask(__name__)
app.config["SECRET_KEY"] = "1756524c-bdb2-4273-bbde-cd4d411763ca"
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Usuario.query.filter_by(nombre=data['nombre']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated



@app.route('/', methods=['GET'])
def home(): 
    return render_template('base.html', context={})


@app.route('/registrar', methods=['POST', 'GET'])
def registrar(): 
    if(request.method == "GET"): 
        return render_template('registration.html')
    elif(request.method == "POST"): 
        nombre = request.form.get('nameControl')
        apellido = request.form.get('apellidoControl')
        email = request.form.get("emailControl")
        telefono = request.form.get("telefonoControl")
        direccion = request.form.get("direccionControl")
        password = request.form.get('passwordControl')
        repeat_password = request.form.get('repeatPasswordControl')
        is_admin = True if request.form.get("adminControl") == 'on' else False
        
        if(password != repeat_password):
            return redirect('/registrar')
        usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            password=password,
            is_admin=is_admin
        )
        connection.session.add(usuario)
        connection.session.commit()

        return redirect("/login")

@app.route('/login', methods=['POST', 'GET'])
def login(): 
    if(request.method == "GET"):
        return render_template('login.html')
    elif(request.method == "POST"):
        email = request.form.get("emailControl")
        password = request.form.get("passwordControl")
        
        # usuario = connection.session.query(Usuario).filter_by(email=email).first()
        usuario = connection.session.query(Usuario).filter_by(email=email).first()
        print("usuario", usuario)
        token = jwt.JWT.encode({
            "id": str(usuario.id), 
            "email": usuario.email,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, app.config["SECRET_KEY"])
        
        return redirect("/dashboard", code=200, Response=token)
    

@app.route('/dashboard', methods=["GET", "POST"])
@token_required
def dashboard():

    return "Hey, estas logeºzado"


if __name__ == '__main__':

    # connection.Base.metadata.create_all(connection.engine)
    app.run(debug=True)

