import keras
import matplotlib.pyplot as plt


class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = {'batch':[], 'epoch':[]}
        self.val_loss = {'batch':[], 'epoch':[]}

    def on_batch_end(self, batch, logs={}):
        self.losses['batch'].append(logs.get('loss'))
        self.val_loss['batch'].append(logs.get('val_loss'))

    def on_epoch_end(self, batch, logs={}):
        self.losses['epoch'].append(logs.get('loss'))
        self.val_loss['epoch'].append(logs.get('val_loss'))

    def loss_plot(self, loss_type='epoch'):
        iters = range(len(self.losses[loss_type]))
        plt.figure()
        plt.plot(iters, self.losses[loss_type], 'r', label='Train')
        if loss_type == 'epoch':
            plt.plot(iters, self.val_loss[loss_type], 'b', label='Val')
        plt.grid(True)
        plt.xlabel(loss_type)
        plt.ylabel('Cross-entropy loss')
        plt.legend(loc="upper right")
        plt.savefig("../train_loss.jpg")
        # plt.show()
