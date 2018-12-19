import Scene
from charac_fg import Character_
# from Edge import Edge_

class Pile_O_Dung(Scene.Scene_):

    def __init__(self):
        super(Pile_O_Dung, self).__init__()
        self.charac = Character_()
        self.input = "input"
        self.up = "nothing"
        self.right = "edge"
        self.left = "nothing"
        self.down = "nothing"
        self.name = "Pile of Dung"
        self.examine = """
        The tree to the right of the pile of dung seems to be shaking ever so
        slightly...
        """
        # self.edge = Edge_()

    def examine_(self):
        super(Pile_O_Dung, self).examine_()

    def prompt(self):
        super(Pile_O_Dung, self).prompt()
    
    def squirrel_tree(self):
        print("""
        aha! It was a squirrel that was shaking the tree.
        But this is not any squirrel, it's an enchanted squirrel.

        What will you do next?
        a. leave the squirrel alone
        b. tease the squirrel
        c. dance for the squirrel
        """)
        squirrel_inp = input("> ")
        if squirrel_inp in ['a','a.','A','A.']:
            Pile_O_Dung.prompt(self)
        elif squirrel_inp in ['b','b.','B','B.']:
            print("The squirrel jumps down and bites you on the nose!")
            Character_.decrease_hp()
            Pile_O_Dung.prompt(self)
        elif squirrel_inp in ['c','C','C.','c.']:
            print("The squirrel is impressed, he places a fedora on your head!")
            Character_.inven.append('Fedora')
            Character_.get_inven()
            Pile_O_Dung.prompt(self)


    def enter(self):
        super(Pile_O_Dung, self).enter()


    def witch(self):
        print("""
        'Oh no, not so fast!'
        A Cursed Witch appears and casts a terrible spell on you.
        From now on, when you go to speak, your speech will be scrambled!
        """)

    def move(self):
        self.input = input("Which direction would you like to go? \n")
        super(Pile_O_Dung, self).move()
        if self.input.lower() in ['right', 'east']:
    # work on this still
            self.witch()
            self.right = 'edge'
            return self.right
        elif self.input.lower() in ['left','west']:
            self.nothing_()
        elif self.input.lower() in ['down','south']:
            self.nothing_()
        elif self.input.lower() in ['up','north']:
            self.nothing_()

z = Character_()
