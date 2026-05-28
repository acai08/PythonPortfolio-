#Annie
#Dog Breed
#The prupose of my program is to help users choose a dog bred that meets their needs.

import pandas as pd
import webbrowser
import random

data = pd.read_csv('dogbreed.csv')

name = data['Name'].tolist()
max_weight = data['Maximum Weight'].tolist()
min_weight = data['Minimum Weight'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()
bredfor = data['BredFor'].tolist()
breed = []

def dogsize():
    size = input("What dog size do you prefer? (tiny, small, medium, or large): ")
    if size == "tiny":
        for i in range(len(name)):
            if max_weight[i] <= 10:
                breed.append(name[i])
        rec = random.randint(0, len(breed))
        print(f"I recommend this dog: {breed[rec]}")
        print(f"If you don't like that dog, here is a list of tiny dogs: {breed}")
        breed.clear()
    elif size == "small":
        for i in range(len(name)):
            if max_weight[i] <= 25 and min_weight[i] >= 11:
                breed.append(name[i])
        rec1 = random.randint(0, len(breed))
        print(f"I recommend this dog: {breed[rec1]}")
        print(f"If you don't like that dog, here is a list of small dogs: {breed}")
        breed.clear()
    elif size == "medium":
        for i in range(len(name)):
            if max_weight[i] <= 60 and min_weight >= 26:
                breed.append(name[i])
        rec2 = random.randint(0, len(breed))
        print(f"I recommend this dog: {breed[rec2]}")
        print(f"If you don't like that dog, here is a list of medium dogs: {breed}")
        breed.clear()
    else:
        for i in range(len(name)):
            if max_weight[i] > 60:
                breed.append(name[i])
        rec3 = random.randint(0, len(breed))
        print(f"I recommend this dog: {breed[rec3]}")
        print(f"If you don't like that dog, here is a list of large dogs: {breed}")
        breed.clear()

def temp(breed_name):
    number = 0
    for i in range(len(name)):
        if breed_name in name[i]:
            print(temperament[i])
            webbrowser.open(image[i])
            number = number + 1
    if number == 0:
            print("Sorry, your dog isn't on the list")

def breeds(purpose):
    num = 0
    for i in range(len(name)):
        if purpose in bredfor[i]:
            breed.append(name[i])
            num = num + 1
    rec4 = random.randint(0, len(breed))
    print(f"I recommend this dog: {breed[rec4]}")
    print(f"Here are all the other dogs that matches your input: {breed}")
    breed.clear()
    if num == 0:
        print("There are no matching breeds")

def menu():
    while True:
        interface = input("Do you want to find a dog based on size (size), find a dog's temperament (temperament), look for a dog with a specfic trait (trait), or quit?: ")
        if interface == "size":
            dogsize()
        elif interface == "temperament":
            temp1 = input("What dog do you want to look up?: ")
            temp(temp1)
        elif interface == "trait":
            trait = input("What dog trait do you want to look up?: ")
            breed(trait)
        else:
            break

menu()

#Functions

#Main

#Sources
#Mr.J shared this data with me.
