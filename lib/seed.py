# lib.seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Pokemon, Party, Trainer, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///pokemon_database.db')
    # Base.metadata.create_all (engine)

    Session = sessionmaker(bind = engine)
    session = Session()

    session.query(Pokemon).delete()
    session.commit()
    
    session.query(Trainer).delete()
    session.commit()

    session.query(Party).delete()
    session.commit()

    pokemon_data = [
    {"name": "Bulbasaur", "level": 1, "baseHP": 45, "type": "Grass/Poison"},
    {"name": "Ivysaur", "level": 3, "baseHP": 60, "type": "Grass/Poison"},
    {"name": "Venusaur", "level": 5, "baseHP": 80, "type": "Grass/Poison"},
    {"name": "Charmander", "level": 1, "baseHP": 39, "type": "Fire"},
    {"name": "Charmeleon", "level": 3, "baseHP": 58, "type": "Fire"},
    {"name": "Charizard", "level": 5, "baseHP": 78, "type": "Fire/Flying"},
    {"name": "Squirtle", "level": 1, "baseHP": 44, "type": "Water"},
    {"name": "Wartortle", "level": 3, "baseHP": 59, "type": "Water"},
    {"name": "Blastoise", "level": 5, "baseHP": 79, "type": "Water"},
    {"name": "Caterpie", "level": 1, "baseHP": 45, "type": "Bug"},
    {"name": "Metapod", "level": 1, "baseHP": 50, "type": "Bug"},
    {"name": "Butterfree", "level": 2, "baseHP": 60, "type": "Bug/Flying"},
    {"name": "Weedle", "level": 1, "baseHP": 40, "type": "Bug/Poison"},
    {"name": "Kakuna", "level": 1, "baseHP": 45, "type": "Bug/Poison"},
    {"name": "Beedrill", "level": 2, "baseHP": 65, "type": "Bug/Poison"},
    {"name": "Pidgey", "level": 1, "baseHP": 40, "type": "Normal/Flying"},
    {"name": "Pidgeotto", "level": 2, "baseHP": 63, "type": "Normal/Flying"},
    {"name": "Pidgeot", "level": 4, "baseHP": 83, "type": "Normal/Flying"},
    {"name": "Rattata", "level": 1, "baseHP": 30, "type": "Normal"},
    {"name": "Raticate", "level": 2, "baseHP": 55, "type": "Normal"},
    {"name": "Spearow", "level": 1, "baseHP": 40, "type": "Normal/Flying"},
    {"name": "Fearow", "level": 2, "baseHP": 65, "type": "Normal/Flying"},
    {"name": "Ekans", "level": 1, "baseHP": 35, "type": "Poison"},
    {"name": "Arbok", "level": 2, "baseHP": 60, "type": "Poison"},
    {"name": "Pikachu", "level": 1, "baseHP": 35, "type": "Electric"},
    {"name": "Raichu", "level": 2, "baseHP": 60, "type": "Electric"},
    {"name": "Sandshrew", "level": 1, "baseHP": 50, "type": "Ground"},
    {"name": "Sandslash", "level": 2, "baseHP": 75, "type": "Ground"},
    {"name": "Nidoran♀", "level": 1, "baseHP": 55, "type": "Poison"},
    {"name": "Nidorina", "level": 1, "baseHP": 70, "type": "Poison"},
    {"name": "Nidoqueen", "level": 3, "baseHP": 90, "type": "Poison/Ground"},
    {"name": "Nidoran♂", "level": 1, "baseHP": 46, "type": "Poison"},
    {"name": "Nidorino", "level": 1, "baseHP": 61, "type": "Poison"},
    {"name": "Nidoking", "level": 3, "baseHP": 81, "type": "Poison/Ground"},
    {"name": "Clefairy", "level": 1, "baseHP": 70, "type": "Fairy"},
    {"name": "Clefable", "level": 2, "baseHP": 95, "type": "Fairy"},
    {"name": "Vulpix", "level": 1, "baseHP": 38, "type": "Fire"},
    {"name": "Ninetales", "level": 2, "baseHP": 73, "type": "Fire"},
    {"name": "Jigglypuff", "level": 1, "baseHP": 115, "type": "Normal/Fairy"},
    {"name": "Wigglytuff", "level": 2, "baseHP": 140, "type": "Normal/Fairy"},
    {"name": "Zubat", "level": 1, "baseHP": 40, "type": "Poison/Flying"},
    {"name": "Golbat", "level": 2, "baseHP": 75, "type": "Poison/Flying"},
    {"name": "Oddish", "level": 1, "baseHP": 45, "type": "Grass/Poison"},
    {"name": "Gloom", "level": 2, "baseHP": 60, "type": "Grass/Poison"},
    {"name": "Vileplume", "level": 4, "baseHP": 75, "type": "Grass/Poison"},
    {"name": "Paras", "level": 1, "baseHP": 35, "type": "Bug/Grass"},
    {"name": "Parasect", "level": 2, "baseHP": 60, "type": "Bug/Grass"},
    {"name": "Venonat", "level": 1, "baseHP": 60, "type": "Bug/Poison"},
    {"name": "Venomoth", "level": 2, "baseHP": 70, "type": "Bug/Poison"},
    {"name": "Diglett", "level": 1, "baseHP": 10, "type": "Ground"},
    {"name": "Dugtrio", "level": 3, "baseHP": 35, "type": "Ground"},
    {"name": "Meowth", "level": 1, "baseHP": 40, "type": "Normal"},
    {"name": "Persian", "level": 3, "baseHP": 65, "type": "Normal"},
    {"name": "Psyduck", "level": 1, "baseHP": 50, "type": "Water"},
    {"name": "Golduck", "level": 3, "baseHP": 80, "type": "Water"},
    {"name": "Mankey", "level": 1, "baseHP": 40, "type": "Fighting"},
    {"name": "Primeape", "level": 3, "baseHP": 65, "type": "Fighting"},
    {"name": "Growlithe", "level": 1, "baseHP": 55, "type": "Fire"},
    {"name": "Arcanine", "level": 4, "baseHP": 90, "type": "Fire"},
    {"name": "Poliwag", "level": 1, "baseHP": 40, "type": "Water"},
    {"name": "Poliwhirl", "level": 3, "baseHP": 65, "type": "Water"},
    {"name": "Poliwrath", "level": 4, "baseHP": 90, "type": "Water/Fighting"},
    {"name": "Abra", "level": 1, "baseHP": 25, "type": "Psychic"},
    {"name": "Kadabra", "level": 3, "baseHP": 40, "type": "Psychic"},
    {"name": "Alakazam", "level": 5, "baseHP": 55, "type": "Psychic"},
    {"name": "Machop", "level": 1, "baseHP": 70, "type": "Fighting"},
    {"name": "Machoke", "level": 2, "baseHP": 80, "type": "Fighting"},
    {"name": "Machamp", "level": 4, "baseHP": 90, "type": "Fighting"},
    {"name": "Bellsprout", "level": 1, "baseHP": 50, "type": "Grass/Poison"},
    {"name": "Weepinbell", "level": 2, "baseHP": 65, "type": "Grass/Poison"},
    {"name": "Victreebel", "level": 4, "baseHP": 80, "type": "Grass/Poison"},
    {"name": "Tentacool", "level": 1, "baseHP": 40, "type": "Water/Poison"},
    {"name": "Tentacruel", "level": 3, "baseHP": 80, "type": "Water/Poison"},
    {"name": "Geodude", "level": 1, "baseHP": 40, "type": "Rock/Ground"},
    {"name": "Graveler", "level": 2, "baseHP": 55, "type": "Rock/Ground"},
    {"name": "Golem", "level": 4, "baseHP": 80, "type": "Rock/Ground"},
    {"name": "Ponyta", "level": 1, "baseHP": 50, "type": "Fire"},
    {"name": "Rapidash", "level": 4, "baseHP": 65, "type": "Fire"},
    {"name": "Slowpoke", "level": 1, "baseHP": 90, "type": "Water/Psychic"},
    {"name": "Slowbro", "level": 3, "baseHP": 95, "type": "Water/Psychic"},
    {"name": "Magnemite", "level": 1, "baseHP": 25, "type": "Electric/Steel"},
    {"name": "Magneton", "level": 3, "baseHP": 50, "type": "Electric/Steel"},
    {"name": "Farfetch'd", "level": 2, "baseHP": 52, "type": "Normal/Flying"},
    {"name": "Doduo", "level": 2, "baseHP": 35, "type": "Normal/Flying"},
    {"name": "Dodrio", "level": 3, "baseHP": 60, "type": "Normal/Flying"},
    {"name": "Seel", "level": 1, "baseHP": 65, "type": "Water"},
    {"name": "Dewgong", "level": 4, "baseHP": 90, "type": "Water/Ice"},
    {"name": "Grimer", "level": 1, "baseHP": 80, "type": "Poison"},
    {"name": "Muk", "level": 3, "baseHP": 105, "type": "Poison"},
    {"name": "Shellder", "level": 1, "baseHP": 30, "type": "Water"},
    {"name": "Cloyster", "level": 4, "baseHP": 50, "type": "Water/Ice"},
    {"name": "Gastly", "level": 1, "baseHP": 30, "type": "Ghost/Poison"},
    {"name": "Haunter", "level": 3, "baseHP": 45, "type": "Ghost/Poison"},
    {"name": "Gengar", "level": 5, "baseHP": 60, "type": "Ghost/Poison"},
    {"name": "Onix", "level": 2, "baseHP": 35, "type": "Rock/Ground"},
    {"name": "Drowzee", "level": 1, "baseHP": 60, "type": "Psychic"},
    {"name": "Hypno", "level": 3, "baseHP": 85, "type": "Psychic"},
    {"name": "Krabby", "level": 1, "baseHP": 30, "type": "Water"},
    {"name": "Kingler", "level": 3, "baseHP": 55, "type": "Water"},
    {"name": "Voltorb", "level": 1, "baseHP": 40, "type": "Electric"},
    {"name": "Electrode", "level": 3, "baseHP": 60, "type": "Electric"},
    {"name": "Exeggcute", "level": 1, "baseHP": 60, "type": "Grass/Psychic"},
    {"name": "Exeggutor", "level": 5, "baseHP": 95, "type": "Grass/Psychic"},
    {"name": "Cubone", "level": 1, "baseHP": 50, "type": "Ground"},
    {"name": "Marowak", "level": 3, "baseHP": 60, "type": "Ground"},
    {"name": "Hitmonlee", "level": 4, "baseHP": 50, "type": "Fighting"},
    {"name": "Hitmonchan", "level": 4, "baseHP": 50, "type": "Fighting"},
    {"name": "Lickitung", "level": 3, "baseHP": 90, "type": "Normal"},
    {"name": "Koffing", "level": 1, "baseHP": 40, "type": "Poison"},
    {"name": "Weezing", "level": 3, "baseHP": 65, "type": "Poison"},
    {"name": "Rhyhorn", "level": 1, "baseHP": 80, "type": "Ground/Rock"},
    {"name": "Rhydon", "level": 3, "baseHP": 105, "type": "Ground/Rock"},
    {"name": "Chansey", "level": 3, "baseHP": 250, "type": "Normal"},
    {"name": "Tangela", "level": 2, "baseHP": 65, "type": "Grass"},
    {"name": "Kangaskhan", "level": 3, "baseHP": 105, "type": "Normal"},
    {"name": "Horsea", "level": 1, "baseHP": 30, "type": "Water"},
    {"name": "Seadra", "level": 3, "baseHP": 55, "type": "Water"},
    {"name": "Goldeen", "level": 1, "baseHP": 45, "type": "Water"},
    {"name": "Seaking", "level": 3, "baseHP": 80, "type": "Water"},
    {"name": "Staryu", "level": 1, "baseHP": 30, "type": "Water"},
    {"name": "Starmie", "level": 4, "baseHP": 60, "type": "Water/Psychic"},
    {"name": "Mr. Mime", "level": 3, "baseHP": 40, "type": "Psychic/Fairy"},
    {"name": "Scyther", "level": 4, "baseHP": 70, "type": "Bug/Flying"},
    {"name": "Jynx", "level": 4, "baseHP": 65, "type": "Ice/Psychic"},
    {"name": "Electabuzz", "level": 3, "baseHP": 65, "type": "Electric"},
    {"name": "Magmar", "level": 3, "baseHP": 65, "type": "Fire"},
    {"name": "Pinsir", "level": 3, "baseHP": 65, "type": "Bug"},
    {"name": "Tauros", "level": 3, "baseHP": 75, "type": "Normal"},
    {"name": "Magikarp", "level": 1, "baseHP": 20, "type": "Water"},
    {"name": "Gyarados", "level": 3, "baseHP": 95, "type": "Water/Flying"},
    {"name": "Lapras", "level": 3, "baseHP": 130, "type": "Water/Ice"},
    {"name": "Ditto", "level": 3, "baseHP": 48, "type": "Normal"},
    {"name": "Eevee", "level": 1, "baseHP": 55, "type": "Normal"},
    {"name": "Vaporeon", "level": 3, "baseHP": 130, "type": "Water"},
    {"name": "Jolteon", "level": 3, "baseHP": 65, "type": "Electric"},
    {"name": "Flareon", "level": 3, "baseHP": 65, "type": "Fire"},
    {"name": "Porygon", "level": 4, "baseHP": 65, "type": "Normal"},
    {"name": "Omanyte", "level": 2, "baseHP": 35, "type": "Rock/Water"},
    {"name": "Omastar", "level": 4, "baseHP": 70, "type": "Rock/Water"},
    {"name": "Kabuto", "level": 2, "baseHP": 30, "type": "Rock/Water"},
    {"name": "Kabutops", "level": 4, "baseHP": 60, "type": "Rock/Water"},
    {"name": "Aerodactyl", "level": 4, "baseHP": 80, "type": "Rock/Flying"},
    {"name": "Snorlax", "level": 4, "baseHP": 160, "type": "Normal"},
    {"name": "Articuno", "level": 5, "baseHP": 90, "type": "Ice/Flying"},
    {"name": "Zapdos", "level": 5, "baseHP": 90, "type": "Electric/Flying"},
    {"name": "Moltres", "level": 5, "baseHP": 90, "type": "Fire/Flying"},
    {"name": "Dratini", "level": 3, "baseHP": 41, "type": "Dragon"},
    {"name": "Dragonair", "level": 4, "baseHP": 61, "type": "Dragon"},
    {"name": "Dragonite", "level": 5, "baseHP": 91, "type": "Dragon/Flying"},
    {"name": "Mewtwo", "level": 6, "baseHP": 106, "type": "Psychic"},
    {"name": "Mew", "level": 6, "baseHP": 100, "type": "Psychic"}
]


    for pokemon in pokemon_data:
        new_poke = Pokemon(
            name=pokemon["name"], 
            level = pokemon["level"],
            baseHP = pokemon["baseHP"],
            type = pokemon["type"]
            )
        session.add(new_poke)
    

    ash = Trainer(name = "Ash")
    misty = Trainer(name = "Misty")

    session.add(ash)
    session.add(misty)


    ashs_party_data = [
        {"trainer_id": 1, "pokemon_id": 10},
        {"trainer_id": 1, "pokemon_id": 11},
        {"trainer_id": 1, "pokemon_id": 12},
]



    for party in ashs_party_data:
        add_party = Party(
            trainer_id = party["trainer_id"],
            pokemon_id = party["pokemon_id"],

        )
        session.add(add_party)
    
    mistys_party_data = [
        {"trainer_id": 2, "pokemon_id": 7},
        {"trainer_id": 2, "pokemon_id": 8},
        {"trainer_id": 2, "pokemon_id": 9},
]
    for party in mistys_party_data:
        add_party = Party(
            trainer_id = party["trainer_id"],
            pokemon_id = party["pokemon_id"],

        )
        session.add(add_party)

    session.commit()