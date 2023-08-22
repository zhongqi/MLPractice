# data preparation
# 1. get data from web and cache locally
# 2. provide a data service interface
import pandas as pd
# from param import raw_data_path, target_component, service_data_path


# get data from web and cache locally
def get_data(raw_data_path, service_data_path, component):
    raw_data = pd.read_excel(raw_data_path, skiprows=2).drop([0], axis=0).rename(columns={'Unnamed: 0': "算例名称"})
    component_data = specify_algorithm(raw_data, component)
    component_data.to_csv(service_data_path, index_label=False)
    return raw_data


def specify_algorithm(raw_data, component, num_of_components=3):
    # 选定一种功能组件类作为标签生成数据
    tar_component = raw_data[[component]]  # 选定该算法对应的列
    feature_column = raw_data.iloc[:, :-num_of_components]
    component_data = feature_column.join(tar_component)  # 与特征列合并
    return component_data


# provide a data service interface
def service_data(service_data_path):
    result = pd.read_csv(service_data_path)
    return result


if __name__=="__main__":
    raw_data = get_data(raw_data_path='./data/样本_demo.xlsx', service_data_path='./data/材料模型_data_test.csv', component='材料模型')
    print(service_data(service_data_path='./data/材料模型_data_test.csv'))