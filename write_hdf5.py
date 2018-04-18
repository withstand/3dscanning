import numpy as np
import h5py
import glob



def create_hdf5(fn='test_data.hdf5'):

    f = h5py.File(fn,'w')

    for file in glob.glob('*.xyz'):
        fn = file.split('.')[0]
        print('Processing ', file)
        f.create_dataset(fn, data=np.genfromtxt(file))

    f.flush()
    f.close()
