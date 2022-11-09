# feature engineering
from dataPre import service_data
from param import loc_db

class featureEng:
    def __init__():
        self.loc_database = loc_db
        self.data = self._get_data()
        self.num_features = 1000 #predefined, fill 0 by default
        self.features = [] # e.g. [{'SH600001':100,'SH600002':3},{'SH600001':0.4},{},{},{}]

    # load data in memory
    def _get_data():
        # result = service_data(xxxx)
        # return result

    # feature engineering method 1
    def _feature_eng1():
        feature = {}
        return feature

    # feature engineering method 2
    def _feature_eng2():
        feature = {}
        return feature

    def feature_eng_all():
        f1 = self._feature_eng1() #{'SH600001':100,'SH600002':3}
        self.features.append(f1)

        f2 = self._feature_eng2()
        self.features.append(f2)

    # done.
    def service_features(id):
        result = []
        cnt = 0
        for i in range(len(self.features)):
            result.append(self.features[i][id])
            cnt += 1
        for i in range(cnt, self.num_features):
            result.append(0)
        return result

    
if __name__=='__main__':
    print("testing featureEng.py")
    fe = featureEng()
    fe.feature_eng_all()
    
