import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


train_df = pd.read_csv('./train.csv')
test_df = pd.read_csv('./test.csv')
combine = [train_df, test_df]

train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)
g = sns.FacetGrid(train_df, col="Survived")
g.map(plt.hist, 'Age',  bins=20)

plt.show()