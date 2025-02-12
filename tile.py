reset = "\033[0m"
yellow = "\033[33m"
green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"
white = "\033[97m"
magenta = "\033[35m"
cyan = "\033[36m"

class Tile:
    def __init__(self, symbol: str, color: str = reset, colored: bool = True):
        if colored:
            self.symbol = f"{color}{symbol}{reset}"
        else:
            self.symbol = symbol

plains = Tile(" ", reset)
forest = Tile("8", green)
town = Tile("#", white)
bridge = Tile("=", reset)
mountain = Tile("A", cyan)
cave = Tile("0", magenta)
water = Tile("~", blue)