from mahjong.tile import TilesConverter
from tenpai import tenpai
# man pin sou z1234567 东南西北白发中

def change_tile_to_number(tile):
    if len(tile) == 2:
        number = int(tile[0])
        k = 0
        if tile[1] == "p":
            k = 1
        if tile[1] == "s":
            k = 2
        return k * 9 + number - 1
    z_list = "東南西北白発中"
    return z_list.find(tile) + 27

def parse_start_hand(tiles):
    tiles_34 = [0] * 34
    i = 0
    while i < len(tiles):
        if '1' <= tiles[i] <= '9':
            now_tile = tiles[i:i + 2]
            tiles_34[change_tile_to_number(now_tile)] += 1
            i += 2
        else:
            now_tile = tiles[i]
            tiles_34[change_tile_to_number(now_tile)] += 1
            i += 1
    return tiles_34

def parse_haifu(haifu):
    '''
    Not finished
    '''
    # haifu has 6 lines
    dora_position = haifu[4].find("[裏ドラ]")
    dora_string = haifu[4][5:dora_position - 1]
    #dora = TilesConverter.string_to_34_array(dora_string)
    
    richi_position = haifu[5].find("R")
    first_richi_player = int(haifu[5][richi_position - 1])
    haifu[5] = haifu[5][0:richi_position + 1]
    
    # Generate input
    player_list = [1, 2, 3, 4]
    for player in player_list:
        if player != first_richi_player:
            start_hand = parse_start_hand(haifu[player - 1])
            
    
    # Generate output        
    start_hand_richi = parse_start_hand(haifu[first_richi_player - 1])
    sute = [False] * 34
    for action in haifu[5].split(" "):
        if action[0] == str(first_richi_player):
            if action[1] == "G":
                now_tile = action[2:]
                start_hand_richi[change_tile_to_number(now_tile)] += 1
            if action[1] == "D" or action[1] == "d":
                now_tile = action[2:]
                tile_number = change_tile_to_number(now_tile)
                start_hand_richi[tile_number] -= 1
                sute[tile_number] = True
    tenpai_result = tenpai(start_hand_richi, sute)
    
    return None

def check_haifu(st):
    haifu_checker = ["[1東", "[1南", "[1西", "[1北"]
    for checker in haifu_checker:
        if st.find(checker) != -1:
            return 1
    return -1
    
def load_data(file_name):
    # For haifu from 東風荘
    haifu_list = []

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        use_line = 0
        while use_line != len(lines):
            if check_haifu(lines[use_line]) == -1:
                use_line += 1
            else:
                haifu_now = lines[use_line: use_line + 5]
                use_line = use_line + 5
                sute = ""
                star = lines[use_line].find("*")
                while star != -1:
                    sute += lines[use_line][star + 1:]
                    use_line += 1
                    star = lines[use_line].find("*")
                haifu_now.append(sute.strip())
                haifu_list.append(haifu_now)    

    return haifu_list

def richi_filter(haifu_list): 
    return [haifu for haifu in haifu_list if haifu[5].find("R")!=-1]

if __name__ == "__main__":
    test_list = load_data("../data/sample.txt")
    #test_list = load_data("../data/totuhaihu.txt")
    richi_data = richi_filter(test_list)