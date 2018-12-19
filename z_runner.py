import sys
sys.path.insert(0, '/Users/HomeFolder/Python1/Forest_Gameee')

from Scene import Scene_
from Edge import Edge_
from Thorn import Thorn_
from Aban import Abandoned
from Gigan import Gigantic_tree
from Hole import Hole_
from Pile import Pile_O_Dung
from River import River_
from charac_fg import Character_


class Runner(object):

    scenes = {
            'edge' : Edge_(),
            'thorn' : Thorn_(),
            'pile' : Pile_O_Dung(),
            'aban_fire' : Abandoned(),
            'hole' : Hole_(),
            'river' : River_(),
            'gigan_tree' : Gigantic_tree(),
            'nothing' : "hmmm nothing really here"
    }

    def __init__(self):
        pass

    def start_edge(self):
        edge = Runner.scenes.get('edge')
        edge.enter()

        while Character_.location == "Edge of Forest":
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
