import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sb

def single_variable_continuous(df):
    print("Single Variable Analysis:")
    print("Continuous Variable")
    num = df.select_dtypes(exclude='category')
    for col in num.columns:
        print(col)
        print('-----------------')
        print(f"Range of {col} is ",np.ptp(num[col]))
        print(f"Skewness of {col} is",num[col].skew())
        plt.boxplot(num[col])
        plt.show()
        sb.kdeplot(num[col])
        plt.show()
        print("-----------------")
        