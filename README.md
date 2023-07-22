# MLPractice
A ML pipeline.

## Code Conventions
### Name
1. "service_$x" functions provide $x service;
2. "get_$x" functions collect $x from sources;

## dataPre.py
Data preparation. There are two basic functions: 
1. get data from web and cache locally;
2. provide a data service interface.

Some preprocessing function:
1. specify one specific component in the data

## featureEng.py
Feature engineering. 
1. multi_hot_encoder(data,featurename): 
   1. turn the 'featurename' column of the data into multi-hot
2. multi_hot_one_label():
   1. turn all the feature into multi_hot, 
   2. split multi-label into one label with multi raws,
   3. save to the 'encoder_csvdata_path'.
3. csv_to_libsvm():
   1. read from 'encoder_csvdata_path'
   2. encoder y label with LabelBinarizer(lb)
   3. change csv_data into libsvm_data and save
4. x_y_split():
   1. split x_data and y_data in libsvm form.

## train.py
Train model
1. tf/sk_model(): define a model through Tensorflow/sklearn
2. train_tf/sk_model(): 
   1. train a model with train data
   2. save the trained model

## infer.py
Evaluate model
1. load_tf/sk_model(): load_model
2. tf/sk_model_perf(): evaluate model performance
3. 
## pipeline.py
Use pipeline.py to execute feature-training-inference pipeline
