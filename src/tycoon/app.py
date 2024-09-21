import rich

from . import game

if __name__ == "__main__":
    print("Starting")
    mygame = game.Game()
    mygame.run()
    print("done")
