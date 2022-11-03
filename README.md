# TimeSeriesAnalysisMLPractice
A ML pipeline to apply time series analysis.

## Code Conventions
### Name
1. "service_$x" functions provide $x service;
2. "get_$x" functions collect $x from sources;

## dataPre.py
Data preparation. There are two basic functions: 
1. get data from web and cache locally;
2. provide a data service interface.


## pipeline
Use pipeline.py to execute feature-training-inference pipeline
A typical ML pipeline includes:
1. data preparation (dataPre.py)
2. feature engineering (featureEng.py)
3. train a ML model (train.py)
4. make predictions (infer.py)
In addition, put global parameters in param.py