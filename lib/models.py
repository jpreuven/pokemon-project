# lib.models.py

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from rich import print
from rich.console import Console


Base = declarative_base()

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    level = Column(Integer())
    baseHP = Column(Integer())
    type = Column(String())

    parties = relationship('Party', backref=backref('pokemons'))

    def full_details(self):
        return (
            f"{self.name}: \n" +
            f"Level {self.level} \n" + 
            f"Pokemon ID:{self.id} \n" +
            f"BaseHP: {self.baseHP} \n" +
            f"Type: {self.type} \n"
            )

    def __repr__ (self):
        return (
            f"{self.name}: \n" +
            f"Level {self.level} \n" + 
            f"Pokemon ID:{self.id} \n"
            )

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    
    parties = relationship('Party', backref=backref('trainers'), cascade="all, delete-orphan")

    # parties = relationship('Party', backref=backref('trainers'))

    def __repr__(self):
        return f"Trainer: {self.name}"

class Party(Base):
    __tablename__ = "parties"

    id = Column(Integer(), primary_key = True)
    pokemon_id = Column(Integer(), ForeignKey("pokemons.id"))
    trainer_id = Column(Integer(), ForeignKey("trainers.id"))

