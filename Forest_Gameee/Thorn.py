import Scene
from charac_fg import Character_
# from Edge import Edge_

class Thorn_(Scene.Scene_):

    def __init__(self):
        super(Thorn_, self).__init__()
        self.charac = Character_()
        self.input = "-"
        self.up = "-"
        self.right = "-"
        self.left = "-"
        self.down = "-"
        self.examine = """
        There is a red, curly mess of thorns, that you
        think you may be able to crawl through.
        """
        self.name = "Thorny Patch!"
        # self.edge = Edge_()

    def enter(self):
        super(Thorn_, self).enter()

    def examine_(self):
        super(Thorn_, self).examine_()

    def nothing_(self):
        super(Thorn_, self).nothing_()

    def prompt(self):
        super(Thorn_, self).prompt()

    def move(self):
        self.input = input("Which direction would you like to go? \n")
        super(Thorn_, self).move()
        if self.input.lower() in ['right', 'east']:
             self.nothing_()
        elif self.input.lower() in ['left','west']:
            self.left = 'edge'
            return self.left
        elif self.input.lower() in ['down','south']:
            self.nothing_()
        elif self.input.lower() in ['up','north']:
            self.nothing_()

    def crawl(self):
        crawl_inp = input("""
        There are three tunnels of thorns,
        which will you crawl thorugh?
        """)
        while crawl_inp in ['2','3','two','three']:
            print("Ouchie!!! You get pricked by thorns! The tunnel is too small!")
            # will this save over other scenes?
            Character_.decrease_hp()
            self.charac.health_to_death()
            crawl_inp = input("try again: ")
        if crawl_inp in ['one','1']:
            print("""
            You hunch down, scrape your knee on the dirt, but successfully
            make it through the tunnel into the center portion of the thorns.
            You find a mirror, and pick it up.
            """)
            Character_.decrease_hp()
            self.charac.health_to_death()
            mirr_input = input("> ")
            accept_act = ['return','look','use','quit','reflection','help']
            while mirr_input.lower() not in accept_act:
                print("...")
                mirr_input = input("> ")
            if mirr_input == 'help':
                print("these are your options: ~~use~~return~~quit~~")
                mirr_input = input("> ")
            if mirr_input.lower() == 'return':
                self.enter()
            elif mirr_input.lower() in ['look','look into mirror',
            'check self out','use','reflection']:
                print("""
                You stare into your mirror and observe your gaping nares.
                But wait, as you stare into the depths of your nostrils
                you notice something shiny... a wet booger perhaps?
                You take a closer look and you see that the tiny object is a
                golden key!
                You pick your nose and extract the key, congrats!
                """)
                # add to inventory????
                Character_.add_inven('golden key')
                Character_.get_inven()
                self.enter()
            elif mirr_input == 'quit':
                quit(0)

z = Character_()
