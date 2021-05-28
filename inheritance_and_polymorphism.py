#Exercise 1 - Creating a Subclass from a Class.
class Bin:
  pass

class RecyclingBin(Bin):
  pass

#Exercise 2 - Creating an exeption class that is raised when conditions are met.
class OutOfStock(Exception):
    pass

class CandleShop():
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        self.stock[color] = self.stock[color] - 1
        if self.stock[color] < 1:
            raise OutOfStock


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

#Exercise 3 - Learning Overriding Methods, for use in practical ways such as Admin Permissions, tec.
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text


class User:
    def __init__(self, username):
        self.username = username

    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text


class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text

#Exercise 4 - Using the <super()> method to ad attributes from the main 'super' class.
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery,    onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

#Exercise 5 - Usint interface to use the same information from one class in multiple sub classes.
class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005

#Exercise 6 - Using the add dunder method instead of .add()
class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine

#Exercise 7 - Using the len and contains dunder methods to create a code that checks the number of
#lawyers and who they are.
class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyers):
        return lawyers in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

#Exercise 8 - Creating a subclass for the built-in type LIST and using the super method to run through
#the subclass.
class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()