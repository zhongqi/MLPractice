from keras.models import load_model
from sklearn.externals import joblib


class Infer:

    def __init__(self, lb, tf_model_path=None, sk_model_path=None):
        self.lb = lb
        self.tfmp = tf_model_path
        self.skmp = sk_model_path

    def load_tf_model(self):
        model = load_model(self.tfmp)
        return model

    def load_sk_model(self):
        model = joblib.load(self.skmp)
        return model

    def tf_model_perf(self, model, x_test, y_test):
        print("测试集评估指标结果：")
        results = model.evaluate(x_test, y_test, verbose=0)
        print("loss, accuracy :", results)
        predicts = model.predict(x_test, verbose=0)
        print("测试集预测标签：", self.lb.inverse_transform(predicts))
        print("测试集真实标签：", self.lb.inverse_transform(y_test))

    @staticmethod
    def sk_model_perf(model, x_test, y_test):
        print("测试集评估指标结果：")
        results = model.score(x_test, y_test)
        print("accuracy :", results)
        predicts = model.predict(x_test)
        print("测试集预测标签：", predicts)
        print("测试集真实标签：", y_test)
