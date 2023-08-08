from models import Pokemon, Party, Trainer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('sqlite:///pokemon_database.db')

    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Trainer).delete()
    session.query(Party).delete()

    ash = Trainer(name = "Ash")
    misty = Trainer(name = "Misty")
    session.add(ash)
    session.add(misty)


    # ashs_party = Party(trainer_id = 1, pokemon_id = 10)
    # ashs_party1 = Party(trainer_id = 1, pokemon_id = 11)
    # ashs_party2 = Party(trainer_id = 1, pokemon_id = 12)

    ashs_party_data = [
        {"trainer_id": 1, "pokemon_id": 10},
        {"trainer_id": 1, "pokemon_id": 11},
        {"trainer_id": 1, "pokemon_id": 12},
    ]

    mistys_party_data = [
        {"trainer_id": 2, "pokemon_id": 7},
        {"trainer_id": 2, "pokemon_id": 8},
        {"trainer_id": 2, "pokemon_id": 9},
    ]

    for party in ashs_party_data:
        add_party = Party(
            trainer_id = party["trainer_id"],
            pokemon_id = party["pokemon_id"],

        )
        session.add(add_party)

    for party in mistys_party_data:
        add_party = Party(
            trainer_id = party["trainer_id"],
            pokemon_id = party["pokemon_id"],

        )
        session.add(add_party)
    session.commit()

    # print ([session.query(Pokemon).filter(Pokemon.id == party.pokemon_id).first() for party in session.query(Party).all()])

import ipdb;
ipdb.set_trace()