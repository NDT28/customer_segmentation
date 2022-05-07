import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sb

def single_variable_category(df):
    print("Single Variable Analysis :")
    print("Category Variable")
    cat = df.select_dtypes(include='category')
    for col in cat.columns:
        print(col)
        print('-----------------')
        count = cat[col].value_counts()
        print(count)
        count.plot(kind = 'bar',color = 'skyblue')
        plt.show()
        print("-----------------")
        