import random
list=["p","r","s"]
chance= 10
no_of_chance=0
human_point=0
computer_point=0
print("\t\t\t\t\t stone, paper, scissors game")
print("type s for snake, p for paper and s for scissors")

while no_of_chance<=chance:
    _input=input("rock , paper, scissors\n")
    _random=random.choice(list)

    if _input==_random:
        print("tie, 0 point for each")

    if _input=="r" and _random=="p":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and human_point is {human_point}")
    elif _input=="r" and _random=="s":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you win 1 point")
        print(f"computer_point is {computer_point} and human_point is {human_point}")
    elif _input=="p" and _random=="r":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you win 1 point")
        print(f"computer_point is {computer_point} and human_point is {human_point}")
    elif _input=="p" and _random=="s":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and human_point{human_point}")
    elif _input=="s" and _random=="r":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point")
        print(f"computer_point is {computer_point} and human_point{human_point}")
    elif _input=="s" and _random=="p":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you win 1 point")
        print(f"computer_point is {computer_point} and human_point is {human_point}")
    else:
        print("you have wrong input")
        break
    
    no_of_chance = no_of_chance+1

    print(f"{chance- no_of_chance } is left out of {chance}")

    if no_of_chance>=chance:
        print("game over")
    else:
        print("you are still in the game \n")

if computer_point>human_point:
    print("computer wins")
else:
    print("human win")

print(f"your point is {human_point} and computer point is {computer_point}")
