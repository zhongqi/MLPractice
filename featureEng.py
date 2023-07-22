# feature engineering
from sklearn.preprocessing import MultiLabelBinarizer, OrdinalEncoder, LabelBinarizer
from sklearn.datasets import load_svmlight_file, dump_svmlight_file
from sklearn.model_selection import train_test_split
import pandas as pd


class FeatureEng:
    def __init__(self, component_data, component):
        # component_data:待编码数据; component:功能组件类别
        self.data = component_data
        self.component = component

    @staticmethod
    def multi_hot_encoder(data, featurename):
        # 自定义函数利用MultiBinarizer实现MultiHot编码
        lab_split = data[featurename].str.split(',')  # 将数据按‘,’拆分
        mlb = MultiLabelBinarizer()  # 多标签编码
        lb_results = mlb.fit_transform(lab_split)
        labclass = mlb.classes_  # 标签类别
        labcol = [featurename] * lb_results.shape[1]  # 生成对应的列名称
        for i in range(len(labclass)):
            labcol[i] = '{}_{}'.format(labcol[i], labclass[i])
        df = pd.DataFrame(lb_results, columns=labcol)
        return df

    def multi_hot_one_label(self, csv_data_path):
        # "算例名称"用序号编码
        name = OrdinalEncoder(dtype=int).fit_transform(self.data[['算例名称']])
        namedf = pd.DataFrame(name, columns=['算例名称'])

        # 所有特征用Multi-Hot编码
        mul_hot = pd.DataFrame()
        for i in self.data.iloc[:, 1:-1].columns:  # 算例名称和功能组件列以外的特征列
            mlf = self.multi_hot_encoder(self.data, i)
            mul_hot = mul_hot.join(mlf, how='right')

        # 目标算法
        target = self.data[self.component].reset_index(drop=True) \
            .str.split(',', expand=True).stack().reset_index(drop=True, level=1).rename(self.component)  # 将多标签分割变成多行

        # 将所有特征编码拼接
        dataset = namedf.join(mul_hot).join(target).reset_index(drop=True)
        dataset.to_csv(csv_data_path, index=False)
        return dataset

    @staticmethod
    def csv_to_libsvm(csv_data, libsvm_data_path):
        lb = LabelBinarizer()
        y = lb.fit_transform(csv_data.iloc[:, -1])
        X = csv_data.iloc[:, :-1]
        dump_svmlight_file(X, y, libsvm_data_path, multilabel=True)
        libsvm_data = load_svmlight_file(libsvm_data_path)
        return libsvm_data, lb

    @staticmethod
    def x_y_split(libsvm_data):
        svm_x = libsvm_data[0]
        svm_y = libsvm_data[1]
        return svm_x, svm_y

    def service_features():
        pass
