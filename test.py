from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length
import webbrowser
import threading

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pompeya.db"
app.config["SECRET_KEY"] = "some secret passwd"
db = SQLAlchemy(app)

class Desmechados(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	desmechados = db.Column(db.String(220),unique=False,nullable=False)
	cantidadyMesa = db.Column(db.String(220),unique=False,nullable=True)
	agregados = db.Column(db.String(220),unique=False,nullable=False)

class Hamburguesas(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	hamburguesas = db.Column(db.String(220),unique=False,nullable=False)
	cantidadyMesa2 = db.Column(db.String(220),unique=False,nullable=True)
	agregados2 = db.Column(db.String(220),unique=False,nullable=False)

class Lomitos(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	lomitos = db.Column(db.String(220),unique=False,nullable=False)
	cantidadyMesa3 = db.Column(db.String(220),unique=False,nullable=True)
	agregados3 = db.Column(db.String(220),unique=False,nullable=False)

class Pizzas(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	pizzas = db.Column(db.String(220),unique=False,nullable=False)
	agregados4 = db.Column(db.String(220),unique=False,nullable=False)
	cantidadyMesa4 = db.Column(db.String(220),unique=False,nullable=True)

class Faltantes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	faltante = db.Column(db.String(150),nullable=False)
	cantidad = db.Column(db.Integer,nullable=False)

class Stock(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	en_stock = db.Column(db.String(150),nullable=False)
	cantidad2 = db.Column(db.String(300),nullable=False)

class produccionForm(FlaskForm):
	desmechados = SelectField("Desmechados", choices=[('p/de carne', 'p/de carne'), ('p/de cerdo', 'p/de cerdo'), ('p/de pollo', 'p/de pollo'), ('p/de cordero', 'p/de cordero')])
	agregados = SelectField("Agregados", choices=[('ninguno', 'ninguno'),('huevo', 'huevo'), ('queso', 'queso'), ('panceta', 'panceta')])
	cantidadyMesa = StringField(label="Cantidad/Mesa")
	añadir = SubmitField()

class hamburguesasForm(FlaskForm):
	hamburguesas = SelectField("Hamburguesas", choices=[('h/simple', 'h/simple'), ('h/doble chesse', 'h/doble chesse'), ('h/la paraguaya', 'h/la paraguaya'),('h/oklahoma style', 'h/oklahoma style')],validators=[DataRequired(),Length(min=2,max=220)])
	agregados2 = SelectField("Agregados", choices=[('ninguno', 'ninguno'),('huevo', 'huevo'), ('queso', 'queso'), ('panceta', 'panceta')],validators=[DataRequired(),Length(min=2,max=220)])
	cantidadyMesa2 = StringField(label="Cantidad/Mesa")
	añadir = SubmitField()

class lomitosForm(FlaskForm):
	lomitos = SelectField("Lomitos", choices=[('s/lomito/carne', 's/lomito/carne'), ('s/lomito/pollo', 's/lomito/pollo'),('arabe/carne', 'arabe/carne'),('arabe/pollo', 'arabe/pollo'),('arabe/mixto', 'arabe/mixto')],validators=[DataRequired(),Length(min=2,max=220)])
	agregados3 = SelectField("Tipo", choices=[('simple', 'simple'), ('completo', 'completo')],validators=[DataRequired(),Length(min=2,max=220)])
	cantidadyMesa3 = StringField(label="Cantidad/Mesa")
	añadir = SubmitField()

class pizzasForm(FlaskForm):
	pizzas = SelectField("Pizzas", choices=[('muzzarella', 'muzzarella'), ('pepperoni', 'pepperoni'),('margarita', 'margarita'),('pepperoni', 'pepperoni'),('pollo con katupiry', 'pollo con katupiry')],validators=[DataRequired(),Length(min=2,max=220)])
	agregados4 = SelectField("Tipo", choices=[('masa normal', 'masa normal'), ('borde relleno', 'borde relleno')],validators=[DataRequired(),Length(min=2,max=220)])
	cantidadyMesa4 = StringField(label="Cantidad/Mesa")
	añadir = SubmitField()

class faltantesForm(FlaskForm):
	faltante = StringField(label="Producto:",validators=[DataRequired(),Length(min=1,max=150)])
	cantidad = IntegerField(label="Cantidad:",validators=[DataRequired()])
	añadir = SubmitField()

class stockForm(FlaskForm):
	en_stock = StringField(label="Producto:",validators=[DataRequired(),Length(min=2,max=150)])
	cantidad2 = StringField(label="Cantidad",validators=[DataRequired(),Length(min=1,max=300)])
	añadir = SubmitField()

@app.route("/produccion",methods=["POST","GET"])
def produccion():
	form = produccionForm()
	form2 = hamburguesasForm()
	form3 = lomitosForm()
	form4 = pizzasForm()
	productoTotal = Desmechados.query.all()
	hamburguesasTotal = Hamburguesas.query.all()
	lomitosTotal = Lomitos.query.all()
	pizzasTotal = Pizzas.query.all()
	if form.validate_on_submit():
		add_product = Desmechados(desmechados=form.desmechados.data,agregados=form.agregados.data,cantidadyMesa=form.cantidadyMesa.data)
		db.session.add(add_product)
		db.session.commit()
		form.agregados.data = ""
		form.desmechados.data = ""
		form.cantidadyMesa.data = ""
		return redirect(url_for("produccion"))
	
	if form2.validate_on_submit():
		add_product2 = Hamburguesas(hamburguesas=form2.hamburguesas.data,agregados2=form2.agregados2.data,cantidadyMesa2=form2.cantidadyMesa2.data)
		db.session.add(add_product2)
		db.session.commit()
		form2.hamburguesas.data = ""
		form2.agregados2.data = ""
		form2.cantidadyMesa2.data = ""
		return redirect(url_for("produccion"))
	
	if form3.validate_on_submit():
		add_product3 = Lomitos(lomitos=form3.lomitos.data,agregados3=form3.agregados3.data,cantidadyMesa3=form3.cantidadyMesa3.data)
		db.session.add(add_product3)
		db.session.commit()
		form3.lomitos.data = ""
		form3.agregados3.data = ""
		form3.cantidadyMesa3.data = ""
		return redirect(url_for("produccion"))
	
	if form4.validate_on_submit():
		add_product4 = Pizzas(pizzas=form4.pizzas.data,cantidadyMesa4=form4.cantidadyMesa4.data,agregados4=form4.agregados4.data)
		db.session.add(add_product4)
		db.session.commit()
		form4.pizzas.data = ""
		form4.cantidadyMesa4.data = ""
		form4.agregados4.data = ""
		return redirect(url_for("produccion"))

	return render_template("produccion.html",form=form,form2=form2,form3=form3,form4=form4,pizzasTotal=pizzasTotal,lomitosTotal=lomitosTotal,hamburguesasTotal=hamburguesasTotal,productoTotal=productoTotal)

@app.route("/faltantes",methods=["POST","GET"])
def faltantes():
	form = faltantesForm()
	faltantesTotal = Faltantes().query.all()
	if form.validate_on_submit():
		add_product = Faltantes(faltante=form.faltante.data,cantidad=form.cantidad.data)
		db.session.add(add_product)
		db.session.commit()
		form.faltante.data = ""	
		form.cantidad.data = ""	
		return redirect(url_for("faltantes"))
	return render_template("faltantes.html",form=form,faltantesTotal=faltantesTotal)

@app.route("/stock",methods=["POST","GET"])
def stock():
	form = stockForm()
	stockTotal = Stock().query.all()
	if form.validate_on_submit():
		add_product = Stock(en_stock=form.en_stock.data,cantidad2=form.cantidad2.data)
		db.session.add(add_product)
		db.session.commit()
		form.en_stock.data = ""	
		form.cantidad2.data = ""	
		return redirect(url_for("stock"))
	return render_template("stock.html",form=form,stockTotal=stockTotal)

#DESMECHADOS
@app.route("/update/<int:id>",methods=["POST","GET"])
def update1(id):
	product_to_update = Desmechados.query.get_or_404(id)
	form = produccionForm()
	if request.method == "POST":
		product_to_update.desmechados = request.form["desmechados"]
		product_to_update.agregados = request.form["agregados"]
		product_to_update.cantidadyMesa = request.form["cantidadyMesa"]
		try:
			db.session.commit()
			return redirect(url_for("produccion"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("update.html",product_to_update=product_to_update,form=form)
	return render_template("update.html",product_to_update=product_to_update,form=form)

@app.route("/delete/<int:id>")
def delete(id):
	product_to_delete = Desmechados.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("produccion"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")

#HAMBURGUESAS
@app.route("/hamburguesasA/<int:id>",methods=["POST","GET"])
def hamburguesasA(id):
	product_to_update = Hamburguesas.query.get_or_404(id)
	form = hamburguesasForm()
	if request.method == "POST":
		product_to_update.hamburguesas = request.form["hamburguesas"]
		product_to_update.agregados2 = request.form["agregados2"]
		product_to_update.cantidadyMesa2 = request.form["cantidadyMesa2"]
		try:
			db.session.commit()
			return redirect(url_for("produccion"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("hamburguesasA.html",product_to_update=product_to_update,form=form)
	return render_template("hamburguesasA.html",product_to_update=product_to_update,form=form)

@app.route("/hamburguesasD/<int:id>")
def hamburguesasD(id):
	product_to_delete = Hamburguesas.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("produccion"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")

#LOMITOS
@app.route("/lomitosA/<int:id>",methods=["POST","GET"])
def lomitosA(id):
	product_to_update = Lomitos.query.get_or_404(id)
	form = lomitosForm()
	if request.method == "POST":
		product_to_update.lomitos = request.form["lomitos"]
		product_to_update.agregados3 = request.form["agregados3"]
		product_to_update.cantidadyMesa3 = request.form["cantidadyMesa3"]
		try:
			db.session.commit()
			return redirect(url_for("produccion"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("lomitosA.html",product_to_update=product_to_update,form=form)
	return render_template("lomitosA.html",product_to_update=product_to_update,form=form)

@app.route("/lomitosD/<int:id>")
def lomitosD(id):
	product_to_delete = Lomitos.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("produccion"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")

#PIZZAS
@app.route("/pizzasA/<int:id>",methods=["POST","GET"])
def pizzasA(id):
	product_to_update = Pizzas.query.get_or_404(id)
	form = pizzasForm()
	if request.method == "POST":
		product_to_update.pizzas = request.form["pizzas"]
		product_to_update.cantidadyMesa4 = request.form["cantidadyMesa4"]
		product_to_update.agregados4 = request.form["agregados4"]
		try:
			db.session.commit()
			return redirect(url_for("produccion"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("pizzasA.html",product_to_update=product_to_update,form=form)
	return render_template("pizzasA.html",product_to_update=product_to_update,form=form)

@app.route("/pizzasD/<int:id>")
def pizzasD(id):
	product_to_delete = Pizzas.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("produccion"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")

'''
Esta ruta sirve para actualizar y borrar el stock
'''
@app.route("/update2/<int:id>",methods=["POST","GET"])
def update2(id):
	product_to_update = Stock.query.get_or_404(id)
	form = stockForm()
	if request.method == "POST":
		product_to_update.en_stock = request.form["en_stock"]
		product_to_update.cantidad2 = request.form["cantidad2"]
		try:
			db.session.commit()
			return redirect(url_for("stock"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("update2.html",product_to_update=product_to_update,form=form)
	return render_template("update2.html",product_to_update=product_to_update,form=form)

@app.route("/delete2/<int:id>")
def delete2(id):
	product_to_delete = Stock.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("stock"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")
'''
Esta ruta sirve para actualizar los faltantes
'''
@app.route("/update3/<int:id>",methods=["POST","GET"])
def update3(id):
	product_to_update = Faltantes.query.get_or_404(id)
	form = faltantesForm()
	if request.method == "POST":
		product_to_update.faltante = request.form["faltante"]
		product_to_update.cantidad = request.form["cantidad"]
		try:
			db.session.commit()
			return redirect(url_for("faltantes"))
		except:
			#tiene que ser con flash messages
			print("Algo ha salido mal...")
	else:
		return render_template("update3.html",product_to_update=product_to_update,form=form)
	return render_template("update3.html",product_to_update=product_to_update,form=form)

@app.route("/delete3/<int:id>")
def delete3(id):
	product_to_delete = Faltantes.query.get_or_404(id)
	try:
		db.session.delete(product_to_delete)
		db.session.commit()
		return redirect(url_for("faltantes"))
	except:
		#añadir aqui un flash 
		print("somenthing failed")

@app.route("/")
def index():
	produccion = Desmechados().query.all()
	produccion2 = Hamburguesas().query.all()
	produccion3 = Lomitos().query.all()
	produccion4 = Pizzas.query.all()
	faltantes = Faltantes().query.all()
	stock = Stock().query.all()
	return render_template("index.html",produccion=produccion,produccion2=produccion2,produccion3=produccion3,produccion4=produccion4,faltantes=faltantes,stock=stock)

def open_browser():
	webbrowser.open("http://localhost:5000",new=1)

if __name__ == "__main__":
	threading.Timer(1,open_browser).start()
	app.run(debug=True)

