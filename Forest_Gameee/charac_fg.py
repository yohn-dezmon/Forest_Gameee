# from Death import Death_

class Character_(object):

    health = 10
    inven = []
    location = "location"

    def __init__(self):
        self.inven = []
        self.health = 10
        # self.death = Death_()

    def get_hp():
        print(Character_.health)

    def get_inven():
        print("\nYour current inventory:")
        print("\n".join(Character_.inven))

    def add_inven(item):
        Character_.inven.append(item)

    def decrease_hp():
        Character_.health -= 1
        print(f"Your health has decreased to: {Character_.health}")

    def increase_hp():
        if Character_.health <= 9:
            Character_.health += 1
            print(f"You've increased your hp to: {Character_.health}")
        elif Character_.health == 10:
            print("\nYou're at full health!")
            pass

    def health_to_death(self):
        if Character_.health == 0:
            self.die()
        elif Character_.health != 0:
            pass

    def die(self):
        print("GAME OVER")
        quit(0)
