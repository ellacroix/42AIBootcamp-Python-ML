class First_name:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("Description has to be a string.")
		setattr(obj, self.private_name, value)

class Is_alive:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, bool):
			raise ValueError("Value is not True or False")
		setattr(obj, self.private_name, value)

class Family_name:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("Family name has to be a string.")
		setattr(obj, self.private_name, value)

class House_words:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("House words has to be a string.")
		setattr(obj, self.private_name, value)

class GotCharacter:
    first_name = First_name()
    is_alive = Is_alive()

    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    family_name = Family_name()
    house_words = House_words()
    
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False

arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)