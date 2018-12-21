import Scene

class GiganticTree(Scene.Scene_):

    def __init__(self):
        super(GiganticTree, self).__init__()
        self.input = "input"
        self.up = "nothing"
        self.right = "nothing"
        self.left = "death"
        self.down = "nothing"

    def enter(self):
        pass
