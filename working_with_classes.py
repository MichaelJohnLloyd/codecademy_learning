#Exercise 1 - Using <type> to define the method/dictionary/list.
print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))

#Exercise 2 - Defining a class called Facade and passing through it.
class Facade:
  pass

#Exercise 3 - Creating an instance of the class.
class Facade:
  pass

facade_1 = Facade()

#Exercise 4 - Creating a variable to check the type of the class.
class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)

print(facade_1_type)

#Exercise 5 - Creating a class variable.
class Grade:
  minimum_passing = 65

#Exercise 6 - Creating a class method.
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#Exercise 7 - Creating methods within a class that takes more than one argument.
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

#Exercise 8 - Using the dunder constructor __init__ to pass through the new diameter of a circle.
class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)

#Exercise 9 - Creating an instance variable for the class.
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#Exercise 10 - Checking the attributes of the data stored in the variable.
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

#Exercise 11 - Creating a class method to calculate the circumference of a diameter.
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#Exercise 12 - Using dir() on a function to see the inner attributes.
print(dir(5))


def this_function_is_an_object(num):
    return "Cheese is {} times better than everything else".format(num)


print(dir(this_function_is_an_object))

#Exercise 13 - Using the __repr__method to pass the class through to attach strings. It does this by returning the
#string when the <self> parameter is passed through.
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

#Exercise 14 - Creating an <add_grade> function and a <Grade> class to cycle through the score and, if above the pass
#grade of 65, adds to the student variable.
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

pieter.add_grade(Grade(100))