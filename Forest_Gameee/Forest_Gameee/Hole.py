import Scene

class Hole_(Scene.Scene_):

    def __init__(self):
        super(Hole_, self).__init__()
        self.examine = """ Whoa Whoa! What's this!? There's a hole three times
        your size in diameter in the dirt!
        """
        self.name = "Hole"

    def enter(self):
        super(Hole_, self).enter()

    def examine_(self):
        super(Hole_, self).prompt()

    def nothing_(self):
        super(Hole_, self).nothing_()

    def prompt(self):
        super(Hole_, self).prompt()

    def hole_dungeon(self):
        print(""""
        You take several steps before you begin uncontrollably sliding into
        the dirt hole! You've now reached a flat plain at the bottom of the hole.
        It's rather dark, but you hear chattering in the distance...
        """)
        cave_inp = input("""
            What will you do next?

            a. Scream and cry for help!
            b. Use torch
            c. Start sprinting into the depths of the hole
        """)

        accept_inp = ['a','a.','A','A.','b','b.','B','B.','c','C','C.','c.']

        while cave_inp not in accept_inp:
            print("please type either a, b, or c!")
            



    def move(self):
        # This method on all scenes allows the user's input to be translated
        # to a string that is then used as a key to call a value from a dictionary
        # in the z_runner.py module.
        self.input = input("Which direction would you like to go? \n")
        super(Hole_, self).move()
        if self.input.lower() in ['right', 'east']:
            self.nothing_()
        elif self.input.lower() in ['left','west']:
            self.nothing_()
        elif self.input.lower() in ['down','south']:
            self.nothing_()
        elif self.input.lower() in ['up','north']:
            self.up = "aban_fire"
            return self.up
