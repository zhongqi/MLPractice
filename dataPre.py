# data preparation
# 1. get data from web and cache locally
# 2. provide a data service interface

from param import tushare_token, loc_db
import json
import sqlite3

# get data from web and cache locally
def get_data(compCode):
    import tushare
    tushare.set_token(tushare_token)

    conn = sqlite3.connect(loc_db)
    c = conn.cursor()
    

# provide a data service interface
def service_data(comCode):
    result = {}
    result[compCode] = []
    return json.dumps(result)



