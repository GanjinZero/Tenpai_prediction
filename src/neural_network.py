from generate_train_data import generate_train_test_local
from keras.layers import Input, CuDNNLSTM, Dropout
from keras.layers import Dense
from keras.models import Model
from keras.optimizers import Adam


if __name__ == "__main__":
    # x_train, x_test, y_train, y_test = generate_train_test()
    x_train, x_test, y_train, y_test = generate_train_test_local()

    # Model
    inp = Input(shape=(x_train[0].shape[0], 52))
    x = CuDNNLSTM(256, return_sequences=True)(inp)
    x = Dropout(0.1)(x)
    """
    x = CuDNNLSTM(256, return_sequences=True)(x)
    x = Dropout(0.1)(x)
    x = CuDNNLSTM(256, return_sequences=True)(x)
    x = Dropout(0.1)(x)
    """
    x = CuDNNLSTM(256, return_sequences=False)(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation="relu")(x)
    x = Dropout(0.1)(x)
    x = Dense(64, activation="relu")(x)
    x = Dropout(0.1)(x)
    output = Dense(34, activation="softmax")(x)

    model = Model(inputs=inp, outputs=output)
    opt = Adam(lr=0.001, beta_1=0.9, beta_2=0.999,
               epsilon=None, decay=0.0, amsgrad=False)

    # Which kind of loss to use?
    # We should write another metrics
    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['categorical_crossentropy'])
    print(model.summary())

    epoch_nb = 80
    batch = 64

    model.fit(x_train, y_train, batch_size=batch, epochs=epoch_nb,
              verbose=1, validation_data=(x_test, y_test))

    model.save("../model/tenpai.model")
