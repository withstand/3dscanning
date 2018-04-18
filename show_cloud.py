# -*- coding: utf-8 -*-
"""
Demonstrates use of GLScatterPlotItem with rapidly-updating plots.

"""

## Add path to library (just for examples; you do not need this)

import os.path as p
import sys
import time

import h5py
import numpy as np
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

import write_hdf5

fn = 'tyui'

if len(sys.argv) > 1:
    fn = sys.argv[1]

def get_data_genfromtxt(f):
    return np.genfromtxt(f+'.xyz')  

if not p.exists('test_data.hdf5'):
    t0 = time.clock()
    print('Create test_data.hdf5 from *.xyz')
    write_hdf5.create_hdf5()
    print('Time used ', (time.clock()-t0) , ' seconds.' )

test_data = h5py.File('test_data.hdf5','r')

def get_data_hdf5(f): 
    c = np.asarray(test_data[f])
    return c

def get_test_data_list():
    return [k for k in test_data.keys()]


def make_3d_widget(cloud_data):    
    w = gl.GLViewWidget()
    w.opts['distance'] = 350
    # g = gl.GLGridItem()
    # w.addItem(g)
    sp = gl.GLScatterPlotItem()
    update_3d_scatter(sp, cloud_data)
    # center = cloud_data.mean(axis=0)
    # sp.translate(-center[0], -center[1], -center[2])
    w.addItem(sp)
    return w, sp

def update_3d_scatter(item, data):
    item.resetTransform()
    item.setData(pos = data, size=0.3, color=(0.3, 1, 0.0, 1))
    center = data.mean(axis=0)
    item.translate(-center[0], -center[1], -center[2])
    # item.rotate(angle=180, x=1.0, y=0.0, z= 0.0)

    


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
