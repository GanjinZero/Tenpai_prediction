def parse_haifu(haifu):
    return 0

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
    #test_list = load_data("../data/sample.txt")
    test_list = load_data("../data/totuhaihu.txt")
    richi_data = richi_filter(test_list)