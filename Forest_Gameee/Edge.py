import sys
import Scene
from charac_fg import Character_
from Thorn import Thorn_
from Pile import Pile_O_Dung
 # is putting this after Scene PEP8 acceptable?

# import sys
# sys.path.insert(0, '/Users/HomeFolder/Python1/the_hard_way')
#
# from z_runner import Runner

class Edge_(Scene.Scene_):
    """ This is the first scene on the map.
    From here you can either go to the thorns or the pile of dung scenes.
    """

    def __init__(self):
        self.charac = Character_()

        super(Edge_, self).__init__()
        # self.runner = Runner()
        self.input = '-'
        self.enter_var = 'a'
        self.up = '-'
        self.right = '-'
        self.left = '-'
        self.down = '-'
        self.examine= """
        You look around, but there isn't much to see.
        Hmmm but something about those shrubs... looks quite pleasant!
        """
        self.name = "Edge of Forest"
        self.thorn = Thorn_()
        self.pile = Pile_O_Dung()

    def enter(self):
        self.enter_var = 'b'
        super(Edge_, self).enter()


    def enter_again(self):
        self.enter_var = 'a'
        super(Edge_, self).enter()


    def examine_(self):
        super(Edge_, self).prompt()

    def nothing_(self):
        super(Edge_, self).nothing_()

    def prompt(self):
        super(Edge_, self).prompt()

    def move(self):
        self.input = input("Which direction would you like to go? \n")
        super(Edge_, self).move()
        if self.input.lower() in ['right', 'east']:
            self.right = 'thorn'
            return self.right
        elif self.input.lower() in ['left','west']:
            self.left = 'pile'
            return self.left
        elif self.input.lower() in ['down','south']:
            self.down = 'aban_fire'
            return self.down
        elif self.input.lower() in ['up','north']:
            self.nothing_()



b = Edge_()
z = Character_()




# HOW CAN I GET INFO FROM THIS CLASS BACK INTO Z_RUNNER...
# I CAN EASILY CALL THIS CLASS WITHIN z_runner
# BUT I NEED TO GET BACK TO Z_RUNNER I THINK... SO I CAN MOVE MAPS





# What did his scene class do last time?
# did it just have things that were inherent to all scenes? (class instances and methods...)
# if I make a scene class, should I have it in a different document?
# i.e. should parent and child classes be in different modules?
# also should we avoid inhertiance, and just use composition? I feel like we should!

# trying to import this I get the error message:
# TypeError: module.__init__() takes at most 2 arguments (3 given)

# how should I go from function to function... should I have the game play else
# where like I have had previously, or can I have one function at the end of an
# other even though it hasn't been defined yet? I guess I can just write them
# first then reverse their order...


#--------- outtakes
# accept_act = ['up','right','down','left','north','east','south','west'
# "examine"]
# while self.input.lower() not in accept_act:
#     print("ahh...hmmm... I don't believe that's a valid command.")
#     self.input = input("> ")



## this works!
    # def enter_again(self):
    #     Character_.location = self.name
    #     self.right = '-'
    #     self.left = '-'
    #     # self.thorn.left = '-'
    #     # self.pile.right = '-'
    #     super(Edge_, self).enter()
    #     # self.right = '-'
    #     # self.left = '-'
    #     self.prompt()


### also this works
##def enter(self):
    # Character_.location = self.name
    ##self.enter_var = 'b'
    ##super(Edge_, self).enter()
    # print("""        ~*~**`*~*`
    # You are an inexperienced lad, lacking in resources,
    # and you have a rather large nose. You happen upon a forest where you
    # think there may be food, shelter, and perhaps a magical potion to
    # shrink your nose.
    # ***~~**~*~
    #
    # You now find yourself at the edge of a Forest, surrounded by shrubs.
    #
    # [please type help for instructions!]
    # """)
    # # STEFAN thought: *Eat Shrubs / *go into the forest
    # # aha! so you can call a class' function before it is defined! yay!
    # self.prompt()
