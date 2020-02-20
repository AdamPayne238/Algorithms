#!/usr/bin/python

import math


# Write a function that receives a recipe and ingredients available to you in a dictionary
def recipe_batches(recipe, ingredients):

    batches = 0

    while True:

        for value in recipe:
            # if we dont have all the ingredients needed for recipe, exit
            if ingredients.get(value) is None:
                return batches  # returns 0

            else:
                # values in ingredients = values of ingredients - values of recipes
                ingredients[value] = ingredients.get(value) - recipe.get(value)
                # if value of ingredients is less than 0, return batches
                if ingredients[value] < 0:
                    return batches

        # iterate batches by 1
        batches += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
