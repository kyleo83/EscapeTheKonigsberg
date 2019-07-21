from textwrap import dedent
from scene import Scene
from stats_inventory import Person, Inventory


class  Brig(Scene, Person, Inventory):

  def enter(self):

    Person.setPerson(self)
   
    print(dedent("""\nYou awaken with a splitting headache and sit up. 
      What happed? One
      minute you are an Ambassador from Earth meeting with these 
      Descrete math crazed Eulerians. You remember eavesdropping
      on a conversation on your way to the head. Something about
      a secret plan to attack Earth. You gotta do something but 
      what?"""))
      
    print(dedent("""\nLooking around you find yourself in a small room.
    There is a closed door facing you, a small sink to 
    the left and a toilet to the right. You are 
    sitting on metal cot that is attached to the 
    wall. Looking on the floor you see a small 
    rectangular piece of paper that must have 
    fallen out of the guard's pocket.\n"""))

    count = 0
    
    while count < 2:
      print(dedent("""Do you attempt to go 'forward' through 
      the door? You can also 'pick' up 
      the 'paper' from the floor.\n"""))
      choice = input("> ")
      if 'pick' in choice or 'paper' in choice:
        print(dedent("""\nBefore adding the scrap of 'paper'
        to your inventory you examine it carefully. 
        In what appears to be a calculator font is 
        written the word 'hELLO'. This just might 
        be a passcode but the Eulerians usually 
        use numbers.\n"""))
        print("Your inventory:")
        myRoot = Inventory.setInventory(self)
        Inventory.item.inOrder(myRoot)
        count += 2
      elif count < 1:
        print(dedent("""You try the door and get thrown 
        to the floor by a strong electrical shock. 
        Another shock like that might kill you!\n"""))
        count += 1
      else:
        print(dedent("""The second shock is even stronger. 
        You fall to the floor dead, while the smoke 
        from your head sets off the sprinkler system.\n"""))
        return 'disaster'
  
    print("There is keypad next to the door:")
    choice = input("What do you want to 'use' now? > ")
    while choice:
      if 'use' in choice and ('keypad' in choice or 'passcode' in choice):
        def passcode():
          codeOne = "07734"
          strCode = []
          count = 0
          decCode = 0

          def dec2bin(x):
            binDigit = ""
            while x != 0:
              digit = x % 2
              x = int( x / 2 )
              binDigit = str(digit) + binDigit
            return binDigit

          while strCode != codeOne:
            strCode = input("Enter passcode: ")
            if strCode == codeOne:
              decCode = int(strCode)
            elif count < 1:
              print(dedent("""A decimal number exactly matching 
              the passcode is expected here. Hurry, you have 
              one more chance to enter the correct passcode 
              before the guard wakes up and enters the room!\n"""))
              count += 1
            else:
              return 0

          # print(decCode)
          binCode = dec2bin(decCode)
          # print("binary code: " + str(binCode))
          strBin = input("Enter passcode's binary value: ")

          # print("strBin[0]: " + str(strBin[0]))
          strBin = strBin.lstrip("0")

          # print("strBin :" + str(strBin))
          if strBin == binCode:
            print(dedent("""The door slides open allowing you to 
            exit. The door slides shut behind you.\n"""))
            return 1
          else:
            print(dedent("""A sharp pain to the head from a blunt
            object is the last thing you remember as you slump 
            to the floor. If you only paid better attention in
            discrete math class, it might have saved your life.\n"""))
            return 0
          
        if passcode() == 1:
          return 'engineroom'
        else:
          return 'disaster'
      elif choice == 'q':
        return 'disaster'
      else:
        print("Try Again! With words like 'use' and 'keypad'.")
        choice = input(" > ")


    