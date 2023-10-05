from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    make_response,
    jsonify,
    url_for,
    session
)
from datetime import datetime

import jwt # https://pyjwt.readthedocs.io/en/stable/
from functools import wraps
from datetime import datetime, timedelta

import connection
from models import (
    Usuario,
    Producto,
    Proveedor,
    Pedido
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "1756524c-bdb2-4273-bbde-cd4d411763ca"
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if('jwt_token' in session):
            token = session.get('jwt_token')
        # return 401 if token is not passed
        if not token:
            return redirect(url_for('login'))
            #return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            current_user = connection.session.query(Usuario).filter_by(id=data['id']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated


@app.route('/', methods=['GET'])
def home(): 
    return render_template('home.html', context={})


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
        usuario = connection.session.query(Usuario).filter_by(email=email, password=password).first()

        token = jwt.encode({
            "id": str(usuario.id), 
            "email": usuario.email,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, app.config["SECRET_KEY"])

        session['jwt_token'] = token
        
        return redirect(url_for('dashboard'))
        # return make_response(jsonify({"token": token}), 201)
        

@app.route('/dashboard', methods=["GET", "POST"])
@token_required
def dashboard(user):
    if(request.method == "GET"):
        productos = connection.session.query(Producto).all()
        context = {
            "user": user, 
            "productos": productos
        }
        return render_template("dashboard.html", context=context)
    elif(request.method == 'POST'):
        pass

@app.route("/logout")
def logout():
    session.pop('jwt_token')
    return redirect(url_for('login'))


@app.route("/form-product", methods=["GET", "POST"])
# @token_required
def form_product():
    if(request.method == 'GET'):
        return render_template('form_productos.html')
    elif(request.method == 'POST'):    
        nombre = request.form.get('nombreProducto')
        description = request.form.get('descriptionProducto')
        precio = request.form.get('precioProducto')
        referencia = request.form.get('referenciaProducto')
        color = request.form.get('colorProducto')
        fecha_ingreso = request.form.get('fechaIngreso')
        fecha_entrega = request.form.get('fechaEntrega')
        producto = Producto(
            nombre=nombre,
            description=description,
            precio=precio,
            referencia=referencia,
            color=color,
            fecha_ingreso=datetime.strptime(fecha_ingreso, "%Y-%m-%d"),
            fecha_entrega=datetime.strptime(fecha_entrega, "%Y-%m-%d")
        )
        connection.session.add(producto)
        connection.session.commit()

        return redirect(url_for('dashboard'))

@app.route("/del-product/<id>")        
def del_product(id):
    product = connection.session.query(Producto).filter_by(id=int(id)).delete()
    connection.session.commit()
    return redirect(url_for('dashboard'))



########################################################

@app.route("/list-providers", methods=['GET'])
@token_required
def list_providers(user):
    if(request.method == "GET"):
        proveedores = connection.session.query(Proveedor).all()
        context = {
            "user": user, 
            "proveedores": proveedores
        }
        return render_template("proveedores.html", context=context)

@app.route("/add-providers", methods=["POST","GET"])
@token_required
def add_providers(id):
    return render_template("form_proveedores.html")


@app.route("/del-providers", methods=["POST"])
def del_providers(id):
    pass

@app.route("/update-providers", methods=["GET, PUT"])
def update_providers(id):
    pass

#########################################################

@app.route("/list-pedidos", methods=['GET'])
@token_required
def list_pedidos(user):
    if(request.method == "GET"):
        pedidos = connection.session.query(Pedido).all()
        context = {
            "user": user, 
            "pedidos": pedidos
        }
        return render_template("pedidos.html", context=context)

@app.route("/add-pedido", methods=["POST","GET"])
@token_required
def add_pedido(id):
    if(request.method == 'GET'):
        usuarios = connection.session.query(Usuario).all()
        productos = connection.session.query(Producto).all()
        context = {
            "users": usuarios,
            "productos": productos
        }
        return render_template("form_pedido.html", context = context)


@app.route("/del-pedido", methods=["POST"])
def del_pedido(id):
    if(request.method == 'POST'):
        usuarios = connection.session.query(Usuario).all()
        productos = connection.session.query(Producto).all()
        if productos
            connection.session.delete(product)
            connection.session.commit()
            flash("Producto eliminado con éxito", "success")
        else:
            flash("El producto no se encontró", "error")
        context = {
            "users": usuarios,
            "productos": productos
        }
        return render_template("form_pedido.html", context = context)

@app.route("/update-pedido", methods=["GET, PUT"])
def update_pedido(id):
    pass



if __name__ == '__main__':
    connection.Base.metadata.create_all(connection.engine)
    app.run(debug=True)
