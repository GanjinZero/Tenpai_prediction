import numpy as np
import time
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from generate_fake_haifu import generate_fake_haifu
from haifu_parser import load_data
from haifu_parser import richi_filter
from haifu_parser import parse_haifu
from haifu_parser import action_to_vector


def generate_train_data(file_name):
    # 600 haifus/1s

    time_start = time.time()
    x_data = []
    y_data = []

    file_path = "../data/" + file_name + ".txt"
    # test_list = load_data("../data/sample.txt")
    # test_list = load_data("../data/totuhaihu.txt")
    test_list = load_data(file_path)

    richi_data = richi_filter(test_list)

    fake_haifu_number = 5 # Too big will cause Out of Memory
    # fake_haifu_number = 0
    new_richi_data = []
    for haifu in richi_data:
        new_richi_data.append(haifu)
        new_richi_data += generate_fake_haifu(haifu, fake_haifu_number)
        if len(new_richi_data) % 1000 == 0:
            print(len(new_richi_data), round(time.time() - time_start, 2))
    print(len(new_richi_data))    

    for haifu in new_richi_data:
        inp, chanfon, jikaze, dora_list, tenpai_result, sute = parse_haifu(haifu)
        for each_inp in inp:
            x = []
            player = each_inp[0]
            for action in each_inp.split(" "):
                if action != "":
                    x.append(action_to_vector(action, player, chanfon,
                                              jikaze, dora_list))
            x_data.append(np.array(x))
            y_data.append(tenpai_result)
            if len(y_data) % 2000 == 0:
                print(len(y_data), round(time.time() - time_start, 2))
    x_data_numpy = np.array(x_data)
    y_data_numpy = np.array(y_data)

    time_end = time.time()
    print('Generate train data cost %s seconds.' %
          round((time_end - time_start), 2))
    print('Haifu number: %s' % y_data_numpy.shape[0])

    return x_data_numpy, y_data_numpy


def generate_test_data(file_name):
    x_data = []
    y_data = []
    assistant_data = []

    file_path = "../data/" + file_name + ".txt"
    test_list = load_data(file_path)
    richi_data = richi_filter(test_list)

    for haifu in richi_data:
        inp, chanfon, jikaze, dora_list, tenpai_result, sute = parse_haifu(haifu)
        for each_inp in inp:
            x = []
            player = each_inp[0]
            for action in each_inp.split(" "):
                if action != "":
                    x.append(action_to_vector(action, player, chanfon,
                                              jikaze, dora_list))
            x_data.append(np.array(x))
            y_data.append(tenpai_result)
            assistant_data.append([player, sute])
    x_data_numpy = np.array(x_data)
    y_data_numpy = np.array(y_data)

    return x_data_numpy, y_data_numpy, assistant_data


def pad_x(x_data):
    x_len = []
    for i in range(len(x_data)):
        x_len.append(x_data[i].shape[0])
    max_x_len = max(x_len)
    x_data_ret = np.zeros((len(x_data), max_x_len, 52))

    for i in range(len(x_data)):
        zeros = np.zeros((max_x_len - x_data[i].shape[0], 52))
        x_data_ret[i] = np.concatenate((zeros, x_data[i]), axis=0)
    return x_data_ret


def shuffle_split(x_data, y_data):
    # x_data, y_data = shuffle(x_data, y_data)
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,
                                                        test_size=0.2)
    return x_train, x_test, y_train, y_test


def generate_train_test():
    x_data_0, y_data_0 = generate_train_data("totuhaihu")
    x_data_1, y_data_1 = generate_train_data("kintaro")
    x_data_2, y_data_2 = generate_train_data("mjscore")
    x_data_3, y_data_3 = generate_train_data("momosescore")
    x_data_4, y_data_4 = generate_train_data("score")
    print(x_data_0.shape)
    print(x_data_1.shape)
    print(x_data_2.shape)
    print(x_data_3.shape)
    print(x_data_4.shape)
    x_data = np.concatenate((x_data_0, x_data_1, x_data_2, x_data_3, x_data_4), axis=0)
    y_data = np.concatenate((y_data_0, y_data_1, y_data_2, y_data_3, y_data_4), axis=0)
    x_data = pad_x(x_data)
    x_train, x_test, y_train, y_test = shuffle_split(x_data, y_data)
    return x_train, x_test, y_train, y_test


local_place = "/media/veritas/95af80a9-ce6b-4f40-8cb3-9bfe602478f1/veritas/GanjinZero/haifu/"
def save_train_data():
    x_data_0, y_data_0 = generate_train_data("totuhaihu")
    x_data_1, y_data_1 = generate_train_data("kintaro")
    x_data_2, y_data_2 = generate_train_data("mjscore")
    x_data_3, y_data_3 = generate_train_data("momosescore")
    x_data_4, y_data_4 = generate_train_data("score")
    print(x_data_0.shape)
    print(x_data_1.shape)
    print(x_data_2.shape)
    print(x_data_3.shape)
    print(x_data_4.shape)
    x_data = np.concatenate((x_data_0, x_data_1, x_data_2, x_data_3, x_data_4), axis=0)
    y_data = np.concatenate((y_data_0, y_data_1, y_data_2, y_data_3, y_data_4), axis=0)
    x_data = pad_x(x_data)
    # np.save("../model/x_data.npy", x_data)
    # np.save("../model/y_data.npy", y_data)
    np.save(local_place + "x_data.npy", x_data)
    np.save(local_place + "y_data.npy", y_data)
    print("Train data generate and save on local place")


def generate_train_test_local():
    x_data = np.load(local_place + "x_data.npy")
    y_data = np.load(local_place + "y_data.npy")
    x_train, x_test, y_train, y_test = shuffle_split(x_data, y_data)
    return x_train, x_test, y_train, y_test


if __name__ == "__main__":
    save_train_data()

