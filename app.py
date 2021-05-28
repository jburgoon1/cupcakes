"""Flask app for Cupcakes"""
from flask import Flask, jsonify,request, render_template, redirect
from models import Cupcake, connect_db, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cupcakeapp'

connect_db(app)

@app.route('/')
def show_home():
    cupcakes = Cupcake.query.all()

    return render_template('home.html', cupcakes = cupcakes)

@app.route('/api/cupcakes')
def show_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcake = [cake.serialize() for cake in cupcakes]
    return jsonify(cupcakes = cupcake)

@app.route('/api/cupcakes/<int:id>')
def show_details(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods = ['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor =request.json.get('flavor', cupcake.flavor) 
    cupcake.size = request.json.get('size', cupcake.size) 
    cupcake.rating = request.json.get('rating', cupcake.rating) 
    cupcake.image = request.json.get('image', cupcake.image) 
    db.session.commit()
    return jsonify(cupcake.serialize())
@app.route('/api/cupcakes/<int:id>', methods = ['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = 'Cupcake Deleted')

@app.route('/api/cupcakes', methods = ['POST'])
def add_cupcake():
    flavor =request.json.get('flavor') 
    size = request.json.get('size') 
    rating = request.json.get('rating') 
    image = request.json.get('image') 
    new_cupcake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake = new_cupcake.serialize()), 201)

