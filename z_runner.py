import sys
sys.path.insert(0, '/Users/HomeFolder/Python1/Forest_Gameee')

from Scene import Scene_
from Edge import Edge_
from Thorn import Thorn_
from Aban import Abandoned
from Gigan import GiganticTree
from Hole import Hole_
from Pile import PileDung
from River import River_
from charac_fg import Character_


class Runner(object):
    """
    This is the class that runs the game, and allows the user to enter into
    different scenes. The program is written such that once a player enters
    a scene, they can complete all of the activities within the methods available
    in the class and with the methods inherited from the parent Scene_ class.
    """
    # This is a dictionary which consists of string key values that refer to
    # the scene modules in the form of class instantiations.
    scenes = {
            'edge' : Edge_(),
            'thorn' : Thorn_(),
            'pile' : PileDung(),
            'aban_fire' : Abandoned(),
            'hole' : Hole_(),
            'river' : River_(),
            'gigan_tree' : GiganticTree(),
            'nothing' : "hmmm nothing really here"
    }

    def __init__(self):
        pass

    def start_edge(self):
        # The runner class is instantiated and then calls this method to start_edge
        # the game.

        # Here the edge key is used to instantiate the Edge_ class/scene.
        edge = Runner.scenes.get('edge')
        # Here the enter method is called for the Edge_ scene.
        edge.enter()

        while Character_.location == "Edge of Forest":
            # This while loop takes the value of the scenes directional attributes
            # and calls functions that allow entry into other scenes. 
            edge = Runner.scenes.get('edge')
            if edge.right == 'thorn':
                self.into_thorn()
            elif edge.left == 'pile':
                self.into_pile()
            elif edge.down == 'aban_fire':
                self.into_fire()


    def into_edge(self):
        edge = Runner.scenes.get('edge')
        edge.enter_again()
        while Character_.location == "Edge of Forest":
            if edge.right == 'thorn':
                self.into_thorn()
            elif edge.left == 'pile':
                self.into_pile()
            elif edge.down == 'aban_fire':
                self.into_fire()



    def into_thorn(self):
        thorn = Runner.scenes.get('thorn')
        thorn.enter()
        while Character_.location == "Thorny Patch!":
            if thorn.name == "Thorny Patch!" and thorn.left == 'edge':
                self.into_edge()

    def into_pile(self):
        pile = Runner.scenes.get('pile')
        pile.enter()
        while Character_.location == "Pile of Dung":
            if pile.name == "Pile of Dung" and pile.right == 'edge':
                self.into_edge()

    def into_fire(self):
        fire = Runner.scenes.get('aban_fire')
        fire.enter()
        while Character_.location == "Abandoned Fire Pit":
            if fire.name == "Abandoned Fire Pit" and fire.right == 'river':
                self.into_river()
            elif fire.name == "Abandoned Fire Pit" and fire.down == 'hole':
                self.into_hole()
            elif fire.name == "Abandoned Fire Pit" and fire.up == 'edge':
                self.into_edge()

    def into_river(self):
        pass

    def into_hole(self):
        pass


c = Character_()
b = Runner()
b.start_edge()
