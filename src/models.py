import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    sesionID = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False)
    password = Column(String(30), nullable = False)

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key = True)
    email = Column(String(30), nullable = False)
    password = Column(String(30), nullable = False)
    name = Column(String(50), nullable = False)
    birth = Column(DataTime = True)
    login = relationship(Login)

class Favorite(Base):
    __tablename__ = 'favorite'
    favoriteId = Column(Integer, primary_key = True)
    userId = Column(Integer, ForeignKey("Users.UserId"))
    characterId = Column(Integer, ForeignKey("Characters.Uid"))
    planetId = Column(Integer, ForeignKey("Planets.Uid"))
    name = Column(String(50))
    users = relationship(Users)

class Characters(Base):
    __tablename__ = "characters"
    uid = Column(Integer, primary_key = True)
    url = Column(String(200), unique = True)
    name = Column(String(50))
    favorite = relationship(Favorite)
    
class Planets(Base):
    __tablename__ = "planets"
    uid = Column(Integer, primary_key = True)
    url = Column(String(200), unique = True)
    name = Column(String(50))
    favorite = relationship(Favorite)

class CharacterDetail(Base):
    __tablename__ = "characterDtail"
    url = Column(String(200),ForeignKey("Characters.URL"), primary_key = True)     
    name = Column(String(50))
    gender = Column(String(10))
    birth  = Column(DataTime = True)
    hairColor = Column(String(10))
    skinColor = Column(String(10))
    eyeColor = Column(String(10))
    character = relationship(Characters)

class PlanetDetail(Base):
    __tablename__ = "planetDtail"
    url = Column(String(200),ForeignKey("Planets.URL"), primary_key = True)     
    name = Column(String(50))
    population = Column(Integer) 
    climate = Column(String(20))
    orbitalPeriod = Column(Integer)
    rotationPeriod = Column(Integer)
    planet = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
