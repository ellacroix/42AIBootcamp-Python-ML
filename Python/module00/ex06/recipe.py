cookbook = {"sandwich": {"ingredients":["ham", "bread", "cheese", "tomatoes"], "meal":"lunch", "prep_time":10},
            "cake": {"ingredients":["flour", "sugar", "eggs"], "meal":"dessert", "prep_time":60},
            "salad":{"ingredients":["avocado", "arugula", "tomatoes", "spinach"], "meal":"lunch", "prep_time":15}}

def print_recipe(recipe):
    print("Recipe for", recipe, ":")
    print("Ingredients list:", cookbook[recipe]["ingredients"])
    print("To be eaten for ", cookbook[recipe]["meal"], ".", sep = "")
    print("Takes", cookbook[recipe]["prep_time"], "minutes of cooking.")

def delete_recipe(recipe):
    for x in cookbook:
        if x == recipe:
            del cookbook[recipe]
            print("Recipe deleted\n")
            return()
    else:
        print("Recipe doesn't exist, returning to menu.\n")
        return()

def add_recipe():
    new_recipe = str(input("Enter recipe name: "))
    for recipe in cookbook:
        if new_recipe == recipe:
            print("Recipe already existing, returning to menu.\n")
            return()
    cookbook[new_recipe] = {}
    input_string = str(input("Enter ingredients, separated by a comma:"))
    cookbook[new_recipe]["ingredients"] = input_string.split(",")
    cookbook[new_recipe]["meal"] = str(input("Enter type of meal:"))
    cookbook[new_recipe]["prep_time"] = int(input("Enter preparation time in minutes:"))
    print("Recipe added\n")

def print_allrecipes():
    for recipe in cookbook:
        print_recipe(recipe)
        print("")

def print_menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

def cookbook_program():
    while True:
        print_menu()
        choice = input()
        if not choice in ["1", "2", "3", "4", "5"]:
            print("This option does not exist, please type the corresponding number.")
        else:
            print("")
            if choice == "1":
                add_recipe()
            elif choice == "2":
                target = str(input("Enter recipe to delete: "))
                delete_recipe(target)
            elif choice == "3":
                target = str(input("Enter recipe to print: "))
            elif choice == "4":
                print_allrecipes()
            elif choice == "5":
                print("Cookbook closed.")
                exit()

cookbook_program()