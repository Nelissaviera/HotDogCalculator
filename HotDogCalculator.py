# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:10:49 2022

@author: Nelissa Viera
"""
#constants
hot_dog_package = 10
dog_buns = 8

#input hot dogs values
people = int(input("Enter the number of people attending: "))
number_dog = int(input("Enter the number of hot dogs each person will be given: "))

#calculate total of hot dogs
total_dogs = people * number_dog

#calculate the minimum number of pakages of hot dogs and burn
total_hotdog_package = total_dogs // hot_dog_package
total_dog_buns = total_dogs // dog_buns

#calculate hot dog and burn left over
hotdogs_letf = (total_hotdog_package+1)*hot_dog_package-total_dogs
burn_left = (total_dog_buns+1)*dog_buns-total_dogs
print()
print("The minimum number of packages of hot dogs required is: ", total_hotdog_package)
print("The minimum number of packages of hot dog buns required is: ", total_dog_buns)
print("The number of hot dogs that will be left over is: ", hotdogs_letf)
print("The number of hot dog buns that will be left over is: ", burn_left )

