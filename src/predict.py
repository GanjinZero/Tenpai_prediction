from keras.models import load_model
import numpy as np
from generate_train_data import generate_test_data


model = load_model("../model/tenpai.model")
x_data, y_data, assistant_data = generate_test_data('test')

pad_dim = int(model.input.shape[1])


def pad_sample(x, pad_dim):
    zeros = np.zeros((pad_dim - x.shape[0], 52))
    return np.concatenate((zeros, x), axis=0).reshape(1, pad_dim, 52)


def predict(x, sute):
    p = model.predict(pad_sample(x, pad_dim))[0]
    for i in range(len(sute)):
        if sute[i]:
            p[i] = 0
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


def print_tenpai(y):
    print("Richi player tenpai:",
          [number_to_tile(num) for num in range(34) if y[num] == 1])


def predict_with_assistant(x, y, assist):
    player, sute = assist
    result = dict()
    threshold = 0.01

    prob = predict(x, sute)
    print_tenpai(y)
    print("Player " + str(player) + ": ")
    for i in range(len(prob)):
        if prob[i] > threshold:
            result[number_to_tile(i)] = prob[i]
    print(result)


def predict_by_order(i):
    predict_with_assistant(x_data[i], y_data[i], assistant_data[i])


if __name__ == "__main__":
    cnt = x_data.shape[0]
    for i in range(cnt):
        predict_by_order(i)

