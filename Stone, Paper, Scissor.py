import random

print("STONE PAPER SCISSOR GAME")
print("-------------------------")

print("1. Stone")
print("2. Paper")
print("3. Scissor")

user = int(input("Enter your choice (1-3): "))

computer = random.randint(1, 3)

if user == 1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)
    user_choice = "Stone"

elif user == 2:
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
    user_choice = "Paper"

elif user == 3:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)
    user_choice = "Scissor"

else:
    print("Wrong choice!")
    exit()

if computer == 1:
    computer_choice = "Stone"
elif computer == 2:
    computer_choice = "Paper"
else:
    computer_choice = "Scissor"

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user == computer:
    print("It's a draw!")

elif user == 1 and computer == 3:
    print("You win!")

elif user == 2 and computer == 1:
    print("You win!")

elif user == 3 and computer == 2:
    print("You win!")

else:
    print("Computer wins!")
