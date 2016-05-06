# Role Game
With this tool one can load and play text adventure games. This games are saved in xml files, so everybody can create
and modify games.

## Start
From the directory where the game is saved, type:
	$ python3 role_game.py

## Load a game
To load a game, just type:
	$ load GAME_PATH
where GAME_PATH is the path of the game you want to load.
So for example, if you want to play DemoGame.xml saved in the games folder, just type:
	$ load games/DemoGame.xml

## Play
The command to play this game are:

### EQUIP
	$ equip weapon/shield

Equips the chosen weapon or shield if possible, and if needed unequipping the previous equipped weapon or shield.

### FIGHT
	$ fight who

Fights against the chosen enemy if possible.

### GO
	$ go where

To move from a place to the next place.

### LOOK
This doesn't need a second argument, so:
	$ look
will cause the description of the protagonist's current place to be displayed.

	$ look what
will return to the player the description of the item/character/place to look at.

### PICKUP
	$ pickup what

Causes the protagonist to pick up the chosen item if possible

### SEARCH
	$ search what

To search in places or enemies for items. In case something is found, a list will be shown.


## Exit game
To exit at any moment, just type:
	$ exit

## Objective(s) in the game
Right now there is no end of game (besides by quitting), but this is because not all functionalities are yet 
implemented. The same happens with conversation with characters: it still not implemented, but definitely planed.