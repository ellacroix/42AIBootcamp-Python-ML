from book import *
from datetime import datetime

r1 = Recipe("Fries", 2, 15, ["Potato", "Tomato"], "Random", "lunch")
r2 = Recipe("Cake", 3, 30, ["Flour, Chocolate"], "Simple cake", "dessert")
r3 = Recipe("Salad", 1, 10, ["Lettuce", "Tomato"], "Vegetarian", "starter")
r4 = Recipe("Burger", 2, 30, ["Bread", "Meat"], "Good", "lunch")
r5 = Recipe("Icecream", 1, 5, ["Ice", "Cream"], "Cold", "dessert")

recipes_dict = {"starter":[],
				"lunch":[],
				"dessert":[]}
Cookbook = Book("10 recettes faciles", datetime.now(), datetime.now(), recipes_dict)

print(Cookbook.creation_date)
print(Cookbook.last_update)
Book.add_recipe(Cookbook, r1)
Book.add_recipe(Cookbook, r2)
Book.add_recipe(Cookbook, r3)
Book.add_recipe(Cookbook, r4)
Book.add_recipe(Cookbook, r5)
print(Cookbook.last_update)
Book.get_recipe_by_name(Cookbook, "Burger")
Book.get_recipes_by_types(Cookbook, "dessert")