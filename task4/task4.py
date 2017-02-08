from sklearn.datasets import load_iris
import pandas as pd
from pandas.tools.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
colors = ['red','green','purple']
red = mpatches.Patch(color='red', label='setosa')
blue = mpatches.Patch(color='green', label= 'versicolor')
purple = mpatches.Patch(color='purple', label=  'virginica')

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

grr = scatter_matrix(iris_dataframe, alpha=0.8,c=colors, figsize=(15, 15), marker='o',
                        hist_kwds={'bins': 20}, s=60)


print(list(iris_dataset.target_names))
handles, labels = grr[0][1].get_legend_handles_labels()
grr[0][3].legend(loc = 'center left', bbox_to_anchor = (1.0, 0.7),handles=[red, blue,purple],labels=list(iris_dataset.target_names))
plt.show()