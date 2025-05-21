import random

score = 0
rolls = []

print("welcome player 001")
print("Roll the dice and try to reach 50 points to win the game.")

while score < 50:
    input("press enter to roll the dice...")
    die = random.randint(1, 6)
    score += die 
    rolls.append(die)

    print(f"You rolll;ed a {die}.")
    print(f"Your current total score is {score}.")

print("congratulations! You reached 50 points and won the game!")
print(f"Your final score is {score}.")
print(f"Here are all your rolls: {rolls}")