from sys import exit
from textwrap import dedent
from scene import Scene
from stats_inventory import Person, Inventory


class Finished(Scene):

  def enter(self):
    if Person.earthling.plans == True:
      print(dedent("""
          As you speed along in the vast emptiness of space
          you watch as the The Königsberg explodes scattering
          debris in all directions. The Earth has been warned 
          and you escaped unscathed. Now if you can only figure 
          out the controls on this escape pod."""))
    else:
      print(dedent("""
          As you speed along in the vast emptiness of space
          you wonder what will happen to Earth, since you neither
          transmitted the secret plans to attack Earth nor destroyed
          the space ship Königsberg. You have survived another day
          but for how long with the Eulerians after you?"""
          ))
    exit(1)