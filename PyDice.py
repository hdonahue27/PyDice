import random

# main menu
def menu():
  print("Welcome to PyDice!")
  print("S: Start PyDice")
  print("Q: Quit PyDice")
  print("I: View PyDice info")
  menuInput = input("Choose an option\n")
  if menuInput == "s" or menuInput == "S":
    start()
  elif menuInput == "q" or menuInput == "Q":
    quit()
  elif menuInput == "i" or menuInput == "I":
    info()

# dice/side select
def start():
    global diceNum
    diceNum = input("\nChoose the amount of dice you would like to roll\n")
    diceNum = int(diceNum)
    global sideNum
    sideNum = input("\nChoose the amount of sides that each die will have\n")
    sideNum = int(sideNum)
    print("\nTo view a list of commands, type C and press enter.")
    rollPrompt(diceNum=diceNum, sideNum=sideNum) 

# dice engine and value changer
def rollPrompt(diceNum, sideNum):
  rollPromptInput = input("\nPress enter to roll, or type a command\n")
  if rollPromptInput == "m" or rollPromptInput == "M":
    menu()
  if rollPromptInput == "d" or rollPromptInput == "D":
    print("\n")
    start()
  if rollPromptInput == "q" or rollPromptInput == "Q":
    exit()
  if rollPromptInput == "c" or rollPromptInput == "C":
    cmds()
  if rollPromptInput == "n" or rollPromptInput == "N":
    diceNum = int(input(str(diceNum) + " dice are currently being rolled. Choose the new amount of dice you would like to roll\n"))
    print(str(diceNum) + " dice will now be rolled")
    rollPrompt(diceNum, sideNum)
  if rollPromptInput == "s" or rollPromptInput == "S":
    sideNum = int(input("Each die currently has " + str(sideNum) + " sides. Choose the new amount of sides that each die will have\n"))
    print("Each die will now have " + str(sideNum) + " sides")
    rollPrompt(diceNum, sideNum)
  for i in range(diceNum):
    print(str(random.randint(0,sideNum)))
  rollPrompt(diceNum, sideNum)

# info page
def info():
  print("\nPyDice 1.1.1")
  print("Created by Henry Donahue")
  print("https://www.github.com/hdonahue27/PyDice")
  infoInput = input("\nPress enter to return to main menu\n")
  menu()

# command list
def cmds():
  print("\nHere are the commands you can use:\n")
  print("n: Change number of dice rolled")
  print("s: Change number of sides on the dice")
  print("d: Deletes all previous roles and resets the dice settings")
  print("m: Return to main menu")
  print("q: Terminate the program")
  rollPrompt(diceNum, sideNum)

menu()