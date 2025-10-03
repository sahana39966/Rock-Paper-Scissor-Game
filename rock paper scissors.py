import tkinter as tk
from tkinter import messagebox

winner = False
current_player = "X"

import random
item_list = ["rock","paper","scissor"]
user_choice = input("enter you move = rock, paper, scissor= ")
computer_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {computer_choice}")
if user_choice == computer_choice:
  print("Match Tie")
elif user_choice == "rock":
  if computer_choice == "paper":
    print("paper covers rock= Computer win")
  else:
    print("rock smashes scissor= You win")
elif user_choice == "paper":
  if computer_choice == "scissor":
    print("scissor cuts paper= Computer win")
  else:
    print("paper covers rock= You win")
elif user_choice == "scissor":
  if computer_choice == "paper":
    print("scissor cuts paper= You win")
  else:
    print("rock smashes scissor, Computer win")
