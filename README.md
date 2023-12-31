# Welcome to Pokemon Catcher!

**To get the app started:**

First, run the following commands:

```console
pipenv install
pipenv shell
python lib/seed.py
lib/cli.py
```

At this stage, the game should load, and you should be able to select a trainer. After selecting a trainer, try to catch all of the Pokemon! You can check how many Pokemon you have in your party and see how many Pokemon you have left to catch.

**What each of the files do:**

1. cli.py - this is where the game logic is.
2. helpers.py - this is where all the helper functions are that, among other things, allow my application to interact with the database.
3. models.py - this creates the classes that will eventually be instantiated
4. seed.py - this file instantiates the necessary classes (Pokemon, Trainer, Party), as well as the database with all 151 Pokemon. It also starts with 2 created trainers. If you'd like them to not initialize on start, comment out lines 188-222.
