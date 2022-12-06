import random
from data import *
from art import *

n = True


def game():
    B = random.choice(data)
    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    score = 0
    global n
    
    print(f"Compare A : {A['name']}, {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B : {B['name']}, {B['description']}, from {B['country']}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer == "A":
        if A['follower_count'] > B['follower_count']:
            score += 1
        else:
            n = False
            return "You lose."


    else:
        if A['follower_count'] < B['follower_count']:
            score += 1

        else:
            n = False
            return "You lose."
    if score >= 1:
        print(f"You're right! Current score: {score}. ")
    elif score == 0:
        n = False
        return "You lose."


while n:
    game()
