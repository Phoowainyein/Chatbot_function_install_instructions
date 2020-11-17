
def calculate_hand(dealer_hand):#takes a list as input,return ints as sum of cards
    result =[]
    sum =0
    for hand in range(dealer_hand):
        print("hand",hand)
        sum +=hand
        
    return sum
example=calculate_hand(2)
print(example)