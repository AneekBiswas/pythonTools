#! python3


#map
#             +---------+    +---------+   +-----------+
#             | Thief   O    | Bakery  |   |  Magical  |
#             | Guild   |    |         |   | Escalator |
#     +------++------O--+    +----O----+   |to Nowhere |
#     | Used |                              / O  /
#     |Anvils|        Town Square      +--------+
#     |      O                         |Obs Deck|
#     +------++----O----+    +----O----/ O /
#             | Black-  O    | Wizard /   /
#             | smith   |    | Tower     /
#             +---------+    +---------+


DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80

# DESC is a text description of the area. SHOP, if it exists, is a list of items that can be bought at this area. (We don't implement money in this program, so everything is free.) GROUND is a list of items that are on the ground in this area. The directions (NORTH, SOUTH, UP, etc.) are the areas that exist in that direction.

worldRooms = {
    'Town Square': {
        DESC: 'The town square is a large open space with a fountain in the center. Streets lead in all directions.',
        NORTH: 'North Y Street',
        EAST: 'East X Street',
        SOUTH: 'South Y Street',
        WEST: 'West X Street',
        GROUND: ['Welcome Sign', 'Fountain']},
    'North Y Street': {
        DESC: 'The northern end of Y Street has really gone down hill. Pot holes are everywhere, as are stray cats, rats, and wombats.',
        WEST: 'Thief Guild',
        EAST: 'Bakery',
        SOUTH: 'Town Square',
        GROUND: ['Do Not Take Sign Sign']},
    'Thief Guild': {
        DESC: 'The Thief Guild is a dark den of unprincipled types. You clutch your purse (though several other people here would like to clutch your purse as well).',
        SOUTH: 'West X Street',
        EAST: 'North Y Street',
        GROUND: ['Lock Picks', 'Silly Glasses']},
    'Bakery': {
        DESC: 'The delightful smell of meat pies fills the air, making you hungry. The baker flashes a grin, as he slides a box marked "Not Human Organs" under a table with his foot.',
        WEST: 'North Y Street',
        SOUTH: 'East X Street',
        SHOP: ['Meat Pie', 'Donut', 'Bagel'],
        GROUND: ['Shop Howto']},
    'West X Street': {
        DESC: 'West X Street is the rich section of town. So rich, they paved the streets with gold. This probably was not a good idea. The thief guild opened up the next day.',
        NORTH: 'Thief Guild',
        EAST: 'Town Square',
        SOUTH: 'Blacksmith',
        WEST: 'Used Anvils Store',
        GROUND: []},
    'Used Anvils Store': {
        DESC: 'The anvil store has anvils of all types and sizes, each previously-owned but still in servicable condition. However, due to a bug in the way this game is designed, you can buy anvils like any other item and walk around, but if you drop them they cannot be picked up since their TAKEABLE value is set to False. The code should be changed so that it\'s not possible for shops to sell items with TAKEABLE set to False.',
        EAST: 'West X Street',
        SHOP: ['Anvil'],
        GROUND: ['Anvil', 'Anvil', 'Anvil', 'Anvil']},
    'East X Street': {
        DESC: 'East X Street. It\'s like X Street, except East.',
        NORTH: 'Bakery',
        WEST: 'Town Square',
        SOUTH: 'Wizard Tower',
        GROUND: []},
    'Blacksmith': {
        DESC: 'The blacksmith loudly hammers a new sword over her anvil. Swords, axes, butter knives all line the walls of her workshop, available for a price.',
        NORTH: 'West X Street',
        EAST: 'South Y Street',
        SHOP: ['Sword', 'War Axe', 'Chainmail T-Shirt'],
        GROUND: ['Anvil', 'Shop Howto']},
    'South Y Street': {
        DESC: 'The Christmas Carolers of South Y Street are famous for all legally changing their name to Carol. They are also famous for singing year-round, in heavy fur coats and wool mittens, even in the summer. That\'s dedication to their craft!',
        NORTH: 'Town Square',
        WEST: 'Blacksmith',
        GROUND: []},
    'Wizard Tower': {
        DESC: 'Zanny magical antics are afoot in the world-famous Wizard Tower. Cauldrons bubble, rats talk, and books float midair in this center of magical discovery.',
        NORTH: 'East X Street',
        UP: 'Observation Deck',
        GROUND: ['Crystal Ball', 'Floating Book', 'Floating Book']},
    'Observation Deck': {
        DESC: 'You can see the entire town from the top of the Wizard Tower. Everybody looks like ants, especially the people transformed into ants by the wizards of the tower!',
        DOWN: 'Wizard Tower',
        UP: 'Magical Escalator to Nowhere',
        GROUND: ['Telescope']},
    'Magical Escalator to Nowhere': {
        DESC: 'No matter how much you climb the escalator, it doesn\'t seem to be getting you anywhere.',
        UP: 'Magical Escalator to Nowhere',
        DOWN: 'Observation Deck',
        GROUND: []},
    }

