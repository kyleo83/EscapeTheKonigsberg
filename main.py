from engine_map import Engine, Map


class Main():


  def main():
    s_map = Map('brig')
    s_game = Engine(s_map)
    s_game.play()


  if __name__=='__main__':
    main()