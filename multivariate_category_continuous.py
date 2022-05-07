import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sb
import statsmodels.api as sm 
from statsmodels.formula.api import ols

def multivariate_category_continuous(df,output):
    print("Multivariate Variable Analysis:")
    print("Continuous vs Category")
    
    cat = df.select_dtypes(include='category')
    num = df.select_dtypes(exclude='category')
    
    if df[output].dtypes.name == 'category':
        for nume in num.columns:
            model_cat = ols(f'{nume} ~ C({output})',data=df).fit()
            anova_table_cat = sm.stats.anova_lm(model_cat,typ = 2)
            print(f"{nume} vs {output}")
            print(anova_table_cat)
            print("------------------------------")
    if df[output].dtypes.name != 'category':
        for cate in cat.columns:
            model_num = ols(f'{output} ~ C({cate})',data=df).fit()
            anova_table_num = sm.stats.anova_lm(model_num,typ = 2)
            print(f"{cate} vs {output}")
            print(anova_table_num)
            print("------------------------------")
    
    