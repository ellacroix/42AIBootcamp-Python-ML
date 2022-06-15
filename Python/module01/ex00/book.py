from recipe import *
import datetime
from datetime import datetime as dt

class Last_update:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, datetime.datetime):
			print("Last_update has to be a datetime.")
			exit()
		setattr(obj, self.private_name, value)

class Creation_date:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, datetime.datetime):
			print("Creation_date has to be a datetime.")
			exit()
		setattr(obj, self.private_name, value)

class Recipe_list:
	def __set_name__(self, owner, name):
		self.private_name = '_' + name

	def __get__(self, obj, objtype=None):
		return getattr(obj, self.private_name)
	
	def __set__(self, obj, value):
		if not isinstance(value, dict):
			print("Recipe_list has to be a dictionary.")
			exit()
		elif not {"starter", "lunch", "dessert"} <= value.keys():
			print("Recipe_list has to contain 3 keys: starter, lunch and dessert.")
			exit()
		setattr(obj, self.private_name, value)

class Book:
	
	name = Name()
	last_update = Last_update()
	creation_date = Creation_date()
	recipe_list = Recipe_list()

	def __init__(self, name, last_update, creation_date, recipe_list):
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipe_list = recipe_list

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for n in self.recipe_list["starter"]:
			if n.name == name:
				print(n)
				return()
		for n in self.recipe_list["lunch"]:
			if n.name == name:
				print(n)
				return()
		for n in self.recipe_list["dessert"]:
			if n.name == name:
				print(n)
				return()
		print("Recipe doesn't exist")
		
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for n in self.recipe_list[recipe_type]:
			print(n)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		self.recipe_list[recipe.recipe_type].append(recipe)
		self.last_update = dt.now()
