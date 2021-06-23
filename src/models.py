from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    name=db.Column(db.String(50), nullable=False)
    height=db.Column(db.Float)
    mass=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    homeworld=db.Column(db.String(50))
    image=db.Column(db.String(255))
    born=db.Column(db.Integer)
    died=db.Column(db.Integer)
    species=db.Column(db.String(50))
    cybernetics=db.Column(db.String(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "gender":self.gender,
            "homeworld":self.homeworld,
            "image":self.image,
            "born":self.born,
            "died":self.died,
            "species":self.species,
            "cybernetics":self.cybernetics
        }

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
    climate=db.Column(db.String(50))
    image=db.Column(db.String(255))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period":self.orbital_period,
            "surface_water":self.surface_water,
            "gravity":self.gravity,
            "terrain":self.terrain,
            "population":self.population,
            "climate":self.climate,
            "image":self.image
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }

