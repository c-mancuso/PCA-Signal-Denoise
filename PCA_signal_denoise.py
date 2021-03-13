"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Simple PCA denoising of 1D array (for example time series signal)
Written in Python 3.8.5
By Chris Mancuso
Updated March 13 2021
IN:
	signal:		1D signal of size M (comma separated file)
					-see fname
	n_elements: number of principal components to keep (integer < M/2)
OUT:
	signal		1D de-noised signal of size M (comma separated file)
					-fname+denoised
	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import numpy as np
from scipy.linalg import svd
from scipy.linalg import hankel

n_elements = 5
fname='example_wave.csv'

#open file
myFile = np.genfromtxt(fname, delimiter=',')

#define matrix
A = np.array(myFile)

nt=len(myFile)

#get hankel matrix and trim
B = hankel(A)
C = B[0:int(nt/2)]
D = C[:,0:int(nt/2)]

#SVD
U, s, VT = svd(D)

# create m x n Sigma matrix
Sigma = np.zeros((D.shape[0], D.shape[1]))

# populate Sigma with n x n diagonal matrix
Sigma[:D.shape[0], :D.shape[0]] = np.diag(s)

# select
Sigma = Sigma[:, :n_elements]
VT = VT[:n_elements, :]

# reconstruct
Q = U.dot(Sigma.dot(VT))

aa = Q[:,0]
bb = Q[:,499]

AA = np.concatenate([ aa, bb])

f, axarr = plt.subplots(2, sharex=True)
axarr[0].set_title('Original Signal')
axarr[0].plot(A)
axarr[1].set_title('De-Noised Signal')
axarr[1].plot(AA)
axarr[1].set_xlabel('Time')

np.savetxt(fname+'_denoised',AA, delimiter=',')
plt.show()

