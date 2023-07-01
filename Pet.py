# Joshua Lemuel Z. Centina BS CPE 1-4
# pseudocode
# Write a class named Pet, which should have the following data attributes:
class Pet:
    # The Pet class should have an _ _init_ _ method that creates these attributes. 
    def __init__(self, name, animal_type, age):
        # _ _name (for the name of a pet)
        self.__name = name
        # • _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
        self.__animal_type = animal_type
        # • _ _age (for the pet’s age)
        self.__age = age
    
# It should also have the following methods:
    # set_name()
    def set_name(self, name):
    # This method assigns a value to the _ _name field.
        self.__name = name

    # set_animal_type()
    def set_animal_type(self, animal_type):
    # This method assigns a value to the _ _animal_type field.
        self.__animal_type = animal_type
    
    # • set_age()
    def set_age(self, age):
    # This method assigns a value to the _ _age field.
        self.__age = age
        
    # get_name()
    def get_name(self):
    # This method returns the value of the _ _ name field.
        return self.__name
    
    # get_animal_type()
    def get_animal_type(self):
    # This method returns the value of the _ _animal_type field.
        return self.__animal_type
    
    # get_age()
    def get_age(self):
    # This method returns the value of the _ _age field.
        return self.__age
    # Once you have written the class, write a program that creates an object of the class 
    # and prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. 
    # Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
