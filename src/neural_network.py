from generate_train_data import generate_train_test_local
from keras.callbacks import Callback
from keras.layers import Input, CuDNNLSTM, Dropout
from keras.layers import Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.utils import multi_gpu_model
from LossHistory import LossHistory


class MyCbk(Callback):
    def __init__(self, model):
        self.model_to_save = model

    def on_epoch_end(self, epoch, logs=None):
        self.model_to_save.save('../model/tenpai_epoch_%d.model' % epoch)


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

    par_model = multi_gpu_model(model, gpus=2)

    opt = Adam(lr=0.001, beta_1=0.9, beta_2=0.999,
               epsilon=None, decay=0.0, amsgrad=False)

    # Which kind of loss to use?
    # We should write another metrics
    par_model.compile(loss='categorical_crossentropy',
                      optimizer=opt,
                      metrics=['categorical_crossentropy'])
    print(model.summary())

    epoch_nb = 70
    batch = 256

    cbk = MyCbk(model)
    history = LossHistory()

    par_model.fit(x_train, y_train, batch_size=batch, epochs=epoch_nb,
                  verbose=1, validation_data=(x_test, y_test), callbacks=[cbk, history])
    history.loss_plot()

    model.save("../model/tenpai.model")
