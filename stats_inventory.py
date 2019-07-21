import numpy as np
from itertools import permutations

class PlayerStats(object):


  def __init__(self, name):
    self.name = name
    result = np.random.randint(6,11, size = 3)
    allPerms = permutations(result, 3)
    self.strength = result[0]
    self.health = result[1]
    self.euler = result[2]
    self.plans = False


  def toString(self):
    print("Strength = " + str(self.strength))
    print("Health = " + str(self.health))
    print("Euler = " + str(self.euler))  


class PlayerInventory(object):

  class Node():
    def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      

  def insertKey(self, num, root = Node("Lincoln Head Penny 1909 VBS")):

    if root is None:
      root = self.Node(num)
    elif num > root.key:
      if root.right == None:
        root.right = self.Node(num)
      else:
        self.insertKey(num, root.right)
    elif num < root.key:
      if root.left == None:
        root.left = self.Node(num)
      else:
        self.insertKey(num, root.left)
    # In case root is None 
    return root

  def inOrder(self, root):
    if root:
      self.inOrder(root.left)
      print(root.key)     
      self.inOrder(root.right)

  def searchBST(self, num, root = "Lincoln Head Penny 1909 VBS"):
    if root is None:
      return root
    if num < root.key:
      return self.searchBST(num, root.left)
    elif num > root.key:
      return self.searchBST(num, root.right)
    else:
      return root  
  
  def deleteNode(self, root, key):
    
    if root is None:
      return root  
    # Traverse until find node to be deleted 
    if key < root.key:
      root.left = self.deleteNode(root.left, key)
    elif key > root.key:
      root.right = self.deleteNode(root.right, key)
    else:  # key is found to be deleted
      # Node with one child or no children
      if root.left is None:
        temp = root.right 
        root = None 
        return temp
      elif root.right is None:
        temp = root.left 
        root = None 
        return temp 
      # Node with 2 children  
      # inorder successor - smallest in the right subtree
      temp = minValueNode(root.right)
      # Copy the inorder successor content to this Node
      root.key = temp.key
      # Delete the inoreer successor
      root.right = self.deleteNode(root.right, temp.key)
    return root

class Person:
  
  earthling = PlayerStats("dummy")

  def setPerson(self):
    name = input("Player Name > ")
    self.earthling.name = name
    print("Hello " + self.earthling.name + ", here are your player stats:")
    self.earthling.toString()

class Inventory:

  item = PlayerInventory()

  def setInventory(self):
    return self.item.insertKey("Paper with passcode")
  

