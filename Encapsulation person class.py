class Person:
    def __init__(self, name, age):
        self.__name = name            
        self.__age = age              

    # method to check if the person is an adult
    def __is_adult(self):
        return self.__age >= 18

    # method to display person's information
    def show_info(self):
        adult_status = "an adult" if self.__is_adult() else "a minor"
        return f"{self.__name} is {self.__age} years old and is {adult_status}."

# Input
person = Person("Siri", 27)

info = person.show_info()
print(info)
