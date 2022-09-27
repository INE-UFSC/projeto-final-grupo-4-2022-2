

class Body:

    def __init__(self, position, velocity, radius):
        self.__position = position
        self.__velocity = velocity
        self.__radius = radius

    def get_position(self):
        return self.__position

    def set_position(self, new_position):
        self.__position = new_position

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, new_velocity):
        self.__velocity = new_velocity

    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        self.__radius = new_radius

    def move(self, value):
        self.set_position(self.get_position() + value)

    def accelerate(self, value):
        self.set_velocity(self.get_velocity() + value)
