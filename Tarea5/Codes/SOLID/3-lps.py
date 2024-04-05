class Bird:
    def make_sound(self):
        pass


class Duck(Bird):
    def make_sound(self):
        print("Quack")


class Penguin(Bird):
    def make_sound(self):
        print("Honk")


def make_bird_sound(bird):
    bird.make_sound()


duck = Duck()
penguin = Penguin()
make_bird_sound(duck)
make_bird_sound(penguin)
