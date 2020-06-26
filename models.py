from manage import db,app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(250), index=True, unique=False)
    title = db.Column(db.String(120), index=True, unique=False)
    description = db.Column(db.String(6400), index=True, unique=False)
    longitude = db.Column(db.String(12), index=True, unique=False)
    latitude = db.Column(db.String(12), index=True, unique=False)

    def __repr__(self):
        return '<House %r>' % (self.title)