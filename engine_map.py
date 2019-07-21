from brig import Brig
from communication import Communication
from finished import Finished
from disaster import Disaster
from armory import Armory
from engineroom import EngineRoom
from bridge import Bridge
from podbay import PodBay


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # sets the opening scene to the current scene.
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # Call the finished class
        current_scene.enter()


class Map(object):

    scenes = {'communication': Communication(),
              'finished': Finished(),
              'disaster': Disaster(),
              'armory': Armory(),
              'engineroom': EngineRoom(),
              'bridge': Bridge(),
              'brig': Brig(),
              'podbay': PodBay()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = self.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)