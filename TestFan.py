from Fan import Fan
# Write a test program named TestFan that creates two Fan objects.

# Display each object’s speed, radius, color, and on properties.
class TestFan:
    def Testing(self):
        # First fan, assign the maximum speed, radius 10, color yellow, and turn it on.
        fan_1 = Fan()
        fan_1.set_speed(3)
        fan_1.set_radius(10)
        fan_1.set_color("yellow")
        fan_1.set_on(True)
        fan_1.show()

        # Second fan, assign medium speed, radius 5, color blue, and turn it off.
        fan_2 = Fan()
        fan_2.set_speed(3)
        fan_2.set_radius(10)
        fan_2.set_color("yellow")
        fan_2.set_on(True)
        fan_2.show()
