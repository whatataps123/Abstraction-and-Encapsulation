# Abstraction and Encapsulation

This repository demonstrates the concepts of abstraction and encapsulation using the Python programming language. It includes programming exercises that involve implementing classes for a fan, car, and pet, showcasing the use of abstraction and encapsulation.

## Fan Class

The `Fan` class represents a fan and contains the following components:

- Three constants: `SLOW`, `MEDIUM`, and `FAST`, with values 1, 2, and 3, respectively, to indicate the fan speed.
- Private instance variables:
  - `speed` (int): Specifies the speed of the fan.
  - `on` (bool): Specifies whether the fan is on or off (default is `False`).
  - `radius` (float): Specifies the radius of the fan.
  - `color` (str): Specifies the color of the fan.
- Getter and setter methods for all four data fields.
- A constructor that creates a fan with the specified speed (default: `SLOW`), radius (default: 5), color (default: blue), and on/off state (default: off).

A test program named `TestFan` is provided, which creates two `Fan` objects. The first object is assigned the maximum speed, a radius of 10, a yellow color, and turned on. The second object is assigned a medium speed, a radius of 5, a blue color, and turned off. The program displays each object's speed, radius, color, and on/off state.

## Car Class

The `Car` class represents a car and includes the following attributes:

- `__year_model` (int): Represents the year model of the car.
- `__make` (str): Represents the make of the car.
- `__speed` (int): Represents the current speed of the car.

The `Car` class provides the following methods:

- `__init__(year_model, make)`: Initializes the car's year model and make. Sets the speed to 0.
- `accelerate()`: Increases the car's speed by 5 each time it is called.
- `brake()`: Decreases the car's speed by 5 each time it is called.
- `get_speed()`: Returns the current speed of the car.

To demonstrate the functionality of the `Car` class, a program is provided that creates a `Car` object and calls the `accelerate()` method five times. After each call, it retrieves and displays the current speed of the car. Then, it calls the `brake()` method five times and displays the speed after each braking operation.

## Pet Class

The `Pet` class represents a pet and includes the following attributes:

- `__name` (str): Represents the name of the pet.
- `__animal_type` (str): Represents the type of animal the pet is (e.g., 'Dog', 'Cat', 'Bird').
- `__age` (int): Represents the age of the pet.

The `Pet` class provides the following methods:

- `set_name(name)`: Assigns a value to the `__name` attribute.
- `set_animal_type(animal_type)`: Assigns a value to the `__animal_type` attribute.
- `set_age(age)`: Assigns a value to the `__age` attribute.
- `get_name()`: Returns the value of the `__name` attribute.
- `get_animal_type()`: Returns the value of the `__animal_type` attribute.
- `get_age()`: Returns the value of the `__age` attribute.

To demonstrate the usage of the `Pet` class, a program is included that creates an instance of the class and prompts the user to enter the name, type, and age of their pet. This data is then stored as the object's attributes. The program uses the object's accessor methods to retrieve the pet's name, type, and age, and displays this information on the screen.
