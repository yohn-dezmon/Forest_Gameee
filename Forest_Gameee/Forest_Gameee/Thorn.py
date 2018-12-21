import Scene
from charac_fg import Character_
# from Edge import Edge_

class Thorn_(Scene.Scene_):

    def __init__(self):
        super(Thorn_, self).__init__()
        self.charac = Character_()
        self.examine = """
        There is a red, curly mess of thorns, that you
        think you may be able to crawl through.
        """
        self.name = "Thorny Patch!"


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
        

z = Character_()
