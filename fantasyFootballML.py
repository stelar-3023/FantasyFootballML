import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.set_option("display.max_columns", None)
df = pd.read_csv(r"E:\\FantasyFootballML\\fantasyFootballLeaders.csv")

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

#print(X)
#print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit (X[:, 8:21])
X[:, 8:21] = imputer.transform(X[:, 8:21])

print(X)


print(df["Season"].min(), df["Season"].max())
print(df.head())