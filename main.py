import random
comp_right = 0
user_right = 0
while True:  
  possibilities = ["Rock", "Paper", "Scissors"]
  user_choice = input("Rock, paper, or scissors: ")
  user_choice = user_choice.lower().strip()
  comp_choice = random.choice(["rock" , "paper", "scissors"])

  # print(f"Computer has {comp_right} answers right.")
  # print(f"You have {user_right} answers right.")
  
  print(f"Computer choose {comp_choice}. ")
  if user_choice == "rock" and comp_choice == "scissors":
    print("You win")
    user_right = user_right + 1
  
  elif user_choice == "paper" and comp_choice == "rock":
    print("You win")
    user_right = user_right + 1
  
  elif user_choice == "scissors" and comp_choice == "paper":
    print("You win")
    user_right += 1
  
  elif user_choice == "scissors" and comp_choice == "rock":
    print("You lose")
    comp_right = comp_right + 1
  
  elif user_choice == "paper" and comp_choice == "scissors":
    print("You lose")
    comp_right = comp_right + 1
  
  elif user_choice == "rock" and comp_choice == "paper":
    print("You lose")
    comp_right = comp_right + 1
  
  elif user_choice == comp_choice:
    print("It is a tie")
    comp_right = comp_right + 0
    user_right = user_right + 0
  else: 
    print("Invalid answer")
  
  print(f"Computer has {comp_right} answers right.")
  print(f"You have {user_right} answers right.")