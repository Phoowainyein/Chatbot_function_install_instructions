#! /usr/bin/python3
import random

def easy(dice,number_of_sides_in_dice):
    results = []
    for each in range(1,number_of_sides_in_dice+1):
        #print("each",each)
        results.append(each)
    return results
def ask_number_of_sides_in_dice():
    number_of_sides_in_dice = int(input("how many-sided dice you want to cast?: "))
    dice = easy(1,number_of_sides_in_dice)
    return dice

num_side_diced_from_user=ask_number_of_sides_in_dice()
print(num_side_diced_from_user)
roll_dice = random.choice(num_side_diced_from_user)
print("Here is the result after rolling the dice : ",roll_dice)

#starting point for normal
numbers_of_rolls= int(input("How many rolls do you want ? : "))
count = numbers_of_rolls
sum = 0
while numbers_of_rolls >= count and count > 0:
    roll_dice = random.choice(num_side_diced_from_user)
    print(roll_dice)
    count = count -1
    sum = sum + roll_dice
print("sum",sum)

roll_again = input("Do you want to roll agian? \n Please type yes or no : ").lower()
while roll_again != "yes" and  "y":
    print("Bye,Have a good day!")
    break

while roll_again == "yes":    
        
    if roll_again == "yes"and "y":
        ask_again =ask_number_of_sides_in_dice()
        roll_dice = random.choice(num_side_diced_from_user)
        numbers_of_rolls= int(input("How many rolls do you want ? : "))
        count = numbers_of_rolls
        sum = 0
        while numbers_of_rolls >= count and count > 0:
            roll_dice = random.choice(num_side_diced_from_user)
            print(roll_dice)
            count = count -1
            sum = sum + roll_dice
        print("sum",sum)
        end_program = input("Do you want to end program?")
        if end_program == "end":
            break