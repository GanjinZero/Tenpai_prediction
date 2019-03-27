import copy
import random
from haifu_parser import load_data 


z = "中"
h = "発"
b = "白" 
def transform_1(string, mode):
    if mode == 1:
        def f(char):
            if char == z:
                return h
            if char == h:
                return b
            if char == b:
                return z
            return char
    if mode == 2:
        def f(char):
            if char == z:
                return h
            if char == h:
                return z
            return char
    if mode == 3:
        def f(char):
            if char == z:
                return b
            if char == h:
                return z
            if char == b:
                return h
            return char
    if mode == 4:
        def f(char):
            if char == z:
                return b
            if char == b:
                return z
            return char
    if mode == 5:
        def f(char):
            if char == h:
                return b
            if char == b:
                return h
            return char
    return ''.join([f(ch) for ch in list(string)])


def transform_2(string, mode):
    if mode == 1:
        def f(char):
            if char == 'm':
                return 'p'
            if char == 'p':
                return 's'
            if char == 's':
                return 'm'
            return char
    if mode == 2:
        def f(char):
            if char == 'm':
                return 'p'
            if char == 'p':
                return 'm'
            return char
    if mode == 3:
        def f(char):
            if char == 'm':
                return 's'
            if char == 'p':
                return 'm'
            if char == 's':
                return 'p'
            return char
    if mode == 4:
        def f(char):
            if char == 'm':
                return 's'
            if char == 's':
                return 'm'
            return char
    if mode == 5:
        def f(char):
            if char == 'p':
                return 's'
            if char == 's':
                return 'p'
            return char
    return ''.join([f(ch) for ch in list(string)])


def transform_3(string, begin=0):
    lst = list(string)
    for i in range(begin, len(lst)):
        if '1' <= lst[i] <= '9':
            lst[i] = str(10 - int(lst[i]))
    return ''.join(lst)


def transform_3_history(string):
    lst = string.split(" ")
    for j in range(len(lst)):
        word = list(lst[j])
        for i in range(2, len(word)):
            if '1' <= word[i] <= '9':
                word[i] = str(10 - int(word[i]))
        lst[j] = ''.join(word)
    return ' '.join(lst)


def generate_one_fake_haifu(haifu, mode):
    # (a,b,c) -> (b,c,a) -> (c,a,b) -> (b,a,c) -> (c,b,a) -> (a,c,b)
    # (1). chun, hatsu, haku 
    # (2). man, pin, sou
    # (3). 123456789 -> 987654321
    # Total 6*6*2=72 kinds of transformation
    # mode in [0, 35] not do (3); mode in [36, 71] do (3)
    # (mode % 36) mod 6 -> transformation type in (2)
    # (mode % 36) // 6 -> transformation type in (1)

    # Haifu format
    # [1北]1m...
    # [2...
    # [3...
    # [4...
    # [表ドラ]2p [裏ドラ]9m
    # 2G9m ...
    # 東1局 0本場(リーチ0) ...

    mode_3 = mode // 36
    mode_2 = (mode % 36) % 6
    mode_1 = (mode % 36) // 6
    fake_haifu = copy.copy(haifu)
    if mode_3 == 1:
        for i in range(4):
            fake_haifu[i] = transform_3(fake_haifu[i], begin=4)
        fake_haifu[4] = transform_3(fake_haifu[4])
        fake_haifu[5] = transform_3_history(fake_haifu[5])

    if mode_2 > 0:
        for i in range(6):
            fake_haifu[i] = transform_2(fake_haifu[i], mode_2)
    
    if mode_1 > 0:
        for i in range(6):
            fake_haifu[i] = transform_1(fake_haifu[i], mode_1)
    return fake_haifu


def generate_fake_haifu(haifu, fake_number):
    fake_haifu_list = []
    
    if fake_number > 0:
        random_mode = random.sample(range(72), fake_number)

        for mode in random_mode:
            if mode > 0:
                fake_haifu_list.append(generate_one_fake_haifu(haifu, mode))
    return fake_haifu_list


if __name__ == "__main__":
    data = load_data('../data/test.txt')
    hf = data[0]
    print(hf)
    f = generate_fake_haifu(hf, 10)
    for h in f:
        print(h)