#The GROUNDDESC value is a short string that displays in the area's description. The SHORTDESC value is a short string that will be used in sentences like, "You drop X." or "You buy X. "The LONGDESC value is displayed when the player looks at the item. The TAKEABLE Boolean value is True if the player can pick up the item and put it in their inventory. The DESCWORDS value is a list of strings that can be used in the player's commands. For example, if this is ['welcome', 'sign'] then the player can type a command such as "take sign" or "look welcome". The TAKEABLE value is True if the item can be picked up off the ground. If this key doesn't exist, it defaults to True. The EDIBLE value is True if the item can be eaten. If this key doesn't exist, it defaults to False.

worldItems = {
    'Welcome Sign': {
        GROUNDDESC: 'A welcome sign stands here.',
        SHORTDESC: 'a welcome sign',
        LONGDESC: 'The welcome sign reads, "Welcome to this text adventure . You can type "help" for a list of commands to use."',
        TAKEABLE: False,
        DESCWORDS: ['welcome', 'sign']},
    'Do Not Take Sign Sign': {
        GROUNDDESC: 'A sign stands here, not bolted to the ground.',
        SHORTDESC: 'a sign',
        LONGDESC: 'The sign reads, "Do Not Take This Sign"',
        DESCWORDS: ['sign']},
    'Fountain': {
        GROUNDDESC: 'A bubbling fountain of green water.',
        SHORTDESC: 'a fountain',
        LONGDESC: 'The water in the fountain is a bright green color. Is that... gatorade?',
        TAKEABLE: False,
        DESCWORDS: ['fountain']},
    'Sword': {
        GROUNDDESC: 'A sword lies on the ground.',
        SHORTDESC: 'a sword',
        LONGDESC: 'A longsword, engraved with the word, "Exkaleber"',
        DESCWORDS: ['sword', 'exkaleber', 'longsword']},
    'War Axe': {
        GROUNDDESC: 'A mighty war axe lies on the ground.',
        SHORTDESC: 'a war axe',
        LONGDESC: 'The mighty war axe is made with antimony impurities from a fallen star, rendering it surpassingly brittle.',
        DESCWORDS: ['axe', 'war', 'mighty']},
    'Chainmail T-Shirt': {
        GROUNDDESC: 'A chainmail t-shirt lies wadded up on the ground.',
        SHORTDESC: 'a chainmail t-shirt',
        LONGDESC: 'The chainmail t-shirt has a slogan and arrow engraved on the front: "I\'m with Stupid"',
        DESCWORDS: ['chainmail', 'chain', 'mail', 't-shirt', 'tshirt', 'stupid']},
    'Anvil': {
        GROUNDDESC: 'The blacksmith\'s anvil, far too heavy to pick up, rests in the corner.',
        SHORTDESC: 'an anvil',
        LONGDESC: 'The black anvil has the word "ACME" engraved on the side.',
        TAKEABLE: False,
        DESCWORDS: ['anvil']},
    'Lock Picks': {
        GROUNDDESC: 'A set of lock picks lies on the ground.',
        SHORTDESC: 'a set of lock picks',
        LONGDESC: 'A set of fine picks for picking locks.',
        DESCWORDS: ['lockpicks', 'picks', 'set']},
    'Silly Glasses': {
        GROUNDDESC: 'A pair of those silly gag glasses with the nose and fake mustache rest on the ground.',
        SHORTDESC: 'a pair of silly fake mustache glasses',
        LONGDESC: 'These glasses have a fake nose and mustache attached to them. The perfect disguise!',
        DESCWORDS: ['glasses', 'silly', 'fake', 'mustache']},
    'Meat Pie': {
        GROUNDDESC: 'A suspicious meat pie rests on the ground.',
        SHORTDESC: 'a meat pie',
        LONGDESC: 'A meat pie. It tastes like chicken.',
        EDIBLE: True,
        DESCWORDS: ['pie', 'meat']},
    'Bagel': {
        GROUNDDESC: 'A bagel rests on the ground. (Gross.)',
        SHORTDESC: 'a bagel',
        LONGDESC: 'It is a donut-shaped bagel.',
        EDIBLE: True,
        DESCWORDS: ['bagel']},
    'Donut': {
        GROUNDDESC: 'A donut rests on the ground. (Gross.)',
        SHORTDESC: 'a donut',
        LONGDESC: 'It is a bagel-shaped donut.',
        EDIBLE: True,
        DESCWORDS: ['donut']},
    'Crystal Ball': {
        GROUNDDESC: 'A glowing crystal ball rests on a small pillow.',
        SHORTDESC: 'a crystal ball',
        LONGDESC: 'The crystal ball swirls with mystical energy, forming the words "Answer Unclear. Check Again Later."',
        DESCWORDS: ['crystal', 'ball']},
    'Floating Book': {
        GROUNDDESC: 'A magical book floats here.',
        SHORTDESC: 'a floating book',
        LONGDESC: 'This magical tomb doesn\'t have a lot of pictures in it. Boring!',
        DESCWORDS: ['book', 'floating']},
    'Telescope': {
        GROUNDDESC: 'A telescope is bolted to the ground.',
        SHORTDESC: 'a telescope',
        LONGDESC: 'Using the telescope, you can see your house from here!',
        TAKEABLE: False,
        DESCWORDS: ['telescope']},
    'README Note': {
        GROUNDDESC: 'A note titled "README" rests on the ground.',
        SHORTDESC: 'a README note',
        LONGDESC: 'The README note reads, "Welcome to the text adventure . Be sure to check out the source code to see how this game is put together."',
        EDIBLE: True,
        DESCWORDS: ['readme', 'note']},
    'Shop Howto': {
        GROUNDDESC: 'A "Shopping HOWTO" note rests on the ground.',
        SHORTDESC: 'a shopping howto',
        LONGDESC: 'The note reads, "When you are at a shop, you can type "list" to show what is for sale. "buy <item>" will add it to your inventory, or you can sell an item in your inventory with "sell <item>". (Currently, money is not implemented in this program.)',
        EDIBLE: True,
        DESCWORDS: ['howto', 'note', 'shop']},
    }

