from textwrap import dedent
from scene import Scene
from cipher import Cipher
from itertools import permutations
from stats_inventory import Person, Inventory

class Communication(Scene):

  def enter(self):

    print(dedent("""You enter the communications room. This 
    would be a great place to decode and transmit the secret 
    message you printed out.
      """))
         
    text = Cipher.textToEncode 
    shiftKey = Cipher.shiftKey
    myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
    foundNode = Inventory.item.searchBST("Top secret message", myRoot)
    if foundNode is not None:
      print("You look at the encoded secret message.\n")
      message = Cipher.shiftCipher(text, shiftKey)
      print(message)

    print("\nIn front of you there is a cipher set used to set the daily key. Do you choose to 'solve' the 'cipher' or go through an exit 'forward' or 'starboard'.")

    choice = input(" > ")

    if 'forward' in choice or choice == 'f':
      return 'bridge'

    elif 'starboard' in choice or choice == 's':
      return 'engineroom'

    elif foundNode is not None and Person.earthling.plans == 0:
      print(dedent("""\nThis looks like a Vigenère cipher to you.
      To determine the common word that is the cipher key
      you'll need to find the intersection of two sets
      and the union of this new set with the third set.
      Here are the three sets needed to determine the key. 
      Unscramble the letters in the correct set to form the 
      cipher key.\n"""))

      setA = {'e', 'k', 'b', 't'}
      setB = {'a', 'r', 'h'}
      setC = {'t', 'j', 'a', 'e'}

      print("A " + str(setA))
      print("B " + str(setB))
      print("C " + str(setC))

      choice = input("Enter the letter of the set to unite with the first two > ")
      choice = choice.upper()
      while choice != 'D':
        unionABC = {}
        if choice == 'A':
          intersectBC = setB & setC
          unionABC = setA | intersectBC 

        elif choice == 'B':
          intersectAC = setA & setC
          unionABC = setB | intersectAC

        elif choice == 'C':
          intersectAB = setA & setB
          unionABC = setC | intersectAB

        else:
          print("Please enter the letter 'A', 'B' or 'C'")
        if unionABC != {}:
          listABC = list(unionABC)
          print(listABC)
          perms = permutations(unionABC)
          numPerms = len(list(perms))
          print("There are " + str(numPerms) + " permutations.")
          print("Here is the set as a sorted list: ")
          listABC.sort()
          print(listABC)
        choice = input("Enter D to decipher or A, B, C to produce another jumbled cipher > ")
        choice = choice.upper()

      myKey = input("Enter the cipher key > ")

      print("The computer screen displays the decoded message:\n")

      decodedMessage = Cipher.unShiftCipher(message, myKey)
      print(decodedMessage)

      print(dedent("""Now would be a good time to transmit the
      decoded message to earth. All you need to 
      do is press the red button."""))
      
      print(dedent("""\nThere are doors 'forward' and 'starboard' and
      a big red 'button'."""))
      choice = input("> ")
      while choice.lower() != "quit":     
        choice = choice.lower()
        if "forward" in choice or choice == 'f':
          return 'bridge'
        elif "starboard" in choice or choice == 's':
          return 'engineroom'
        elif "inventory" in choice or choice == 'i':
          myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
          print("Your inventory:")
          Inventory.item.inOrder(myRoot)
        elif "button" in choice or "push" in choice:
          print(dedent("""\nThere are two red buttons! So you 
          press both of them to be sure. That did it. 
          Now earth has a fighting chance. You wonder 
          what the other button is for..."""))
          print(dedent("""\nOver the computers speakers you hear a soothing voice, 'The ship will explode in 13 minutes.'"""))
          Person.earthling.plans = True
        print("Your choices are 'forward' and 'starboard', Matey!")
        choice = input("> ")

    elif "inventory" in choice or choice == 'i':
        myRoot = Inventory.item.insertKey("Lincoln Head Penny 1909 VBS")
        print("Your inventory:")
        Inventory.item.inOrder(myRoot) 

    
    print(dedent("""You return to the engine room just
     case you still need the secret plans"""))
    return 'engineroom'

