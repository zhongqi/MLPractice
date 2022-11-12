# feature engineering
import json

import pandas as pd

from dataPre import service_data
from param import loc_db
from param import tushare_token
import sqlite3


class featureEng:
    def __init__(self, loc_db, tushare_token):
        self.loc_database = loc_db
        self.data = self._get_data(tushare_token)
        self.num_features = 1000  # predefined, fill 0 by default
        self.features = []  # e.g. [{'SH600001':100,'SH600002':3},{'SH600001':0.4},{},{},{}]

    # load data in memory
    def _get_data(self, token):
        result = service_data(token)
        return result

    # feature engineering method 1
    def _feature_eng1(self):
        feature = {}

        dict_f1 = json.loads(self)
        for i in range(len(dict_f1)):
            feature.setdefault("trade_date", []).append(dict_f1[str(i)]["trade_date"])

        return feature

    # feature engineering method 2
    def _feature_eng2(self):
        feature = {}

        dict_f2 = json.loads(self.data)
        for i in range(len(dict_f2)):
            feature.setdefault("open", []).append(dict_f2[str(i)]["open"])

        return feature

    # feature engineering method 3
    def _feature_eng3(self):
        feature = {}

        dict_f3 = json.loads(self.data)
        for i in range(len(dict_f3)):
            feature.setdefault("high", []).append(dict_f3[str(i)]["high"])

        return feature

    # feature engineering method 4
    def _feature_eng4(self):
        feature = {}

        dict_f4 = json.loads(self.data)
        for i in range(len(dict_f4)):
            feature.setdefault("low", []).append(dict_f4[str(i)]["low"])

        return feature
    # feature engineering method 5
    def _feature_eng5(self):
        feature = {}

        dict_f5 = json.loads(self.data)
        for i in range(len(dict_f5)):
            feature.setdefault("close", []).append(dict_f5[str(i)]["close"])

        return feature

    # feature engineering method 6
    def _feature_eng6(self):
        feature = {}

        dict_f6 = json.loads(self.data)
        for i in range(len(dict_f6)):
            feature.setdefault("pre_close", []).append(dict_f6[str(i)]["pre_close"])

        return feature

    # feature engineering method 7
    def _feature_eng7(self):
        feature = {}

        dict_f7 = json.loads(self.data)
        for i in range(len(dict_f7)):
            feature.setdefault("change", []).append(dict_f7[str(i)]["change"])

        return feature

    # feature engineering method 8
    def _feature_eng8(self):
        feature = {}

        dict_f8 = json.loads(self.data)
        for i in range(len(dict_f8)):
            feature.setdefault("pct_chg", []).append(dict_f8[str(i)]["pct_chg"])

        return feature

    # feature engineering method 9
    def _feature_eng9(self):
        feature = {}

        dict_f9 = json.loads(self.data)
        for i in range(len(dict_f9)):
            feature.setdefault("vol", []).append(dict_f9[str(i)]["vol"])

        return feature

    # feature engineering method 10
    def _feature_eng10(self):
        feature = {}

        dict_f10 = json.loads(self.data)
        for i in range(len(dict_f10)):
            feature.setdefault("amount", []).append(dict_f10[str(i)]["amount"])

        return feature

    # feature engineering method 11
    def _feature_eng11(self):
        feature = {}

        dict_f11 = json.loads(self.data)
        for i in range(len(dict_f11)):
            feature.setdefault("daily_diff_open_close", []).append(list(pd.Series(dict_f11[str(i)]["`open`"])-pd.Series(dict_f11[str(i)]["close"])))

        return feature

    # feature engineering method 12
    def _feature_eng12(self):
        feature = {}

        dict_f12 = json.loads(self.data)
        for i in range(len(dict_f12)):
            feature.setdefault("turn_over_rate_%", []).append(list(pd.Series(dict_f12[str(i)]["vol"])*100/pd.Series(len(dict_f12[str(i)]["trade_date"]))))

        return feature



    def feature_eng_all(self):
        f1 = self._feature_eng1()  # {'SH600001':100,'SH600002':3}
        self.features.append(f1)

        f2 = self._feature_eng2()
        self.features.append(f2)

        f3 = self._feature_eng3()  # {'SH600001':100,'SH600002':3}
        self.features.append(f3)

        f4 = self._feature_eng4()
        self.features.append(f4)

        f5 = self._feature_eng5()  # {'SH600001':100,'SH600002':3}
        self.features.append(f5)

        f6 = self._feature_eng6()
        self.features.append(f6)

        f7 = self._feature_eng7()  # {'SH600001':100,'SH600002':3}
        self.features.append(f7)

        f8 = self._feature_eng8()
        self.features.append(f8)

        f9 = self._feature_eng9()  # {'SH600001':100,'SH600002':3}
        self.features.append(f9)

        f10 = self._feature_eng10()
        self.features.append(f10)

        f11 = self._feature_eng11()  # {'SH600001':100,'SH600002':3}
        self.features.append(f11)

        f12 = self._feature_eng12()
        self.features.append(f12)

    # done.
    def service_features(self, id):
        result = []
        cnt = 0
        for i in range(len(self.features)):
            result.append(self.features[i][id])
            cnt += 1
        for i in range(cnt, self.num_features):
            result.append(0)
        return result


if __name__ == '__main__':
    print("testing featureEng.py")
    fe = featureEng()
    fe.feature_eng_all()
