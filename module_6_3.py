class Horse:
    def __init__(self):
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'



    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        self.sound = 'I train, eat, sleep and repeat'


    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self.x_distance, self.y_distance

    def get_pos(self):
        tuple_pos = (self.x_distance, self.y_distance)
        return tuple_pos

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()