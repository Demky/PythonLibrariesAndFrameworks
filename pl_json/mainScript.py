# -*- coding: utf8 -*-
import random
import json

def read_values_from_json(file, key):
    values = []                 # Create a new empty list
    with open(file) as f:       # open a json file with my objects
        data = json.load(f)     # load all the data contained in this file /\ see json doc below
        for entry in data:
            values.append(entry[key]) # add each item in my list
    return values               # return my completed list

# json function load() [transform json file into python object] :
# https://docs.python.org/3/library/json.html#json.load

# documentation work with files :
# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get an entry from a list
    return item # return the item

def get_random_heroes():
    all_values = read_values_from_json('heroes.json', 'hero')
    return get_random_item_in(all_values)

# Programm
user_answer = input('Use Enter to get a name or Q to quit the script\n').upper()

while user_answer != "Q":
    print("--------------------------------------------")
    print("Random name from the file -> {}".format(get_random_heroes()))
    print("--------------------------------------------")
    user_answer = input('Use Enter to get a new entry or Q to quit the script\n').upper() # q == Q -> allow the script to end if user enter q instead of Q

# todo : 
# add a choice for user to add a hero name
# add this hero's name to the .json file
