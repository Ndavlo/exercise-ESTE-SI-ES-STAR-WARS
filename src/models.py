import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from eralchemy2 import render_er

Base = declarative_base()

class Films(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    characters = Column(String(300), nullable=False)
    created = Column(DateTime, nullable=False)
    director = Column(String(300), nullable=False)
    edited = Column(DateTime, nullable=False)
    episode_id = Column(Integer)
    opening_crawl = Column(String(300), nullable=False)
    planets = Column(String(300), nullable=False)
    producer = Column(String(300), nullable=False)
    release_date = Column(Date, nullable=False)
    species = Column(String(300), nullable=False)
    starships = Column(String(300), nullable=False)
    title = Column(String(300), nullable=False)
    url = Column(String(300), nullable=False)
    vehicles = Column(String(300), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(300), nullable=False) 
    eye_color = Column(String(300), nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Films)
    gender = Column(String(300), nullable=False)
    hair_color = Column(String(300), nullable=False)
    height = Column(Float, nullable=False)
    homeworld = Column(String(300), nullable=False)
    mass = Column(Float)
    name = Column(String(300), nullable=False)
    skin_color = Column(String(300))
    created = Column(DateTime, nullable=False)
    edited = Column(DateTime, nullable=False)
    species = Column(String(300), nullable=False) 
    starships = Column(String(300))
    url = Column(String(300))
    vehicles = Column(String(300))

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    MGLT = Column(String(300), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(300), nullable=False)
    cost_in_credits =  Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    crew = Column(Integer, nullable=False)
    edited = Column(DateTime, nullable=False)
    hyperdrive_rating = Column(Float, nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(300), nullable=False)
    max_atmosphering_speed = Column(String(300), nullable=False)
    model = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    passengers = Column(String(300), nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Films)
    pilots = Column(String(300), nullable=False)
    starship_class = Column(String(300), nullable=False)
    url = Column(String(300), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(300), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    crew = Column(Integer, nullable=False)
    edited = Column(DateTime, nullable=False)
    length = Column(Integer, nullable=False)
    manufacturer = Column(String(300), nullable=False)
    max_atmosphering_speed = Column(String(300), nullable=False)
    model = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    passengers = Column(String(300), nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Films)
    pilots = Column(String(300), nullable=False)
    vehicle_class = Column(String(300), nullable=False)
    url = Column(String(300), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    average_height = Column(Float, nullable=False)
    average_lifespan = Column(Integer, nullable=False)
    classification = Column(String(300), nullable=False)
    created = Column(DateTime, nullable=False)
    designation = Column(String(300), nullable=False)
    edited = Column(DateTime, nullable=False)
    eye_colors = Column(String(300), nullable=False)
    hair_colors = Column(String(300), nullable=False)
    homeworld = Column(String(300), nullable=False)
    language = Column(String(300), nullable=False)
    name = Column(String(300), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Films)
    skin_colors = Column(String(300), nullable=False)
    url = Column(String(300), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(300), nullable=False)
    created = Column(DateTime, nullable=False)
    diameter = Column(Integer, nullable=False)
    edited = Column(DateTime, nullable=False)
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship(Films)
    gravity = Column(Integer, nullable=False)
    name = Column(String(300), nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    residents = Column(String(300), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain = Column(String(300), nullable=False)
    url = Column(String(300), nullable=False)


render_er(Base, 'diagram.png')