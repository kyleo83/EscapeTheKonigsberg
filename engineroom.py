import numpy as np 
import pandas as pd
import pprint
from scene import Scene
from textwrap import dedent
from cipher import Cipher
from stats_inventory import Person, Inventory

class EngineRoom(Scene):

  def enter(self):


    print(dedent("""You enter the engine room. You are alone. 
    In the center of the room is console. Now would 
    be the perfect time to download the secret plans 
    you heard so much about. Before you is a computer
    you can access to get the secrect plans.
    """))


    def masterMind():
      count = 0
      black = 0
      guesses = []
      masterDict = {}

      print(dedent("""To access the secret plans you first need 
      to bypass their security by solving a game of 
      MasterMind on the computer. It looks like your 
      love of puzzle games from the 70's wasn't a waste 
      of time after all. You sit down at the computer and 
      attempt to break the code\n"""))
      
      colors_dict = { 0: "red", 1: "green", 2: "yellow", 3: "white", 4: "blue", 5: "orange"}
      result = np.random.randint(0,6, size = 4)
      # left in for testing
      print("MasterMind Numeric Solution:")
      print(result)
      print("For testing\n")

      odds = round(1/(6**4) * 100,4)

      print("Ha, Ha, your chances of winning on the first guess are " + str(odds) + "%.")
      print(dedent("""But you will get clues with each guess. The correct 
      colored peg in the correct column will be counted as 
      such. A correct color in an incorrect column will also be 
      counted separately. A peg will only be counted once."""))

      while black < 4 and count < 10:

        subChoice = []
        subResult = []
        choice = []
        black = 0
        white = 0
        count += 1

        print(dedent("""\nChoose between the colors red, green, yellow, 
        white, blue, and orange. You have ten attempts 
        to get this right.\n"""))

        choice.append(input("Enter color choice for the first peg: "))
        choice.append(input("Enter color choice for the second peg: "))
        choice.append(input("Enter color choice for the third peg: "))
        choice.append(input("Enter color choice for the four peg: "))

        for i in range(len(choice)):
          # print(choice[i][0])
          if (colors_dict[result[i]] == choice[i]):
            black += 1
          else:
            color = colors_dict[result[i]]
            subResult.append(color)
            subChoice.append(choice[i])
        
        for i in range(len(subChoice)):
          for j in range(len(subResult)):
            if (subChoice[i] == subResult[j]):
              white += 1
              subResult.pop(j)
              break;

        masterDict[count] = (choice, black, white)
        df = pd.DataFrame.from_dict(masterDict, orient='index',
             columns=['Guesses','Black','White'])
        print(df)
          
        print("\nCorrect color and position: " + str(black))
        print("Correct color only: " + str(white))

      if black == 4:
        print(dedent("""You have solved the puzzle! The secret plans to destroy the Earth are printed on a loud line-feed printer. You hope no one is listening. You sweat profusely as you wait for the printer to finish. Before placing the secret message in your pack you take a quick look at it. You're gonna need a key to solve this one.\n"""))
        text = Cipher.textToEncode 
        shiftKey = Cipher.shiftKey
        message = Cipher.shiftCipher(text, shiftKey)
        print(message)

        print("\nYour Inventory: ")
        myRoot = Inventory.item.insertKey("Top secret message")
        Inventory.item.inOrder(myRoot)
        return True

      else:
        print(dedent("""Oops, you are out of chances. A security 
        force of Eulerians swoops in and zaps 
        you out of existance."""))
        return False
    
    print(dedent("""\nLooking around the engine room you see 
    three doors to the 'port', 'forward' and 'starboard'. 
    There is a computer before you. Which do you choose?"""))
    choice = input("> ")
    while choice.lower() != "quit":     
      choice = choice.lower()
      if "port" in choice or choice == 'p':
        return 'communication'
      elif "forward" in choice or choice == 'f':
        return 'bridge'
      elif "starboard" in choice or choice == 's':
        return 'armory'
      elif "inventory" in choice or choice == 'i':
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot)
      elif 'use' in choice:
        if masterMind() == False:
          return 'disaster'
      print(dedent("""\nYou stand frozen in place trying to 
      decide which door to open. You can go 'port', 
      'forward' towards the bow or 'startboard'. 
      This is a ship afterall."""))
      choice = input(">")

    
      