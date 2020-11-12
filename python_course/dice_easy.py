#! /usr/bin/python3
import random

def easy(dice,number_of_sides_in_dice):
    results = []
    for each in range(1,number_of_sides_in_dice+1):
        #print("each",each)
        results.append(each)
    return results
#step2
number_of_sides_in_dice = int(input("how many-sided dice you want to cast?"))
dice = easy(1,number_of_sides_in_dice)
print(dice)

#step3

roll_dice = random.choice(dice)
print("hey,you got this : ",roll_dice)



"""Easy
define a function that takes in a number of sides in dice as an argument
and returns a list that has all numbers of dice
Ask from the user how many-sided dice he or she wants to cast
Call the function with the user given answer
roll the dice by taking random member from the list and return answer to the user using print"""