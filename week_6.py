import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
mean_values = df.mean()
print("\nMean values:")
print(mean_values)
median_values = df.median()
print("\nMedian values:")
print(median_values)
mode_values = df.mode().iloc[0]
print("\nMode values:")
print(mode_values)


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
range_values = df.max() - df.min()
print("\nRange values:")
print(range_values)
variance_values = df.var()
print("\nVariance values:")
print(variance_values)
std_values = df.std()
print("\nStandard Deviation values:")
print(std_values)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("\nInterquartile Range (IQR):")
print(IQR)


import scipy as s
from scipy.stats import kurtosis
data=[10,25,14,26,35,45,67,90,40,50,60,10,16,18,20]
s.stats.skew(data,axis=0, bias=True)
kurtosis(data, axis=0, bias=True)


import scipy as s
from scipy.stats import skew, kurtosis
import numpy as np
import pandas as pd
df=pd.read_csv("temporal.csv")
kurtosis(df['data science'], axis=0, bias=True)


import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
skewness_values = df.skew()
print("\nSkewness values:")
print(skewness_values)
kurtosis_values = df.kurtosis()
print("\nKurtosis values:")
print(kurtosis_values)


import pandas as pd
from sklearn.datasets import load_tips
from statistics import mode
tips = load_tips()
df = pd.DataFrame(tips.data, columns=tips.feature_names)
print("First 5 rows of dataset:")
print(df.head())
mean_values = df.mean()
print("\nMean values:")
print(mean_values)
median_values = df.median()
print("\nMedian values:")
print(median_values)
mode_values = df.mode().iloc[0]
print("\nMode values:")
print(mode_values)
range_values = df.max() - df.min()
print("\nRange values:")
print(range_values)
variance_values = df.var()
print("\nVariance values:")
print(variance_values)
std_values = df.std()
print("\nStandard Deviation values:")
print(std_values)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("\nInterquartile Range (IQR):")
print(IQR)
skewness_values = df.skew()
print("\nSkewness values:")
print(skewness_values)
kurtosis_values = df.kurtosis()
print("\nKurtosis values:")
print(kurtosis_values)