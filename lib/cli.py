from helpers import *
import random
from rich import print
from rich.console import Console

console = Console()

def display_welcome():
    print("Welcome to Pokemon Catcher!")

    console.print('''
[bold yellow]       ,___          .-;' [/bold yellow] [bold red]                                                                               [/bold red] [bold yellow]     `;-.         ___,            [/bold yellow]
[bold yellow]       `"-.`\_...._/`.'   [/bold yellow] [bold red]                                      ,'\                                      [/bold red] [bold yellow]      `.`\_...._/`.-"`            [/bold yellow]
[bold yellow]    ,      \        /     [/bold yellow] [bold red]        _.----.        ____         ,'  _\\   ___    ___     ____              [/bold red] [bold yellow]        \        /      ,         [/bold yellow]
[bold yellow] .-' ',    / ()   ()\\    [/bold yellow] [bold red]     _,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\   |`.    [/bold red] [bold yellow]           /()   () \    .' `-._  [/bold yellow]
[bold yellow]`'._   \  /[bold red]()[/bold red]    .  [bold red]([/bold red]|    [/bold yellow] [bold red]     \\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |   [/bold red] [bold yellow]          |[bold red])[/bold red]  .    [bold red]()[/bold red]\  /   _.'   [/bold yellow]
[bold yellow]    > .' ;,     -'-  /    [/bold yellow] [bold red]      \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |   [/bold red] [bold yellow]          \  -'-     ,; '. <      [/bold yellow]
[bold yellow]   / <   |;,     __.;     [/bold yellow] [bold red]        \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |     [/bold red] [bold yellow]         ;.__     ,;|   > \\      [/bold yellow]
[bold yellow]   '-.'-.|  , \    , \\   [/bold yellow] [bold red]          \\    ,-' /  /   \    ,'   | \\/ / ,`.|         /  /   \\  |     |   [/bold red] [bold yellow]           / ,    / ,  |.-'.-'    [/bold yellow]
[bold yellow]      `>.|;, \_)    \_)   [/bold yellow] [bold red]          \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    | [/bold red] [bold yellow]            (_/    (_/ ,;|.<`     [/bold yellow]
[bold yellow]       `-;     ,    /     [/bold yellow] [bold red]           \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |  [/bold red] [bold yellow]             \    ,     ;-`       [/bold yellow]
[bold yellow]          \    /   <      [/bold yellow] [bold red]            \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |    [/bold red] [bold yellow]            >   \    /            [/bold yellow]
[bold yellow]           '. <`'-,_)     [/bold yellow] [bold red]             \\_.-'       |__|    `-._ |              '-.|     '-.| |   |      [/bold red] [bold yellow]         (_,-'`> .'               [/bold yellow]
[bold yellow]            '._)          [/bold yellow] [bold red]                                     `'                            '-._|       [/bold red] [bold yellow]             (_,'                 [/bold yellow]
    ''')


def display_all_trainers():
    all_trainers = get_all_trainers()
    trainer_counter = 0
    counter = 0
    for trainers in all_trainers:
        print(f"{counter+1}: {trainers} Trainer ID: {trainers.id}")
        counter += 1
        trainer_counter = trainers.id
    print(f"{counter + 1}: Create new trainer") if trainer_counter else print("1: Create new trainer")

def choose_trainer(num):
    if num:
        print("\n")
        return input("Which trainer would you like to choose? (Select by ID) ")
    elif not num:
        return input ("Please create a new character. ")

def display_main_menu():
    print("1. Total Pokedex")
    print("2. Party Pokedex")
    print("3. How many Pokemon left?")
    print("4. Catch Pokemon")
    print("5. Delete Trainer")
    print("6. Exit Game")


def get_main_choice():
    print("\n")
    return input("Please select menu item: ")

def display_all_pokemon():
    x = True
    while x:
        all_pokemon = get_all_pokemon()
        for pokemon in all_pokemon:
            type = pokemon.type
            color = get_color(type)
            print(f"[{color}]{pokemon}[/{color}]")
        y = True
        while y:
            choose_poke = input("Enter Pokemon ID to see Pokemon details. Otherwise, enter anything else: ")
            if choose_poke.isnumeric() and int(choose_poke) in range(1,152):
                get_poke_details(int(choose_poke))
                # print(get_poke_details(int(choose_poke)))

                while True:
                    see_more = input("Would you like to see more? (Y/N)")
                    if see_more.lower() == "y":
                        print("OK!")
                        y = False
                        break
                    elif see_more.lower() == "n":
                        print("\n")
                        print("Back to main menu \n")
                        x = False
                        y = False
                        break
            elif choose_poke.isnumeric() and int(choose_poke) not in range(1,152):
                print ("Invalid ID!")
            else:
                print("\n")
                print("Back to main menu \n")
                y = False
                x = False


