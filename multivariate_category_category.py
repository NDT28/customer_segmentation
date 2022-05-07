import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sb
from scipy.stats import chi2_contingency,chi2

def multivariate_category_category(df):
    print("Multivariate Variable Analysis:")
    print("Category vs Category")
    cat = df.select_dtypes(include='category')
    for col in cat.columns:
        for cate in cat.columns:
            if col != cate:
                table = pd.crosstab(cat[col],cat[cate])
                stat,p,dof , expected = chi2_contingency(table)
                prob = 0.95 
                alpha = 1-0.95
                if p <= alpha :
                    print("---------------")
                    print(f"Hai biến {col} và {cate} phụ thuộc, bác bỏ H0 ")
                    print("---------------")
                else:
                    print("---------------")
                    print(f"Hai biến {col} và {cate} độc lập, chấp nhận H0 ")
                    print("---------------")