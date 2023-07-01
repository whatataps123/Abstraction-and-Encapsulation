from Pet import Pet

class TestPet:
    def Testing(self):
        # write a program that creates an object of the class 
        user_pet = Pet()

        # prompts the user to enter the name of pet
        name = str(input("Enter the name of your pet: "))
        # stored as object's attribute
        user_pet.set_name(name)

        # prompts the user to enter the type of pet
        animal_type = str(input("Enter the type of animal of your pet: "))
        # stored as object's attribute
        user_pet.set_animal_type(animal_type)

        # prompts the user to enter the age of pet
        age = int(input("Enter the age of your pet: "))
        # stored as object's attribute
        user_pet.set_age(age)

        # Display the output
        print("\nName of pet: ", user_pet.get_name())
        print("Type of pet: ", user_pet.get_animal_type())
        print("Age: ", user_pet.get_age())

# Created an instance to show the output
test = TestPet()
test.Testing()