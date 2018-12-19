import sys
from charac_fg import Character_

class Scene_(object):

    def __init__(self):
        self.description = "description"
        self.name = "name"
        self.input = "input"
        self.solved = False
        self.up = '-'
        self.input = '-'
        self.examine = '-'
        # self.charac = Character_()
        #self.enemies = # ???
        #self.items = [] # Not sure if I should have this here or just in the items class...

    def enter(self):
        Character_.location = self.name
        self.right = '-'
        self.left = '-'
        print(f"""
                ------------------------
                You've entered: {self.name}!
                ------------------------
        """)
        if Character_.location == "Pile of Dung":
            print("""
            OoOoOO what is that smell?! Ahhhh, it's a large pile of dung!
            """)
        elif Character_.location == "Edge of Forest" and self.enter_var == 'b':
            print("""        ~*~**`*~*`
            You are an inexperienced lad, lacking in resources,
            and you have a rather large nose. You happen upon a forest where you
            think there may be food, shelter, and perhaps a magical potion to
            shrink your nose.
            ***~~**~*~

            You now find yourself at the edge of a Forest, surrounded by shrubs.

            [please type help for instructions!]
            """)
        self.prompt()


    def nothing_(self):
        print("""

                    Hmmmm.... not much to see here, ye young laddy!

        """)
        self.up = 'nothing'
        self.prompt()

    def examine_(self):
        print(self.examine)
        print("\n")
        self.prompt()

    def prompt(self):
        self.input = input("What dare the young lad try next? \n")

        accept_act = ['quit','help','examine','go into forest','go',
        'look around', 'check out','move','move forwards','move backwards',
        'inventory','get inventory','check inventory','get inventory',
        'shrub','eat','cut','touch', 'inspect tree','check out tree','tree',
        'look at tree','shrub','look at shrubs', 'eat','cut','touch',
        'check out shrubs', 'inspect shrubs', 'crawl','crawl into thorns',
        'crawl under thorns', 'crawl into tunnel', 'crawl through thorns',
        'go to tree', 'pick up bag','look at bag','bag',
         'pick up green bag','check out bag','look in green bag'
         'look in bag'
        ]

        while self.input.lower() not in accept_act:
            print("ahh...hmmm... I don't believe that's a valid command.")
            self.input = input("> ")

        if self.input.lower() in ['go','walk','move','go into forest']:
            self.move()
        elif self.input.lower() in ['examine','look around',
        'check','check out']:
            self.examine_()
        # elif self.input.lower() in ['shrub','shrubs','look at shrubs',
        # 'eat shrub fruit','eat','cut','touch','check out shrubs',
        # 'inspect shrubs'] and
        elif self.input.lower() in ['shrub','shrubs','look at shrubs','eat',
        'cut','touch','check out shrubs','inspect shrubs'
        ] and self.name == "Edge of Forest":
            print("\nMmmm you eat some of the shrub fruit")
            Character_.increase_hp()
            self.prompt()
        elif self.input.lower() in ['inventory','get inventory','check inventory',
        'items','get items']:
            Character_.get_inven()
            self.prompt()
            # testing something
        elif self.input.lower() in ['inspect tree','check out tree','tree',
        'look at tree','go to tree'] and self.name == "Pile of Dung":
            self.squirrel_tree()
        elif self.input.lower() in ['pick up bag','look at bag','bag',
         'pick up green bag','check out bag','look in green bag'
         'look in bag'] and self.name == "Abandoned Fire Pit":
            self.inspect_bag()
        elif self.input.lower() in ['crawl','crawl into thorns',
        'crawl under thorns', 'crawl into tunnel', 'crawl through thorns'
        ] and self.name == "Thorny Patch!":
            self.crawl()


        elif self.input.lower() == 'quit':
            quit(0)
        elif self.input.lower() in ['help','instructions','please']:
            self.instructions()

    def move(self):
        accept_act = ['up','right','down','left','north','east',
        'south','west']

        while self.input.lower() not in accept_act:
            print("ahh...hmmm... I don't believe that's a valid command.")
            self.input = input("> ")






    # def move_prompt(self):
    #     accept_act = ['up','quit','help','right','down','left','north',
    #     'east','south','west',]
    #     pass

    def instructions(self):
        print(""""
        LIST OF COMMANDS:

        GENERAL SCENE COMMANDS:

        examine - allows you to examine the scene
        move, go, into - will prompt you to
        help - will print this list of commands
        return - brings you back to the beginning of the scene you are in
        inventory - displays a list of the items your have in your inventory



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


        """)
        self.prompt()



    def exit(self):
        quit(0)




# Questions:
# How to import a module from a different directory?

# since all of my 'rooms' import scene... Do I also need to import scene on the main .py?
# also do I have to do any sys stuff on the files that import scene??
