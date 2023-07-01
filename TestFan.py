from Fan import Fan

class TestFan:
    def Testing(self):
        # First fan, assign the maximum speed, radius 10, color yellow, and turn it on.
        print("Fan 1")
        fan_1 = Fan()
        fan_1.set_speed(3)
        fan_1.set_radius(10)
        fan_1.set_color("yellow")
        fan_1.set_on(True)
        fan_1.show()
        print("\n")
        # Second fan, assign medium speed, radius 5, color blue, and turn it off.
        print("Fan 2")
        fan_2 = Fan()
        fan_2.set_speed(2)
        fan_2.set_radius(5)
        fan_2.set_color("blue")
        fan_2.set_on(False)
        fan_2.show()

# Created an instance to show the output
test = TestFan()
test.Testing()