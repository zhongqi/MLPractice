# training
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from sklearn.linear_model import LogisticRegression
from keras.models import load_model
import matplotlib.pyplot as plt
import joblib
import dataPre
import featureEng


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
        history = model.fit(x_train, y_train, batch_size=self.bs, epochs=self.epochs, verbose= 2)
        model.save(self.tfmp)
        # 可视化loss和accuracy
        acc = history.history['sparse_categorical_accuracy']
        loss = history.history['loss']

        plt.subplot(1, 2, 1)
        plt.plot(acc, label='Training Accuracy')
        plt.title('Training Accuracy')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(loss, label='Training Loss')
        plt.title('Training Loss')
        plt.legend()
        plt.show()
        return model

    def train_sk_model(self, x_train, y_train):
        model = self.sk_model()
        model.fit(x_train, y_train)
        joblib.dump(model, self.skmp)
        return model

    def validation(self,x_test, y_test):
        model = load_model(self.tfmp)
        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=1)
        print("Test loss:", test_loss)
        print("Test accuracy:", test_acc)

if __name__=="__main__":
    component_data = dataPre.service_data(service_data_path='./data/材料模型_data_test.csv')
    feaEng = featureEng.FeatureEng(component_data, '材料模型')
    svm_x, svm_y = feaEng.service_features()
    svmx_train, svmx_test, svmy_train, svmy_test = train_test_split(svm_x, svm_y, test_size=0.1, random_state=2023)
    train_demo = Train(feaEng.lb, loss_function=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                       metrics='sparse_categorical_accuracy',
                       learning_rate=0.01, batch_size=8, epochs=100, tf_model_path='./model/tf_model_test.h5')
    train_demo.train_tf_model(svmx_train, svmy_train)
    train_demo.validation(svmx_test, svmy_test)
