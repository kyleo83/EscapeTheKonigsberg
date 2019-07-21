from sys import exit
from scene import Scene


class Disaster(Scene):

  def enter(self):
      print("That's all folks!")
      exit(1)