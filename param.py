# dataPre.py
raw_data_path = './data/样本.xlsx'
target_component = "材料模型"
service_data_path = './data/{}_data.csv'.format(target_component)
num_of_component = 3  # 样本数据中功能组件的类别数量,目前只有三种，”单元算法“，”材料模型“，”求解流程“

# featureEng.py
csv_data_path = ''
libsvm_data_path = ''

# train.py
loss_function = 'categorical_crossentropy'
metrics = 'sparse_categorical_accuracy'
learning_rate = 0.1
batch_size = 32
epochs = 100
tf_model_path = ''
sk_model_path = ''
