import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import pymysql
df = DataFrame()

movie_db = pymysql.connect(
    user='root', 
    passwd='ssafy', 
    host='127.0.0.1', 
    db='DKM', 
    charset='utf8'
)

cursor = movie_db.cursor(pymysql.cursors.DictCursor)

sql = "select * from movies_movie_cast;"
cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)

sql2 = "select * from movies_genre;"
cursor.execute(sql2)
result2 = cursor.fetchall()
result2 = pd.DataFrame(result2)

sql3 = "select * from movies_overview_tag;"
cursor.execute(sql3)
result3 = cursor.fetchall()
result3 = pd.DataFrame(result3)

# print(result)
# print(result2)
# print(result3)
A = result.loc[:, ['movie_actors']]
B = result2.loc[:, ['name']]
C = result3.loc[:, ['tags']]
# print(A)
# print(B)
A.columns = ['name']
C.columns = ['name']
print(A)
D = pd.concat([A, B, C])
print(D)
F = D.T
print(F)