from keras.models import load_model
import joblib
from sklearn.model_selection import train_test_split

import dataPre
import featureEng


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
        print(self.lb.classes_)
        print("测试集真实标签：", y_test)

    @staticmethod
    def sk_model_perf(model, x_test, y_test):
        print("测试集评估指标结果：")
        results = model.score(x_test, y_test)
        print("accuracy :", results)
        predicts = model.predict(x_test)
        print("测试集预测标签：", predicts)
        print("测试集真实标签：", y_test)

if __name__=="__main__":
    component_data = dataPre.service_data(service_data_path='./data/材料模型_data_test.csv')
    feaEng = featureEng.FeatureEng(component_data, '材料模型')
    svm_x, svm_y = feaEng.service_features()
    svmx_train, svmx_test, svmy_train, svmy_test = train_test_split(svm_x, svm_y, test_size=0.1, random_state=2023)
    infer_demo = Infer(feaEng.lb, tf_model_path='./model/tf_model_test.h5')
    infer_model = infer_demo.load_tf_model()
    infer_demo.tf_model_perf(infer_model, svmx_test, svmy_test)
