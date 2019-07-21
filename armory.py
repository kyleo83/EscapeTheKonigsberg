from scene import Scene
from textwrap import dedent
from stats_inventory import Person, Inventory

class Armory(Scene):

  def enter(self):
    print(dedent("""You enter the armory! Along the wall are 
    several Buzz Sticks. A Club with an electrical shock\n
      """))

    print(dedent("""There are doors 'forward' and 'port'."""))
    choice = input("> ")
    while choice.lower() != "quit":     
      choice = choice.lower()
      if "forward" in choice or choice == 'f':
        return 'bridge'
      elif "port" in choice or choice == 'p':
        return 'engineroom'
      elif "buzz" in choice or "stick" in choice:
        myRoot = Inventory.item.insertKey("Buzz Stick")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot)
      elif "inventory" in choice or choice == 'i':
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot)
      choice = input("\nThere are doors 'forward' and 'port'. > ")