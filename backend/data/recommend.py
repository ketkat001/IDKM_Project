import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import sqlite3

def recommend_s(user_pk):
    conn = 