import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
plt.figure(figsize=(6,4))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Sepal Length')
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['sepal length (cm)'])
plt.title('Boxplot of Sepal Length')
plt.show()

species_counts = df['species'].value_counts()
plt.figure(figsize=(6,4))
plt.pie(species_counts, labels=iris.target_names, autopct='%1.1f%%')
plt.title('Species Distribution (Pie Chart)')
plt.show()


plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'], hue=df['species'])
plt.title("Scatterplot: Sepal Length vs Sepal Width")
plt.show()

plt.figure(figsize=(6,4))
plt.plot(df['sepal length (cm)'])
plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=df['species'], y=df['sepal length (cm)'])
plt.title("Bar Chart: Mean Sepal Length by Species")
plt.xticks([0, 1, 2], iris.target_names)
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df.iloc[:, :4].corr(), annot=True, cmap='coolwarm')
plt.title("Heatmap of Feature Correlations")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], s=df['petal length (cm)']*20, alpha=0.5,c=df['species'])
plt.title("Bubble Chart: Sepal vs Petal (Size = Petal width)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal width (cm)")
plt.show()
sns.pairplot(df.iloc[:, :4])
plt.suptitle("Pairplot of Iris Features", y=1.02)
plt.show()


plt.figure(figsize=(6,4))
sns.violinplot(x=df['species'], y=df['sepal length (cm)'])
plt.title("Violin Plot: Sepal Length by Species")
plt.xticks([0, 1, 2], iris.target_names)
plt.show()


import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")

print(df.head())

plt.figure(figsize=(6, 4))
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.figure(figsize=(6, 4))
sns.boxplot(x=df["total_bill"])
plt.title("Boxplot of Total Bill")
plt.xlabel("Total Bill")

day_counts = df["day"].value_counts()

plt.figure(figsize=(6, 4))
plt.pie(day_counts, labels=day_counts.index, autopct="%1.1f%%")
plt.title("Day Distribution")

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day")
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.figure(figsize=(6, 4))
plt.plot(df["total_bill"])
plt.title("Line Chart of Total Bill")
plt.xlabel("Sample Index")
plt.ylabel("Total Bill")

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="day", y="total_bill")
plt.title("Mean Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Mean Total Bill")

plt.figure(figsize=(8, 6))
correlation = df[["total_bill", "tip", "size"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.figure(figsize=(6, 4))
plt.scatter(
    df["total_bill"],
    df["tip"],
    s=df["size"] * 20,
    alpha=0.5,
    c=df["size"]
)
plt.title("Bubble Chart: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

sns.pairplot(df[["total_bill", "tip", "size"]])
plt.suptitle("Pairplot of Tips Dataset", y=1.02)

plt.figure(figsize=(6, 4))
sns.violinplot(data=df, x="day", y="total_bill")
plt.title("Violin Plot: Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")

plt.show()