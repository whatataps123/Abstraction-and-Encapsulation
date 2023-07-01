# Joshua Lemuel Z. Centina BS CPE 1-4
# pseudocode
# (The Fan class).  Design a class named Fan to represent a fan. The class contains:
class Fan:
    # Three constants named SLOW, MEDIUM, FAST with values 1, 2, 3 to denote fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed, on, radius, color):
        # priv int data named speed
        self.__speed = int(speed)
        # priv bool data named on
        self.__on = on
        # priv float data field named radius
        self.__radius = float(radius)
        # priv string data named color
        self.__color = str(color)

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
        self.__speed = speed

    def set_on(self, on):
        self.__on = on    

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
# Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
# Display each object’s speed, radius, color, and on properties.