import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris_dataset=load_iris()

data = iris_dataset
setosa=data['data'][data['target']==0]
versicolor=data['data'][data['target']==1]
virginica=data['data'][data['target']==2]

def main():


    fig = scatterplot_matrix(data, ['sep len', 'sep wid', 'pet len', 'pet wid'])
    fig.suptitle('Pair-plot matrix of Iris Dataset, measurements in cm')
    plt.show()

def scatterplot_matrix(data, names, **kwargs):
    """Plots a scatterplot matrix of subplots.  Each row of "data" is plotted
    against other rows, resulting in a nrows by nrows grid of subplots with the
    diagonal subplots labeled with "names".  Additional keyword arguments are
    passed on to matplotlib's "plot" command. Returns the matplotlib figure
    object containg the subplot grid."""
    numvars = 4
    fig, axes = plt.subplots(nrows=numvars, ncols=numvars, figsize=(12,12))
    fig.subplots_adjust(hspace=0.25, wspace=0.25)

    for ax in axes.flat:
        # Hide all ticks and labels
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        # Set up ticks only on one side for the "edge" subplots...
        if ax.is_first_col():
            ax.yaxis.set_ticks_position('left')
        if ax.is_last_col():
            ax.yaxis.set_ticks_position('right')
        if ax.is_first_row():
            ax.xaxis.set_ticks_position('bottom')
        if ax.is_last_row():
            ax.xaxis.set_ticks_position('bottom')

    for i in range(0,4):
        for j in range(0,4):
            if i==j:
                continue
            axes[j,i].plot(setosa[:,j], setosa[:,i], color='blue',marker='o',linestyle='none')
            axes[j,i].plot(versicolor[:,j], versicolor[:,i], color='red',marker='o',linestyle='none')
            axes[j,i].plot(virginica[:,j], virginica[:,i], color='green',marker='o',linestyle='none')    

    for i in range(0,4):
        axes[i,i].hist(setosa[:,i])
        axes[i,i].hist(versicolor[:,i])
        axes[i,i].hist(virginica[:,i])
    
    axes[0,0].set_title('Sepal length')
    axes[1,1].set_title('Sepal width')
    axes[2,2].set_title('Petal length')
    axes[3,3].set_title('Petal width')
    # Turn on the proper x or y axes ticks.
    #for i, j in zip(range(numvars), itertools.cycle((-1, 0))):
    for i in range(0,4):
        for j in range(0,4):
            axes[j,i].xaxis.set_visible(True)
            axes[i,j].yaxis.set_visible(True)

    plt.legend(('Setosa','Virginica','Versicolor'))
    
    return fig

main()
