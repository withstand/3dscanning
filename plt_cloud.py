import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import sys

fn = 'zxcvbbb.xyz'


if len(sys.argv) > 1:
	fn = sys.argv[1]

cloud = np.genfromtxt(fn)


fig = plt.figure()

ax = fig.gca(projection='3d')

ax.scatter3D(cloud[:,0], cloud[:,1], cloud[:,2])



plt.show()

