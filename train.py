# training
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Dense
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


class Train:
    def __init__(self, lb, loss_function, metrics, learning_rate,
                 batch_size, epochs, tf_model_path=None, sk_model_path=None):
        self.lb = lb
        self.lf = loss_function
        self.mt = metrics
        self.lr = learning_rate
        self.bs = batch_size
        self.epochs = epochs
        self.tfmp = tf_model_path
        self.skmp = sk_model_path

    def tf_model(self):
        model = tf.keras.Sequential([
            Dense(len(self.lb.classes_), activation='softmax', name='output')
        ])
        model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=self.lr),
            loss=self.lf,
            metrics=[self.mt])

        return model

    # sklearn中的分类器
    @staticmethod
    def sk_model():
        model = LogisticRegression(multi_class='ovr')
        return model

    def train_tf_model(self, x_train, y_train):
        model = self.tf_model()
        model.fit(x_train, y_train, batch_size=self.bz, epochs=self.epochs)
        model.save(self.tfmp)
        return model

    def train_sk_model(self, x_train, y_train):
        model = self.sk_model()
        model.fit(x_train, y_train)
        joblib.dump(model, self.skmp)
        return model

    def validation():
        pass
