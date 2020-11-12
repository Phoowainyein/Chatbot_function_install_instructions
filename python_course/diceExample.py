#! /usr/bin/python3
import random
def roll(dice, sides):
    results = []
    for each in range(dice):
        number = random.randint(1,sides)
        results.append(number)
    return results

dice = roll(1,6)
print(dice)