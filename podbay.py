from scene import Scene
from textwrap import dedent
from stats_inventory import Person, Inventory

class PodBay(Scene):

  def enter(self):

    print(dedent("""
          You see 14 identical looking escape pods except for 
          the unique number on each one. You only have the 
          launch code for one these pods but which one.
        """))

    
    escapePods = ["gaba", "gulu", "gol", "jum", "ken", "joj","gob", "lok", "moh", "goru", "jobo", "kumo", "juvi", "loto"]

    def bubSort(list):
      x = 1
      
      for item in list:
        for j in range(len(list) - x):
          if(list[j] > list[j + 1]):
            list[j], list[j + 1] = list[j + 1], list[j]
        x += 1    
      return list

    def choosePod(myList):
      name = input("Enter name of escape pod> ")
      name = name.lower()
      shipNum = myList.index(name) + 1
      print(name + " Escape Pod #: " + str(shipNum))
      return "" + str(shipNum)

    bubSort(escapePods)

    print(dedent("""There is one door 'aft' or you can 
    'select' an escape pod. What do you choose? If you 
    picked up a 'Buzz Stick' you will need to 'drop' it 
    now before getting a escape pod. The charge
    in the stick will cause the navigation system to 
    go haywire."""))
    print("\nCurrent Inventory: ")
    myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
    Inventory.item.inOrder(myRoot)
    choice = input("> ")
    while choice.lower() != "quit":     
      choice = choice.lower()
      if "aft" in choice or choice == 'a':
        return 'bridge'
      elif "drop" in choice or "stick" in choice:
        print(dedent("""The stick rolls away and drops into a nearby 
        shute never to be seen again"""))
        print("\nInventory after dropping the stick: ")
        myRoot = Inventory.item.deleteNode(myRoot, "Buzz Stick")
        Inventory.item.inOrder(myRoot)
      elif "select" in choice or "pod" in choice:
        # get root and show inventory       
        sNum = choosePod(escapePods)
        myNum = input("Ship # to escape in > ")
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        foundNode = Inventory.item.searchBST("Buzz Stick", myRoot)
        if foundNode is not None:
          print(dedent("""Unfortunately, you did not heed the
          warning about the buzz stick. The escape pod spins
          around in a circle colliding with the ship. You 
          don't survive."""))
          return 'disaster'
        elif myNum == '7':
          return 'finished'
        else:
          print(dedent("""Unfortunately, you did not choose 
          wisely. A small air leak in the pod causes it 
          to loose pressure causing it to implode on 
          itself, crushing you as you asphyxiated from 
          lack of oxygen"""))
          return 'disaster'
      elif "inventory" in choice or choice == 'i':
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot)
      
      choice = input("Your choices are 'aft' or 'select' escape pod! > ")