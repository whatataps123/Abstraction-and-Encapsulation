from Car import Car
# Next, design a program that creates a Car object

# Then call the brake method five times. 
# After each call to the brake method, get the current speed of the car and display it.
class TestingCar:
    def Testing(self):
        print("Car Description")
        car = Car(2003, "Honda")
        car.show()
        # Calls the accelerate method five times. 
        for i in range(5):
            car.accelerate()
            print("Gas has been hit", i+1 ,"times.", "Speed is:", car.get_speed())
        # After each call to the accelerate method, get the current speed of the car and display it. 
        print("Car current speed is:", car.get_speed(),"\n")

        # Then call the brake method five times.
        for i in range (5):
            print("Brake has been hit", i+1 ,"times.", "Speed is:", car.get_speed())
            car.brake()
        # After each call to the brake method, get the current speed of the car and display it.\
        print("Car current speed is:", car.get_speed())
#Created an instance to show the output
test = TestingCar()
test.Testing()