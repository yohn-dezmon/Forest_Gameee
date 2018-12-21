import sys
from charac_fg import Character_

class Scene_(object):
    """ This is the parent class for all scene subclasses which are located
    in separate modules. Here I attempted to create methods that would apply
    to all of the subclasses and would include the basis for later modification.
    """

    def __init__(self):
        # This special method gives the general attributes for all of the
        # subclasses (scenes).  I set up the directional attributes as such
        # so that when they are assigned values in the move method of each
        # subclass, they will return a value that allows for movement
        # from one scene to the next in the z_runner module.
        self.name = '-'
        self.input = '-'
        self.solved = False
        self.up = '-'
        self.input = '-'
        self.examine = '-'


    def enter(self):
        # Here I set the character's location to the subclass' name.
        # This was done to allow for scene specific entrance text
        # that were printed with if statements.
        #
        # The self.right and self.left are set to their default dashes here
        # to ensure that upon entering a scene the values from the previous
        # scene do not carry over, or that the values from when this scene
        # was exited previously remain intact.
        Character_.location = self.name
        self.right = '-'
        self.left = '-'
        # This is the greeting displayed upon entering any scene
        print(f"""
                ------------------------
                You've entered: {self.name}!
                ------------------------
        """)

        if Character_.location == "Pile of Dung":
            # This is an example of a specific greeting, in this case when the
            # character enters the Pile of Dung scene.
            print("""
            OoOoOO what is that smell?! Ahhhh, it's a large pile of dung!
            """)

        elif Character_.location == "Edge of Forest" and self.enter_var == 'b':
            # I had to use the self.enter_var == 'b' here to ensure that
            # Edge of forest had a different greeting upon being entered initially
            # versus later in the game, given that it is the first scene and
            # provides a text-introduction to the game.
            print("""        ~*~**`*~*`
            You are an inexperienced lad, lacking in resources,
            and you have a rather large nose. You happen upon a forest where you
            think there may be food, shelter, and perhaps a magical potion to
            shrink your nose.
            ***~~**~*~

            You now find yourself at the edge of a Forest, surrounded by shrubs.

            [please type help for instructions!]
            """)
        # This is necessary to allow the player to continue playing.
        self.prompt()


    def nothing_(self):
        # This method is called upon when a character desires to walk in a
        # directional in which there is no scene to enter.
        print("""

                    Hmmmm.... not much to see here, ye young laddy!

        """)
        self.up = 'nothing'
        self.prompt()

    def examine_(self):
        # This method allows for the scene specific text to be displayed
        # giving the character a better idea of what can be accessed within
        # each scene.
        print(self.examine)
        print("\n")
        self.prompt()

    def prompt(self):
        # This is the most used method of the game. From this method
        # the user can elect to move, examine, view the contents of their
        # inventory, and utilize the contents of their inventory.
        self.input = input("What dare the young lad try next? \n")

        # Only the exact commands that are within this list are commands that
        # will produces actions in the game play.
        accept_act = ['quit','help','examine','go into forest','go',
        'look around', 'check out','move','move forwards','move backwards',
        'inventory','get inventory','check inventory','get inventory',
        'shrub','eat','cut','touch', 'inspect tree','check out tree','tree',
        'look at tree','shrub','look at shrubs', 'eat','cut','touch',
        'check out shrubs', 'inspect shrubs', 'crawl','crawl into thorns',
        'crawl under thorns', 'crawl into tunnel', 'crawl through thorns',
        'go to tree', 'pick up bag','look at bag','bag',
         'pick up green bag','check out bag','look in green bag'
         'look in bag', 'use', 'pick up rocks','pick up rock','rock',
         'check out rocks', 'rocks', 'look at rock', 'look at rocks',
         'pick up sticks','pick up stick','sticks',
         'check out sticks', 'look at stick', 'look at sticks', 'stick'
        ]
        # This while loop is essential, because it allows the user to enter
        # as many bad commands as they want without crashing the program.
        # As it is set-up, this whlie loop must be written before all of the
        # following if statements, because it has the self.input variable
        # at the end, and all of the if statements need to be able to
        # reference that input.

        while self.input.lower() not in accept_act:
            print("ahh...hmmm... I don't believe that's a valid command.")
            self.input = input("Try another command: ")

        if self.input.lower() in ['go','walk','move','go into forest']:
            # if a character wants to move, they must first input one of the above
            # commands, bringing them to the move prompt method.
            self.move()

        elif self.input.lower() in ['examine','look around',
        'check','check out']:
            self.examine_()

        elif self.input.lower() == 'use':
            self.use_item()

        elif self.input.lower() in ['health','get hp', 'what is my health',
        'character health','get health']:
            Character_.get_hp()
            self.prompt()


        elif self.input.lower() in ['shrub','shrubs','look at shrubs','eat',
        'cut','touch','check out shrubs','inspect shrubs'
        # An important syntatical note here is that the bracket ending the
        # list and the 'and' operator need to be on the same line!
        ] and self.name == "Edge of Forest":
        # This is the first time a scene specific if statement appears.
        # this is a conditional statement that requires that both a specific
        # command be given, and that it be within a certain scene.
        # if this statement evaluates to false, the else clause will be
        # executed, allowing the prompt method to restart.
            print("\nMmmm you eat some of the shrub fruit")
            # I chose to make the increase_hp method of Character_
            # be instantiation-independent so that the value of the
            # character's health will remain constant upon changing from
            # scene to scene.
            Character_.increase_hp()
            self.prompt()

        elif self.input.lower() in ['inventory','get inventory','check inventory',
        'items','get items']:
        # Allows the player to access their inventory when prompted.
            Character_.get_inven()
            self.prompt()

        elif self.input.lower() in ['enter hole','hole','go into hole',
        'explore hole'] and self.name == "Hole":

        elif self.input.lower() in ['inspect tree','check out tree','tree',
        'look at tree','go to tree'] and self.name == "Pile of Dung":
            self.squirrel_tree()

        elif self.input.lower() in ['pick up bag','look at bag','bag',
         'pick up green bag','check out bag','look in green bag'
         'look in bag'] and self.name == "Abandoned Fire Pit":
            self.inspect_bag()

        elif self.input.lower() in ['pick up rocks','pick up rock','rock',
        'check out rocks', 'rocks', 'look at rock', 'look at rocks'
        ] and self.name == "Abandoned Fire Pit":
            self.pick_up_rocks()

        elif self.input.lower() in ['pick up sticks','pick up stick','sticks',
        'check out sticks', 'look at stick', 'look at sticks', 'stick'
        ] and self.name == "Abandoned Fire Pit":
            self.pick_up_sticks()

        elif self.input.lower() in ['crawl','crawl into thorns',
        'crawl under thorns', 'crawl into tunnel', 'crawl through thorns'
        ] and self.name == "Thorny Patch!":
            self.crawl()

        elif self.input.lower() == 'quit':
            quit(0)

        elif self.input.lower() in ['help','instructions','please']:
            self.instructions()

        else:
            # This is the clause that is executed if a player choses a scene
            # specific action while not in the correct scene.
            self.error_specific()

    def move(self):
        # This function provides a list for all of the possible movement commands
        accept_act = ['up','right','down','left','north','east',
        'south','west']

        while self.input.lower() not in accept_act:
            print("ahh...hmmm... I don't believe that's a valid command.")
            self.input = input("> ")

    def error_specific(self):
        print("\n\tOoOOoOps! You cannot use that command here!")
        self.prompt()

    def instructions(self):
        print(""""
        LIST OF COMMANDS:

        GENERAL SCENE COMMANDS:

        examine - allows you to examine the scene
        move, go, into - will prompt you to
        help - will print this list of commands
        return - brings you back to the beginning of the scene you are in
        inventory - displays a list of the items your have in your inventory
        use - asks which item in the inventory you would like to use
        health - view your current health


        MOVEMENT COMMANDS
        (require a movement command before accessing this list):

        up, north - move to the scene north of your character
        down, south - move to the scene south of your character
        left, west - move to the scene west of your character
        right, east - move to the scene east of your character

        IF YOU OBTAIN AN ITEM:

        use - see what the item does

        SCENE SPECIFIC COMMANDS:

        crawl - allows you to crawl
        tree - allows you to see what's going on with the tree
        shrubs - allows you to inspect the shrubs
        bag - lets you inspect the bag
        sticks - lets you pick up sticks
        rocks - allows you to inspect the rocks




        """)
        self.prompt()

    def break_loop(self):
        self.prompt()

    def use_item(self):
        item_use = input("Which item would you like to use? \n")

        while item_use not in Character_.inven:
            print("""
            You do not have that item.
            You must type the item as it appears in your inventory, ye young laddy!
            Here is a list of the items you have: """)
            print("\n".join(Character_.inven))
            item_use = input("""
            Which item would you like to use?
            [type EXIT to leave inventory]
            """)
            if item_use not in Character_.inven:
                return self.prompt()
                break

        if item_use == 'mirror':
            print("""
            You stare into your mirror and observe your gaping nares.
            But wait, as you stare into the depths of your nostrils
            you notice something shiny... a wet booger perhaps?
            You take a closer look and you see that the tiny object is a
            golden key!
            You pick your nose and extract the key, congrats!
            """)
            Character_.add_inven('golden key')
            Character_.get_inven()
            self.prompt()

        elif item_use == 'golden key' and self.name == "Hole final":
            print("You unlock the chest, horah!")
            self.prompt()

        elif item_use == 'fedora':
            print("""
            You place the fedora atop your little head...
            Looking fresh, lad!
            """)
            self.prompt()


        elif item_use == 'torch':
            print("You set fire to your torch, and voila, you have light!")
            self.prompt()


        elif item_use == 'flint' or item_use == 'sticks' or item_use == 'steel':
            print("This item isn't very useful by itself...")
            self.prompt()

        else:
            self.prompt()








    def exit(self):
        quit(0)
