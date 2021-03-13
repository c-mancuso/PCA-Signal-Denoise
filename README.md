# PCA-Signal-Denoise
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
	
