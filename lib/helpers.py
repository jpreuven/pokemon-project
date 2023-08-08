from models import Pokemon, Party, Trainer
from sqlalchemy import create_engine, insert, not_
from sqlalchemy.orm import sessionmaker
import random
from rich import print
from rich.console import Console

engine = create_engine('sqlite:///pokemon_database.db')

session = sessionmaker(bind = engine)()

def get_color(type):
    if type == "Electric":
        color = "bold yellow"
    elif type == "Grass" or type == "Bug" or type == "Poison":
        color = "bold green"
    elif type == "Fire":
        color = "bold red"
    elif type == "Water" or type == "Ice":
        color = "bold blue"
    elif type == "Normal" or type == "Flying" or type == "Dragon":
        color = "bold white"
    elif type == "Ground" or type == "Fighting" or type == "Rock":
        color = "bold sandy_brown"
    elif type == "Psychic" or "Ghost":
        color = "bold purple"
    elif type == "Fairy":
        color = "bold pink"
    return color


def get_all_trainers():
    return session.query(Trainer).all()

def get_all_pokemon():
    return session.query(Pokemon).all()

def get_party_pokemon(id):    
    return [session.query(Pokemon).filter(Pokemon.id == party.pokemon_id).first() for party in session.query(Party).filter(Party.trainer_id == id).all()]

def get_poke_details(id):
    type = session.query(Pokemon.type).filter(Pokemon.id == id).first()[0]
    color = get_color(type)

    print(f"[{color}]{session.query(Pokemon).filter(Pokemon.id == id).first().full_details()} [/{color}]")

def get_party_ids(id):
    return [x[0] for x in session.query(Party.pokemon_id).filter(Party.trainer_id == id).all()]

def get_trainer_ids():
    return [x[0] for x in session.query(Trainer.id).all()]

def get_poke_by_level(level):
    low_level_pokemon = session.query(Pokemon).filter(Pokemon.level == level).all()
    random_poke_num_picker = random.randint(0,len(low_level_pokemon) - 1)

    return low_level_pokemon[random_poke_num_picker].id

def display_wild_poke(id):
    pokemon = session.query(Pokemon).filter(Pokemon.id == id).all()
    type = session.query(Pokemon.type).filter(Pokemon.id == id).first()[0]
    color = get_color(type)
    print(f"[{color}]{pokemon[0]}[/{color}]")


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