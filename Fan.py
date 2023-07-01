# Joshua Lemuel Z. Centina BS CPE 1-4
# pseudocode
# (The Fan class).  Design a class named Fan to represent a fan. The class contains:
class Fan:
    # Three constants named SLOW, MEDIUM, FAST with values 1, 2, 3 to denote fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        # priv int data named speed
        self.__speed = int(speed)
        # priv bool data named on
        self.__on = on
        # priv float data field named radius
        self.__radius = float(radius)
        # priv string data named color
        self.__color = str(color)

    def show(self):
        print("Fan is on:", self.__on)
        print("Fan speed:", self.__speed)
        print("Fan is radius:", self.__radius)
        print("Fan is color:", self.__color)

    # getter method for each
    def get_speed(self):
        return self.__speed
    
    def get_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    # setter method for each
    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_on(self, on):
        self.__on = on    

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)