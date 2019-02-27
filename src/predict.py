from keras.models import load_model
import numpy as np
from generate_train_data import generate_train_data


model = load_model("../model/tenpai.model")
x_data, y_data = generate_train_data('sample')

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
    return [number_to_tile(num) for num in order]


def print_y(y):
    print([number_to_tile(num) for num in range(34) if y[num] == 1])


def check_example(index):
    print(predict_first_five(x_data[index]))
    print_y(y_data[index])


if __name__ == "__main__":
    check_example(0)
    check_example(3)
    check_example(6)
    check_example(9)
    check_example(12)
    check_example(15)
    check_example(18)
    check_example(21)
