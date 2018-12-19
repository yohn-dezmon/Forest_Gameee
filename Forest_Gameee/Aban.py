import Scene
from charac_fg import Character_

class Abandoned(Scene.Scene_):

    def __init__(self):
        self.charac = Character_()
        super(Abandoned, self).__init__()
        self.input = "input"
        self.up = "nothing"
        self.right = "nothing"
        self.left = "edge"
        self.down = "nothing"
        self.name = "Abandoned Fire Pit"
        self.examine = """
        ... it appears someone has been here recently. You see
        an abandoned fire pit, some sticks lying next to the fire pit,
        and you see a small green bag off next to some rocks.
        """

    def enter_(self):
        super(Abandoned, self).enter()

    def examine_(self):
        super(Abandoned, self).examine_()

    def nothing_(self):
        super(Abandoned, self).nothing_()

    def prompt(self):
        super(Abandoned, self).prompt()

    def pick_up_sticks(self):
        print("You pick up the sticks!")
        Character_.inven.append('Sticks')
        Character_.get_inven()

    def inspect_bag(self):
        print("""You pick up the bag and look inside.
        You are a lucky boy, you find a steel!""")
        Character_.inven.append('steel')
        Character.get_inven()

    def pick_up_rocks(self):
        print("""Good call! These aren't just any ole rocks, you've found flint!
        """)
        Character_.inven.append('flint')
        Character_.get_inven()


    def make_torch(self):
        if 'Sticks' and 'steel' and 'flint' in Character_.inven:
            # ok I want to add two torches to the inventory... how can I have a number for an inventory?
            # do this at the end if we have time.
            # how to delete items from the list?
            print("You've collected the items to create a Torch!")
            Character_.inven.append('Torch!')
            Character_.inven.remove('Sticks','steel','flint')
            Character_.get_inven()

    def move(self):
        self.input = input("Which direction would you like to go? \n")
        super(Abandoned, self).move()
        if self.input.lower() in ['right', 'east']:
            self.right = 'river'
            return self.right
        elif self.input.lower() in ['left','west']:
            self.nothing_()
        elif self.input.lower() in ['down','south']:
            self.down = 'hole'
            return self.down
        elif self.input.lower() in ['up','north']:
            self.up = 'edge'
            return self.up
