from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter

def tenpai():
    return 0

if __name__ == "__main__":
    shanten = Shanten()
    tiles = TilesConverter.string_to_34_array(man='1112345678999')
    result = shanten.calculate_shanten(tiles)
    print(result)