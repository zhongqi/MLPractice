# data preparation
# 1. get data from web and cache locally
# 2. provide a data service interface

from param import tushare_token, loc_db
import json
import sqlite3
import pandas as pd
import time
import csv


# get data from web and cache locally
def get_data(compCode):
    import tushare
    tushare.set_token(tushare_token)

    conn = sqlite3.connect(loc_db)  # Lixiang's db location: 'D:/PyProjects/TimeSeriesAnaPrj_database/CHN_stock_data.db'

    c = conn.cursor()

    pro = tushare.pro_api()
    t = time.strftime('%Y%m%d', time.localtime())
    # df = pro.daily(trade_date=t)  # 获取所有上市公司当前日期的全部历史
    df = pro.query('daily', ts_code=compCode, trade_date=t)  # 获取制定公司当前日期的所有历史
    sql = """
            create table if not exists AShareDaily(ts_code,trade_date,`open`,high,low,`close`,pre_close,change,pct_chg,vol,amount);
        """
    c.execute(sql)
    df.to_sql('AShareDaily', conn, if_exists='append', index=False)
    conn.commit()

    c.close()
    conn.close()


# provide a data service interface
def service_data(compCode):
    result = {}
    result[compCode] = []
    return json.dumps(result)
