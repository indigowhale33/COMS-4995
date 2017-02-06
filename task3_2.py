from __future__ import print_function, division
import numpy as np

def MSD(nparr, ax=0):
	""" 
	Calculate mean and standard deviation of numpy array by axis

	Parameters
	----------
	nparr : array_like
			Array containing numbers
	ax : int, optional (default=0)
		Axis along which means and standard deviations are computed.

	Returns
	-------
	m,std : tuple
		tuple of mean and standard deviation of the input array in terms of the axis.

	Raises
	------
	ValueError
		if the given axis is not None or not 0 or 1.
	"""
	if(ax != None):
		try:
			val = int(ax)
		except ValueError:
			print("axis should be integer")

	if( ax < 0 || ax > 1):
		raise ValueError("axis should be between 0 to 1")

	return np.mean(nparr,axis=ax), np.std(nparr,axis=ax)

a = MSD(np.array([[1,2],[3,4]]))
print(a)
print(MSD(np.array([[1,2],[3,4]]),1))
print(MSD(np.array([[1,2],[3,4]]),None))
print(MSD(np.array([1,2,3,4])))