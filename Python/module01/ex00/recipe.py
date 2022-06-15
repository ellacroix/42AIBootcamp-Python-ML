import sys
from abc import ABC, abstractmethod

class Name:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("Description has to be a string.")
		setattr(obj, self.private_name, value)

class Cooking_lvl:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, int):
			raise ValueError("Cooking_lvl has to be an integer between 1 and 5.")
		elif value < 1 or value > 5:
			raise ValueError("Cooking_lvl has to be an integer between 1 and 5.")
		setattr(obj, self.private_name, value)

class Cooking_time:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not str(value).isnumeric():
			raise ValueError("Cooking_time has to be a positive integer.")
		setattr(obj, self.private_name, value)

class Ingredients:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, list):
			raise ValueError("Ingredients has to be a list of strings.")
		elif not all(isinstance(i, str) for i in value):
			raise ValueError("Ingredients has to be a list of strings.")
		setattr(obj, self.private_name, value)

class Description:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("Description has to be a string.")
		setattr(obj, self.private_name, value)

class Recipe_type:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, str):
			raise ValueError("Recipe_type has to be a string.")
		elif not value in ["starter", "lunch", "dessert"]:
			raise ValueError("Recipe_type has to be starter, lunch or dessert.")
		setattr(obj, self.private_name, value)

class Recipe:
	
	name = Name()
	cooking_lvl = Cooking_lvl()
	cooking_time = Cooking_time()
	ingredients = Ingredients()
	description = Description()
	recipe_type = Recipe_type()

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = "Recipe: " + self.name
		txt += "\nCooking level: " + str(self.cooking_lvl) + "/5"
		txt += "\nCooking time: " + str(self.cooking_time) + " minutes"
		txt += "\nIngredients: " + ", ".join(i for i in self.ingredients)
		txt += "\nDescription: " + self.description
		txt += "\nRecipe type: " + self.recipe_type
		txt += "\n"
		return txt