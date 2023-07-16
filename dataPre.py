# data preparation
# 1. get data from web and cache locally
# 2. provide a data service interface
from sklearn.preprocessing import MultiLabelBinarizer, OrdinalEncoder
from param import datapath,num_of_component,target_component
import pandas as pd
import json


# get data from web and cache locally
def get_data(compCode):
    raw_data = pd.read_excel(datapath, skiprows=2).drop([0], axis=0).rename(columns={'Unnamed: 0': "算例名称"})
    return raw_data


def multi_hot_encoder(samples, featurename):
    # 自定义函数利用MultiBinarizer实现MultiHot编码
    lab_split = samples[featurename].str.split(',')  # 将数据按‘,’拆分
    mlb = MultiLabelBinarizer()  # 多标签编码
    lb_results = mlb.fit_transform(lab_split)
    labclass = mlb.classes_  # 标签类别
    labcol = [featurename] * lb_results.shape[1]  # 生成对应的列名称
    for i in range(len(labclass)):
        labcol[i] = '{}_{}'.format(labcol[i], labclass[i])
    df = pd.DataFrame(lb_results, columns=labcol)
    return df


def multi_hot_one_label(samples):
    # samples:原始数据; targetname:功能组件类别,单标签/多标签特征集合
    # "算例名称"用序号编码
    name = OrdinalEncoder(dtype=int).fit_transform(samples[['算例名称']])
    namedf = pd.DataFrame(name, columns=['算例名称'])

    # 所有特征用Multi-Hot编码
    mulhot = pd.DataFrame()
    for i in samples.iloc[:, 1:-num_of_component].columns:  # 算例名称和组件列以外的特征列
        mlf = multi_hot_encoder(samples, i)
        mulhot = mulhot.join(mlf, how='right')

    # 目标算法
    target = samples[target_component].reset_index(drop=True) \
        .str.split(',', expand=True).stack().reset_index(drop=True, level=1).rename(target_component)  # 将多标签分割变成多行

    # 将所有特征编码拼接
    dataset = namedf.join(mulhot).join(target).reset_index(drop=True)
    return dataset


# provide a data service interface
def service_data(compCode):
    result = {}
    result[compCode] = []
    return json.dumps(result)


