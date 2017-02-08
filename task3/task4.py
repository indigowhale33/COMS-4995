from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def scatter_matrix(data):
	"""
	Plot the iris dataset in scatterplot matrix

	Parameters
	----------
	- **Parameters**::
		data : object
			iris dataset object

	Returns
	-------
	- **Returns**::
		fig : matplotlib figure
		
	"""

	seto = data['data'][data['target']==0]
	versi = data['data'][data['target']==1]
	virgin = data['data'][data['target']==2]

	fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(12,12))


	for i in range(4):
		for j in range(4):
			if i !=j :
				ax[j,i].plot(seto[:,j], seto[:,i], color='red', marker='o', linestyle='none')
				ax[j,i].plot(versi[:,j], versi[:,i], color='green', marker='o',linestyle='none')
				ax[j,i].plot(virgin[:,j], virgin[:,i], color='purple', marker='o', linestyle='none')

	for i in range(4):
		ax[i,i].hist(seto[:,i])
		ax[i,i].hist(versi[:,i])
		ax[i,i].hist(virgin[:,i])

	ax[0,0].set_title('Sepal length')
	ax[1,1].set_title('Sepal width')
	ax[2,2].set_title('Petal length')
	ax[3,3].set_title('Petal width')


	fig.subplots_adjust(hspace=0.3)
	fig.set_size_inches(18.5, 10.5, forward=True)
	plt.legend(loc = 'upper left', bbox_to_anchor = (1.0, 5),labels = data.target_names)

	return fig


def main():
	iris_dataset = load_iris()
	fig = scatter_matrix(iris_dataset)
	plt.show()

if __name__ == '__main__':
	main()
