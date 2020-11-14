import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import pymysql
from konlpy.tag import Kkma
import json

def recommend_sys(searchword):
    kkma = Kkma()
    df = DataFrame()
    movie_db = pymysql.connect(
        user='root', 
        passwd='ssafy', 
        host='127.0.0.1', 
        db='DKM', 
        charset='utf8'
    )

    cursor = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = "select * from movies_tagdatas;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)

    sql2 = "select * from mls;"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    result2 = pd.DataFrame(result2)

    sql3 = "select * from movies_movie_tagdatas;"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    result3 = pd.DataFrame(result3)
    result3['weight'] = 1
    D = []
    words= kkma.nouns(searchword)
    for w in words:
        words_s = result[result['tags'] == w]['id']
        D.extend(words_s.values)
    if len(D) == 0:
        return []
    else:
        ml = list(result2['0'].values)
        mov_l, score_l = list(), list()
        for mnum in ml:
            score = 0
            tgd = list(result3[result3['movie_id'] == mnum]['tagdatas_id'].values)
            for dn in D:
                if dn in tgd:
                    score += 1
            
            mov_l.append(mnum)
            score_l.append(score)
        
        data_df1 = pd.DataFrame({'movie_id': mov_l, 'score': score_l})
        df1 = data_df1.sort_values(by=['score'], ascending=False)
        df1 = df1[1:21]
        df2 = list(df1['movie_id'].values)
        return df2


        # data_df1 = result3.pivot_table(index='movie_id', columns='tagdatas_id', values='weight')
        # data_df1.fillna(0, inplace=True)
        # # print(data_df1)
        # m1 = Series(data_df1.loc[1])

        # # print(m1)
        # data_df2 = data_df1.mul(m1, axis=1)
        # data_df2 = data_df2.sum(axis = 1)
        # data_df2 = data_df2.sort_values(ascending=False)
        # df3 = data_df2[1:21]
        # df4 = [i for i in df3.index]
        # return


def recommend_sys2(user_pk):
    user_pk = 1
    df = DataFrame()
    movie_db = pymysql.connect(
        user='root', 
        passwd='ssafy', 
        host='127.0.0.1', 
        db='DKM', 
        charset='utf8'
    )

    cursor = movie_db.cursor(pymysql.cursors.DictCursor)

    sql = f"select * from movies_user_tagdatas where user_id={user_pk};"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)

    sql3 = "select * from movies_movie_tagdatas;"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    result3 = pd.DataFrame(result3)
    result3['weight'] = 1


    if len(result) == 0:
        pass
        # return []
    else:
        result = result[['tagdata_id', 'weight']]
        result['movie_id'] = 1
        result.rename(columns={'tagdata_id':'tagdatas_id'}, inplace=True)
        result3 = pd.concat([result, result3], ignore_index=True)
        data_df1 = result3.pivot_table(index='movie_id', columns='tagdatas_id', values='weight')
        data_df1.fillna(0, inplace=True)
        data_df1 = data_df1.sort_values(by='movie_id', ascending=True)
        m1 = Series(data_df1.loc[1])

        data_df2 = data_df1.mul(m1, axis=1)
        data_df2 = data_df2.sum(axis = 1)
        data_df2 = data_df2.sort_values(ascending=False)
        df3 = data_df2[1:21]
        df4 = [i for i in df3.index]
        return df4
