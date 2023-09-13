import random

def main():
    print("=== Catch Me If You Can ===")
    print("You are Detective Carl Hanratty, on the trail of Frank Abagnale.")
    print("Frank is trying to escape. Can you catch him before he reaches the airport?")
    print("You have two chances to guess where he's headed!")
    
    print("\nWhere do you think Frank will go on his first move?")
    location = ["the Restaurant", "the Airline Clothing Supply Shop", "the Paper Company", "the Bank","Get a Cab","the Hospital"]
    move_choices(location[:3])
    guess(location[0:3])
    if True:
        print("\nQuick! He's getting away! Where do you think Frank will go on his second move?")
        move_choices(location[3:])
        guess(location[3:])
        if True:
            print("\nFrank slipped away. He's now at the airport!")
            print("You couldn't catch him in time, and he's flying to a faraway country!")
    try_again()

def guess(x):
    moves = random.choice(x)
    guess = int(input("\nEnter your choice (1-3): "))
    if moves == x[guess-1]:
        print("Congratulations, Detective Carl! You caught Frank Abagnale!")
        print("Frank is behind bars, and justice is served.")
        try_again()
    else:
        print(f"Wrong guess! Frank went to {moves}.")
        return 1

def move_choices(n):
    for i in range(0,3,1):
        print(f"{i+1}. {n[i]}")
    
def try_again():
    try_again = input("\nWould you like to play again? Y/N\n").upper()
    if try_again == 'Y':
        main()
    else:
        quit()

main()