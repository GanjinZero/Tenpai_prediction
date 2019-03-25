from keras.models import load_model
import numpy as np
from generate_train_data import generate_train_data
from haifu_parser import show_richi_player_sutehai, load_data, richi_filter
from haifu_parser import show_richi_player_sutehai_list


model = load_model("../model/tenpai.model")
x_data, y_data = generate_train_data('test')

pad_dim = int(model.input.shape[1])


def pad_sample(x, pad_dim):
    zeros = np.zeros((pad_dim - x.shape[0], 52))
    return np.concatenate((zeros, x), axis=0).reshape(1, pad_dim, 52)


def predict(x):
    p = model.predict(pad_sample(x, pad_dim))[0]
    return p / sum(p)


def number_to_tile(num):
    if num <= 26:
        k = num // 9
        numb = num % 9 + 1
        follow = "m"
        if k == 1:
            follow = "p"
        if k == 2:
            follow = "s"
        return str(numb) + follow
    z_list = "東南西北白発中"
    return z_list[num - 27]


def predict_first_five(x):
    prob = predict(x)
    order = prob.argsort()[-5:].tolist()
    order.reverse()
    result = dict()
    for num in order:
        result[number_to_tile(num)] = round(prob[num], 2)
    return result


def print_y(y):
    print("Richi player tenpai:",
          [number_to_tile(num) for num in range(34) if y[num] == 1])


def check_example(index):
    print("Predict tenpai:",
          predict_first_five(x_data[index]))
    print_y(y_data[index])


# test_list = load_data("../data/sample.txt")
test_list = load_data("../data/test.txt")
richi_data = richi_filter(test_list)


def check_example_with_sutehai(index):
    print("Richi player sutehai:",
          show_richi_player_sutehai(richi_data[index]))
    check_example(3 * index - 2)
    check_example(3 * index - 1)
    check_example(3 * index)


if __name__ == "__main__":
    check_example_with_sutehai(0)
    """
    check_example_with_sutehai(2)
    check_example_with_sutehai(3)
    check_example_with_sutehai(4)
    check_example_with_sutehai(5)
    check_example_with_sutehai(6)
    check_example_with_sutehai(7)
    """

