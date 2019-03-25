from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter


def tenpai(tiles, sute):
    shanten = Shanten()
    if len(tiles) == 34:
        # [3,1,1,...,3,0,...,0]
        tiles_34 = tiles
    else:
        # man='1112345678999', pin='', sou='', honors=''
        tiles_34 = TilesConverter.string_to_34_array(tiles)

    result = [0] * 34
    for i in range(34):
        if tiles_34[i] < 4 and not sute[i]:
            tiles_34[i] += 1
            if shanten.calculate_shanten(tiles_34) == -1:
                result[i] = 1
            tiles_34[i] -= 1
    return result


if __name__ == "__main__":
    """
    shanten = Shanten()
    tiles = TilesConverter.string_to_34_array(man='11122233', honors='111777')
    result = shanten.calculate_shanten(tiles)
    print(result)
    """

    sute = [False] * 34
    sute[1] = True
    tiles = [3, 1, 1, 1, 1, 1, 1, 1, 3] + [0] * 25
    print(tenpai(tiles, sute))
