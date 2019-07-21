from scene import Scene
from textwrap import dedent
from stats_inventory import Person, Inventory
import numpy as np 

class Bridge(Scene):

  def enter(self):
    print(dedent("""
        You find yourself on bridge #7 and you are not alone. 
        The captain of the ship 'Dicey Roll' is blocking 
        your path to the podbay, your only hope of escape. 
        Do you 'flee' or 'fight'?
        """))

    choice = input('> ')

    if 'flee' in choice:
      print(dedent("""Looking around the bridge you see four 
      doors to the 'port', 'forward', 'starboard' and 
      'aft'. As the 'forward' door is block you choose 
      another."""))
      choice = input("> ")
      while choice.lower() != "quit":     
        choice = choice.lower()
        if "port" in choice or choice == 'p':
          return 'communication'
        elif "starboard" in choice or choice == 's':
          return 'armory'
        elif "aft" in choice or choice == 'a':
          return 'engineroom'
        else:
          print(dedent("""You stand frozen in place trying to 
          decide which door to open. You can go 'port', 
          'startboard' or 'aft'. This is a ship afterall."""))
          choice = input("> ")
    else:
      print("Get ready to fight!")
      capHealth = 10
      bonusDamage = 0
      choice = input("If you have a weapon now would be good time to 'use' it > ")
      if "use" in choice and ("stick" in choice or "buzz" in choice):
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        foundNode = Inventory.item.searchBST("Buzz Stick", myRoot)
        if foundNode is not None:
          bonusDamage = 3
        else:
          print("You were unable to pull it out in time if you actually have one.")
      print(dedent("""At first you attempt to throw him off-guard with
      vast knowledge discrete mathmatics"""))
      if Person.earthling.euler < 8:
        print(dedent("""(The captain is not amused by anecdotes on 
        'Finite State Machines and gets in the first hit."""))
        Person.earthling.health -= np.random.randint(1,3)
      else:
        print(dedent("""Your knowledge of graphs and set theory stuns him, allowing
        you the first strike."""))
      while capHealth > 0:
        damage = np.random.randint(1,5) + bonusDamage + (Person.earthling.strength - 8)
        capHealth -= damage
        if bonusDamage != 0:
          print("You swing at him with your Buzz Stick and hit him hard!\n")
        else:
          print("You swing at him with your fist and make contact.\n")
        if capHealth > 0:
          print("The captain swings at you\n")
          Person.earthling.health -= np.random.randint(1,4) 
          if Person.earthling.health <= 0:
            return 'disaster'
    print(dedent("""You have defeated the captain! You find a small manual labeled 'Launch codes for the escape pod Joj. You add this to your inventory. You can go 'port', 'aft', 'starboard' or 'forward' to the podbay."""))
    myRoot = Inventory.item.insertKey("Launch Codes for Joj")
    print("\nCurrent Inventory: ")
    Inventory.item.inOrder(myRoot)
    choice = input("> ")
    while choice.lower() != "quit":     
      choice = choice.lower()
      if "port" in choice or choice == 'p':
        return 'communication'
      elif "starboard" in choice or choice == 's':
        return 'armory'
      elif "aft" in choice or choice == 'a':
        return 'engineroom'
      elif "forward" in choice or choice == 'f':
        return 'podbay'
      elif "inventory" in choice or choice == 'i':
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot)
     
      print(dedent("""\nYou stand frozen in place trying to 
      decide which door to open. You can go 'port', 
      'startboard' or 'aft'. This is a ship afterall."""))
      choice = input("> ")