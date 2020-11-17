#! /usr/bin/python3
import random

def easy(dice,number_of_sides_in_dice):
    results = []
    for each in range(1,number_of_sides_in_dice+1):
        #print("each",each)
        results.append(each)
    return results

number_of_sides_in_dice = int(input("how many-sided dice you want to cast?: "))
dice = easy(1,number_of_sides_in_dice)
print(dice)

def roll_the_dice():
    roll_dice = random.choice(dice)
    return roll_dice

call_to_roll_dice=roll_the_dice()
print(call_to_roll_dice)

#step1
#sum = sum + roll
numbers_of_rolls= int(input("How many rolls do you want ? : "))
count = numbers_of_rolls
sum = 0
while numbers_of_rolls >= count and count > 0:
    call_to_roll_dice=roll_the_dice()
    print(call_to_roll_dice)
    count = count -1
    sum = sum + call_to_roll_dice
print("sum = ",sum)


"""Normal
Same as easy plus

also ask how many rolls the user want to do,
Make as many function calls that are need, to have all the rolls.
and print separate results and also the sum of results"""