#These variables track where the player is and what is in their inventory. The value in the location variable will always be a key in the world variable and the value in the inventory list will always be a key in the worldItems variable.

location = 'Town Square' # start in town square
inventory = ['README Note', 'Sword', 'Donut'] # start with blank inventory
showFullExits = True

import cmd, textwrap

def displayLocation(loc):
    """A helper function for displaying an area's description and exits."""
    # Print the room name.
    print(loc)
    print('=' * len(loc))

    # Print the room's description (using textwrap.wrap())
    print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))

    # Print all the items on the ground.
    if len(worldRooms[loc][GROUND]) > 0:
        print()
        for item in worldRooms[loc][GROUND]:
            print(worldItems[item][GROUNDDESC])

    # Print all the exits.
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in worldRooms[loc].keys():
            exits.append(direction.title())
    print()
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction in worldRooms[location]:
                print('%s: %s' % (direction.title(), worldRooms[location][direction]))
    else:
        print('Exits: %s' % ' '.join(exits))

def moveDirection(direction):
    """A helper function that changes the location of the player."""
    global location

    if direction in worldRooms[location]:
        print('You move to the %s.' % direction)
        location = worldRooms[location][direction]
        displayLocation(location)
    else:
        print('You cannot move in that direction')

def getAllDescWords(itemList):
    """Returns a list of "description words" for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.extend(worldItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.append(worldItems[item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    matchingItems = []
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    def help_combat(self):
        print('Combat is not implemented in this program.')
    # These direction commands have a long (i.e. north) and short (i.e. n) form. Since the code is basically the same, I put it in the moveDirection()function.
    def do_north(self, arg):
        """Go to the area to the north, if possible."""
        moveDirection('north')

    def do_south(self, arg):
        """Go to the area to the south, if possible."""
        moveDirection('south')

    def do_east(self, arg):
        """Go to the area to the east, if possible."""
        moveDirection('east')

    def do_west(self, arg):
        """Go to the area to the west, if possible."""
        moveDirection('west')

    def do_up(self, arg):
        """Go to the area upwards, if possible."""
        moveDirection('up')

    def do_down(self, arg):
        """Go to the area downwards, if possible."""
        moveDirection('down')

    # Since the code is the exact same, we can just copy the
    # methods with shortened names:
    do_n = do_north
    do_s = do_south
    do_e = do_east
    do_w = do_west
    do_u = do_up
    do_d = do_down

    def do_exits(self, arg):
        """Toggle showing full exit descriptions or brief exit descriptions."""
        global showFullExits
        showFullExits = not showFullExits
        if showFullExits:
            print('Showing full exit descriptions.')
        else:
            print('Showing brief exit descriptions.')

    def do_inventory(self, arg):
        """Display a list of the items in your possession."""

        if len(inventory) == 0:
            print('Inventory:\n  (nothing)')
            return

        # first get a count of each distinct item in the inventory
        itemCount = {}
        for item in inventory:
            if item in itemCount.keys():
                itemCount[item] += 1
            else:
                itemCount[item] = 1

        # get a list of inventory items with duplicates removed:
        print('Inventory:')
        for item in set(inventory):
            if itemCount[item] > 1:
                print('  %s (%s)' % (item, itemCount[item]))
            else:
                print('  ' + item)

    do_inv = do_inventory


    def do_take(self, arg):
        """"take <item> - Take an item on the ground."""

        # put this value in a more suitably named variable
        itemToTake = arg.lower()

        if itemToTake == '':
            print('Take what? Type "look" the items on the ground here.')
            return

        cantTake = False

        # get the item name that the player's command describes
        for item in getAllItemsMatchingDesc(itemToTake, worldRooms[location][GROUND]):
            if worldItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue # there may be other items named this that you can take, so we continue checking
            print('You take %s.' % (worldItems[item][SHORTDESC]))
            worldRooms[location][GROUND].remove(item) # remove from the ground
            inventory.append(item) # add to inventory
            return

        if cantTake:
            print('You cannot take "%s".' % (itemToTake))
        else:
            print('That is not on the ground.')


    def do_drop(self, arg):
        """"drop <item> - Drop an item from your inventory onto the ground."""

        # put this value in a more suitably named variable
        itemToDrop = arg.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        # find out if the player doesn't have that item
        if itemToDrop not in invDescWords:
            print('You do not have "%s" in your inventory.' % (itemToDrop))
            return

        # get the item name that the player's command describes
        item = getFirstItemMatchingDesc(itemToDrop, inventory)
        if item != None:
            print('You drop %s.' % (worldItems[item][SHORTDESC]))
            inventory.remove(item) # remove from inventory
            worldRooms[location][GROUND].append(item) # add to the ground


    def complete_take(self, text, line, begidx, endidx):
        possibleItems = []
        text = text.lower()

        # if the user has only typed "take" but no item name:
        if not text:
            return getAllFirstDescWords(worldRooms[location][GROUND])

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for item in list(set(worldRooms[location][GROUND])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(TAKEABLE, True):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def complete_drop(self, text, line, begidx, endidx):
        possibleItems = []
        itemToDrop = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        for descWord in invDescWords:
            if line.startswith('drop %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "drop" but no item name:
        if itemToDrop == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_look(self, arg):
        """Look at an item, direction, or the area:
"look" - display the current area's description
"look <direction>" - display the description of the area in that direction
"look exits" - display the description of all adjacent areas
"look <item>" - display the description of an item on the ground or in your inventory"""

        lookingAt = arg.lower()
        if lookingAt == '':
            # "look" will re-print the area description
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    print('%s: %s' % (direction.title(), worldRooms[location][direction]))
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
            if lookingAt.startswith('n') and NORTH in worldRooms[location]:
                print(worldRooms[location][NORTH])
            elif lookingAt.startswith('w') and WEST in worldRooms[location]:
                print(worldRooms[location][WEST])
            elif lookingAt.startswith('e') and EAST in worldRooms[location]:
                print(worldRooms[location][EAST])
            elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
                print(worldRooms[location][SOUTH])
            elif lookingAt.startswith('u') and UP in worldRooms[location]:
                print(worldRooms[location][UP])
            elif lookingAt.startswith('d') and DOWN in worldRooms[location]:
                print(worldRooms[location][DOWN])
            else:
                print('There is nothing in that direction.')
            return

        # see if the item being looked at is on the ground at this location
        item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        # see if the item being looked at is in the inventory
        item = getFirstItemMatchingDesc(lookingAt, inventory)
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    def complete_look(self, text, line, begidx, endidx):
        possibleItems = []
        lookingAt = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)
        groundDescWords = getAllDescWords(worldRooms[location][GROUND])
        shopDescWords = getAllDescWords(worldRooms[location].get(SHOP, []))

        for descWord in invDescWords + groundDescWords + shopDescWords + [NORTH, SOUTH, EAST, WEST, UP, DOWN]:
            if line.startswith('look %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "look" but no item name, show all items on ground, shop and directions:
        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(worldRooms[location][GROUND]))
            possibleItems.extend(getAllFirstDescWords(worldRooms[location].get(SHOP, [])))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems)) # make list unique

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # otherwise, get a list of all "description words" for items for sale at the shop (if this is one):
        for descWord in shopDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # check for matching directions
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)

        # get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_list(self, arg):
        """List the items for sale at the current location's shop. "list full" will show details of the items."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        arg = arg.lower()

        print('For sale:')
        for item in worldRooms[location][SHOP]:
            print('  - %s' % (item))
            if arg == 'full':
                print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))


    def do_buy(self, arg):
        """"buy <item>" - buy an item at the current location's shop."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        itemToBuy = arg.lower()

        if itemToBuy == '':
            print('Buy what? Type "list" or "list full" to see a list of items for sale.')
            return

        item = getFirstItemMatchingDesc(itemToBuy, worldRooms[location][SHOP])
        if item != None:
            # NOTE - If you wanted to implement money, here is where you would add
            # code that checks if the player has enough, then deducts the price
            # from their money.
            print('You have purchased %s' % (worldItems[item][SHORTDESC]))
            inventory.append(item)
            return

        print('"%s" is not sold here. Type "list" or "list full" to see a list of items for sale.' % (itemToBuy))


    def complete_buy(self, text, line, begidx, endidx):
        if SHOP not in worldRooms[location]:
            return []

        itemToBuy = text.lower()
        possibleItems = []

        # if the user has only typed "buy" but no item name:
        if not itemToBuy:
            return getAllFirstDescWords(worldRooms[location][SHOP])

        # otherwise, get a list of all "description words" for shop items matching the command text so far:
        for item in list(set(worldRooms[location][SHOP])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_sell(self, arg):
        """"sell <item>" - sell an item at the current location's shop."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        itemToSell = arg.lower()

        if itemToSell == '':
            print('Sell what? Type "inventory" or "inv" to see your inventory.')
            return

        for item in inventory:
            if itemToSell in worldItems[item][DESCWORDS]:
                # NOTE - If you wanted to implement money, here is where you would add
                # code that gives the player money for selling the item.
                print('You have sold %s' % (worldItems[item][SHORTDESC]))
                inventory.remove(item)
                return

        print('You do not have "%s". Type "inventory" or "inv" to see your inventory.' % (itemToSell))


    def complete_sell(self, text, line, begidx, endidx):
        if SHOP not in worldRooms[location]:
            return []

        itemToSell = text.lower()
        possibleItems = []

        # if the user has only typed "sell" but no item name:
        if not itemToSell:
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for inventory items matching the command text so far:
        for item in list(set(inventory)):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_eat(self, arg):
        """"eat <item>" - eat an item in your inventory."""
        itemToEat = arg.lower()

        if itemToEat == '':
            print('Eat what? Type "inventory" or "inv" to see your inventory.')
            return

        cantEat = False

        for item in getAllItemsMatchingDesc(itemToEat, inventory):
            if worldItems[item].get(EDIBLE, False) == False:
                cantEat = True
                continue # there may be other items named this that you can eat, so we continue checking
            # NOTE - If you wanted to implement hunger levels, here is where
            # you would add code that changes the player's hunger level.
            print('You eat %s' % (worldItems[item][SHORTDESC]))
            inventory.remove(item)
            return

        if cantEat:
            print('You cannot eat that.')
        else:
            print('You do not have "%s". Type "inventory" or "inv" to see your inventory.' % (itemToEat))


    def complete_eat(self, text, line, begidx, endidx):
        itemToEat = text.lower()
        possibleItems = []

        # if the user has only typed "eat" but no item name:
        if itemToEat == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for edible inventory items matching the command text so far:
        for item in list(set(inventory)):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(EDIBLE, False):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


if __name__ == '__main__':
    print('Text Adventure !')
    print('================================================================================')
    print()
    print('(Type "help" for commands.)')
    print()
    print('''MAP OF TEXT TOWN
             +---------+    +---------+   +-----------+
             | Thief   O    | Bakery  |   |  Magical  |
             | Guild   |    |         |   | Escalator |
     +------++------O--+    +----O----+   |to Nowhere |
     | Used |                              / O  /
     |Anvils|        Town Square      +--------+
     |      O                         |Obs Deck|
     +------++----O----+    +----O----/ O /
             | Black-  O    | Wizard /   /
             | smith   |    | Tower     /
             +---------+    +---------+''')
    print('================================================================================')

    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')
