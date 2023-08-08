from models import Pokemon, Party, Trainer
from sqlalchemy import create_engine, insert, not_
# from sqlalchemy import in_
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///pokemon_database.db')

session = sessionmaker(bind = engine)()

def get_all_trainers():
    return session.query(Trainer).all()

def get_all_pokemon():
    return session.query(Pokemon).all()

def get_party_pokemon(id):    
    return [session.query(Pokemon).filter(Pokemon.id == party.pokemon_id).first() for party in session.query(Party).filter(Party.trainer_id == id).all()]

def get_poke_details(id):
    return session.query(Pokemon).filter(Pokemon.id == id).first().full_details()

def get_party_ids(id):
    return [x[0] for x in session.query(Party.pokemon_id).filter(Party.trainer_id == id).all()]

def get_trainer_ids():
    return [x[0] for x in session.query(Trainer.id).all()]

def get_poke_by_level(level):
    low_level_pokemon = session.query(Pokemon).filter(Pokemon.level == level).all()
    random_poke_num_picker = random.randint(0,len(low_level_pokemon) - 1)
    
    print(low_level_pokemon[random_poke_num_picker].full_details()) 
    return low_level_pokemon[random_poke_num_picker].id


def create_trainer(name):
    new_trainer = Trainer(name = name)
    session.add(new_trainer)
    session.commit()

def add_poke_to_party(poke_id, trainer_id):
    caught_poke = Party(pokemon_id = poke_id, trainer_id = trainer_id)
    session.add(caught_poke)
    session.commit()
    pass

def get_remaining_pokemon(trainer_id):
    return session.query(Pokemon).filter(not_(Pokemon.id.in_(get_party_ids(trainer_id)))).all()


def del_trainer(trainer_id):
    trainer = session.query(Trainer).filter(Trainer.id == trainer_id).first()
    session.delete(trainer)
    session.commit()

def update_something():
    pass
# Brainstorm
# Maybe adding a nickname