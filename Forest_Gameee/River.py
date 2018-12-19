import Scene

class River_(Scene.Scene_):

    def __init__(self):
        super(River_, self).__init__()
        self.input = "input"
        self.up = "upstream"
        self.right = "gigantic"        # Poop, I need to create a block for this...
        self.left = "aban_fire"
        self.down = "death"

    def enter(self):
        pass
