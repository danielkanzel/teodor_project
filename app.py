import os
import random
from flask import Flask, request, render_template, redirect, url_for, session, flash, abort
from flask_sqlalchemy import SQLAlchemy

# Flask config
app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Place(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    address = db.Column(db.String(250), index=True, unique=False)
    image_url = db.Column(db.String(250), index=True, unique=False) 
    description = db.Column(db.String(6400), index=True, unique=False)
    longitude = db.Column(db.String(12), index=True, unique=False)
    latitude = db.Column(db.String(12), index=True, unique=False)

    def __repr__(self):
        return '<Place %r>' % (self.title)

@app.route('/')
def home():
    title = "Карта славного города Осташкова"
    map_apikey = app.config['YANDEX_APIKEY']
    login_url = url_for("login")
    return render_template("home.html",title=title, map_apikey=map_apikey, login_url=login_url)

@app.route('/placemark.js')
def placemark():
    markers_list = []
    for c in Place.query.all():
        markers_list.append(c.__dict__)
    return render_template('placemark.js', markers_list=markers_list)

@app.route('/place/<id>')
def place(id):
    place_dict = {}
    for c in Place.query.filter_by(id=id):
        place_dict=dict(c.__dict__)
    return render_template("place.html",
                            name=place_dict.get("name"),
                            address=place_dict.get("address"),
                            description=place_dict.get("description"),
                            image_url=place_dict.get("image_url"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for("admin"))
    return render_template("login.html",error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(request.url_root)


@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        abort(401)
    places_list = []
    for c in Place.query.all():
        places_list.append(c.__dict__)
    return render_template("admin.html",places_list=places_list)

@app.route('/add_place',  methods=['GET', 'POST'])
def add_place():
    error = None
    if request.method == 'POST':
        if len(request.form['name']) > 120:
            error = 'Too large title'
        else:
            db.session.add(Place(
                name=request.form['name'],
                image_url=request.form['image_url'],
                address=request.form['address'],
                description=request.form['description'],
                longitude=request.form['longitude'],
                latitude=request.form['latitude'],
                ))
            db.session.commit()
            flash('Place added')
            return redirect(url_for('admin'))
    return render_template('add_place.html', error=error)

@app.route('/remove_place/<id>')
def remove_place(id):
    Place.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('admin'))
    



# Run by file
if __name__ == "__main__":
    app.debug = True
    app.run()