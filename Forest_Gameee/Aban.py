import Scene
from charac_fg import Character_

class Abandoned(Scene.Scene_):
    """This is a scene where the character can obtain materials to build a torch.
    Once the Player obtains sticks, flint, and a steel, the game automatically
    produces a torch and replaces the other items in the characters inventory.
    """


    def __init__(self):
        super(Abandoned, self).__init__()
        # I believe character must be instantiated here to be used later
        self.charac = Character_()
        self.name = "Abandoned Fire Pit"
        self.examine = """
        ... it appears someone has been here recently. You see
        an abandoned fire pit, some sticks lying next to the fire pit,
        and you see a small green bag off next to some rocks.
        """
        self.down = '-'

    def enter_(self):
        super(Abandoned, self).enter()

    def examine_(self):
        super(Abandoned, self).examine_()

    def nothing_(self):
        super(Abandoned, self).nothing_()

    def prompt(self):
        super(Abandoned, self).prompt()

    def pick_up_sticks(self):
        # This is the result of a particular command on the Scene prompt.
        # This function adds the sticks to the character's inventory.
        print("You pick up the sticks!")
        Character_.inven.append('sticks')
        Character_.get_inven()
        self.prompt()

    def inspect_bag(self):
        # This is the result of a particular command on the Scene prompt.
        # This function adds the steel to the character's inventory.
        print("""You pick up the bag and look inside.
        You are a lucky boy, you find a steel!""")
        Character_.inven.append('steel')
        Character_.get_inven()
        self.prompt()

    def pick_up_rocks(self):
        # This is the result of a particular command on the Scene prompt.
        # This function adds flint to the character's inventory.
        print("""Good call! These aren't just any ole rocks, you've found flint!
        """)
        Character_.inven.append('flint')
        Character_.get_inven()
        self.prompt()


    def make_torch(self):
        if 'sticks' and 'steel' and 'flint' in Character_.inven:
            print("You've collected the items to create a Torch!")
            Character_.inven.append('Torch!')
            Character_.inven.remove('Sticks','steel','flint')
            Character_.get_inven()
            self.prompt()

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
