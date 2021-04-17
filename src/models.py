from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name=db.Column(db.String(50), nullable=False)
    height=db.Column(db.Float)
    mass=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    homeworld=db.Column(db.String(50))
    image=db.Column(db.String(50))
    born=db.Column(db.Integer)
    died=db.Column(db.Integer)
    species=db.Column(db.String(50))
    cybernetics=db.Column(db.String(50))

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name=db.Column(db.String(50), nullable=False)
    diameter=db.Column(db.Integer)
    rotation_period=db.Column(db.Integer)
    orbital_period=db.Column(db.Integer)
    surface_water=db.Column(db.Integer)
    gravity=db.Column(db.String(50))
    terrain=db.Column(db.String(50))
    population=db.Column(db.Integer)

    # def __repr__(self):
    #     return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "rotation period": self.rotation_period,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    # planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }