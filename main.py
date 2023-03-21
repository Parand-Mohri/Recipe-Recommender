from ast import literal_eval

import pandas as pd

data = pd.read_csv('correct_data.csv', converters={'Ingredients': literal_eval})


def get_space_out(ingred_list):
    result = []
    for i in range(0, len(ingred_list)):
        result.append(ingred_list[i].strip())
    return result


def find_recipe_unique(ingredients):
    ing_data = data["Ingredients"]
    recipes_list = []
    for i in range(0, len(ing_data)):
        temp = set(ing_data[i])
        if temp == set(get_space_out(ingredients)):
            recipes_list.append(data['Recipe'][i])
    return recipes_list


def find_that_recipe(ingredients):
    ingredients = get_space_out(ingredients)
    recipes_list = []
    for i in range(0, len(data["Ingredients"])):
        if all(item in data["Ingredients"][i] for item in ingredients):
            recipes_list.append(data['Recipe'][i])
    return recipes_list


if __name__ == "__main__":
    ing = [item for item in input("Enter Ingredients (Separate by , ):\n").split(',')]
    ing = [x.lower() for x in ing]
    inp = input("Do you want other ingredients to be included in the recipe? \n You can choose: yes, no or both")
    if inp.lower() == "yes":
        rec = find_that_recipe(ing)
        if not rec:
            print("No recipes with given ingredients")
        else:
            print(rec)
    elif inp.lower() == "no":
        rec = find_recipe_unique(ing)
        if not rec:
            print("No recipes with given ingredients")
        else:
            print(rec)
    elif inp.lower() == "both":
        rec_unique = find_recipe_unique(ing)
        rec_inc = find_that_recipe(ing)
        if not rec_inc:
            print("No recipes with given ingredients")
        else:
            print("recipes only using given ingredients", rec_unique)
            print("recipes with other ingredients included", rec_inc)
    else:
        print("You must choose between yes, no or both")