def display_party(id):
    x = True
    while x:
        party_pokemon = get_party_pokemon(id)
        print("\n")
        for pokemon in party_pokemon:
            type = pokemon.type
            color = get_color(type)
            print(f"[{color}]{pokemon}[/{color}]")
        choose_poke = input("Enter Pokemon ID to see Pokemon details. Otherwise, enter anything else: ")
        if choose_poke.isnumeric():
            if int(choose_poke) in get_party_ids(id):
                print("\n")
                get_poke_details(int(choose_poke))
                # print(get_poke_details(int(choose_poke)))

                while True:
                    see_more = input("Would you like to see more? (Y/N)")
                    if see_more.lower() == "y":
                        break
                    elif see_more.lower() == "n":
                        print("\n")
                        print("Back to main menu \n")
                        x = False
                        break
            else:
                print("You don't have that Pokemon! \n")
        else:
            print("\n")
            return
        
def find_pokemon(trainer_id):
    print("\n")
    x = True
    while x == True:
        random_level = random.randint(1,100)
        
        if random_level <= 65:
            poke_level = 1
        elif 65 < random_level <=80:
            poke_level = 2
        elif 80 < random_level <= 90:
            poke_level = 3
        elif 90 < random_level <= 96:
            poke_level = 4
        elif 96 < random_level <= 99:
            poke_level = 5
        elif random_level == 100:
            poke_level = 6

        poke_id = get_poke_by_level(poke_level)
        display_wild_poke(poke_id)
        
        print("You can: \n")
        print("1. Throw Pokeball")
        print("2. Run\n")

        y = True
        while y == True:
            choice = input("What would you like to do? ")
            if choice.isnumeric() and int(choice) in [1,2]:
                if int(choice) == 1:
                    print("Pokemon Caught!")
                    add_poke_to_party(poke_id, trainer_id)
                    z = True
                    while z == True:
                        again = input ("Would you like to try and catch another Pokemon? (Y/N)")
                        if again.lower() == "y":
                            y = False
                            z = False
                        elif again.lower() == "n":
                            x = False
                            y = False
                            z = False
                        else:
                            print("invalid selection")
                    # Bug here
                    # insert the poke via poke_id
                elif int(choice) == 2:
                    print("You got away safely!")
                    z = True
                    while z == True:
                        again = input ("Would you like to try and catch another Pokemon? (Y/N)")
                        if again.lower() == "y":
                            y = False
                            z = False
                        elif again.lower() == "n":
                            x = False
                            y = False
                            z = False
                            break
                        else:
                            print("invalid selection!")
            else:
                print("Invalid selection")
                    
        
def create_new_trainer():
    name = input("What is your name? ")
    create_trainer(name)
            
def check_pokemon_remaining(trainer_id):
    remaining_pokemon = get_remaining_pokemon(trainer_id)

    print(f"You have {len(remaining_pokemon)} Pokemon left to catch!")
    if len(remaining_pokemon) >= 100:
        print ("Gotta catch'em all!")
    elif 50 <= len(remaining_pokemon) < 100:
        print ("You're making great progress!")
    elif 10 <= len(remaining_pokemon) < 50:
        print("You're almost there!")
    elif 1 <= len(remaining_pokemon) < 10:
        print("So close!")
    elif len(remaining_pokemon) == 0:
        print("You're a Pokemon champ!")
    
    while True:
        choice = input("Would you like to see the Pokemon data? (Y/N)")
        if choice.lower() == "y":
            for pokemon in remaining_pokemon:
                type = pokemon.type
                color = get_color(type)
                print(f"[{color}]{pokemon.full_details()}[/{color}]")
            another_choice = input("Done? (Any key) ")
            if another_choice:
                break
        elif choice.lower() == "n":
            break
    
def delete_trainer(trainer_id):
    x = True
    while x:
        print("[bold red]Are you sure you would like to delete this trainer? (Y/N) [/bold red]")
        confirm_delete = input("")
        while True:
            if confirm_delete.lower() == "y":
                del_trainer(trainer_id)
                x = False
                decision = True
                break
            elif confirm_delete.lower() == "n":
                x = False
                decision = False
                break
            else:
                print("Invalid choice")
                decision = False
                break
    return decision

if __name__ == "__main__":
    x = True
    while x:
        display_welcome()

        print("\n")
        display_all_trainers()
        while True:
            trainer_id = choose_trainer(len(get_trainer_ids()))
            if trainer_id.isnumeric() and int(trainer_id) in get_trainer_ids():
                print("\n")
                break
            elif trainer_id.isnumeric() and len(get_trainer_ids()) == 0 and int(trainer_id) == 1:
                create_new_trainer()
                break
            elif trainer_id.isnumeric() and not len(get_trainer_ids()) == 0 and int(trainer_id) == (get_trainer_ids()[-1] + 1):
                create_new_trainer()
                break
            else:
                if len(get_trainer_ids()) == 0:
                    print ("Please create new trainer")
                else:
                    print(f"Please choose valid trainer ID")


        # Main Menu
        while True:
            display_main_menu()
            choice = get_main_choice()
            if choice == "1":
                display_all_pokemon()
            elif choice == "2":
                display_party(trainer_id)
            elif choice == "3":
                check_pokemon_remaining(trainer_id)
            elif choice == "4":
                find_pokemon(trainer_id)
            elif choice == "5":
                decision = delete_trainer(trainer_id)
                if decision:
                    break
                else:
                    continue
            elif choice == "6":
                print("Goodbye")
                x = False
                break