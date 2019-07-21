from sys import exit


class Scene(object):
    """Base class for Scene child classes."""

    def enter(self):
        print("The scene you have selected is still under construction.")
        exit(1)
