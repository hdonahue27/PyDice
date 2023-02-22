import random

def start():
    global diceNum
    diceNum = input("Choose the amount of dice you would like to roll\n")
    diceNum = int(diceNum)
    global sideNum
    sideNum = input("Choose the amount of sides that each die will have\n")
    sideNum = int(sideNum)
    print("\nTo view a list of commands, type C and press enter.")
    rollPrompt(diceNum=diceNum, sideNum=sideNum)

def cmds():
  print("\nHere are the commands you can use:\n")
  print("n: Change number of dice rolled")
  print("s: Change number of sides on the dice")
  print("d: Deletes all previous roles and resets the dice settings")
  print("q: Terminate the program")
  rollPrompt(diceNum, sideNum)    

def rollPrompt(diceNum, sideNum):
  rollPromptInput = input("\nPress enter to roll, or type a command\n")
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

start()