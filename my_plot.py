#   make a plot along 3 columns in a fits file
#

import numpy as np
import matplotlib.pyplot as pyplot
import os
from astropy.io import fits
import glob

fitsfile = 'https://github.com/teuben/AAS241/raw/main/M100.mom0.fits'
data = fits.getdata(fitsfile)

def plot_column(col_number,data):
    """ plot a column from a 2d matrix
    """
    (nx,ny) = data.shape
    col =data[col_number, :]
    pyplot.figure()
    pyplot.plot(np.arange(nx), col)
    mean = np.mean(col)
    pyplot.axhline(mean)
    pyplot.legend([f'Column {col_number}', 'Mean'])
    pyplot.title(f'Plot of Column {col_number} Values and Mean')
    pyplot.xlabel('Pixels')
    pyplot.ylabel('Intensity')

print(f"3 columns in {fitsfile}")

plot_column(20,data)
plot_column(33,data)
plot_column(50,data)

pyplot.show()
