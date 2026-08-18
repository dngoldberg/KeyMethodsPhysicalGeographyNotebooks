import numpy as np
pordata = np.loadtxt('porosity.csv', skiprows=1, delimiter=',')
import matplotlib.pyplot as plt
porcolumn = pordata[:,1]
counts, bins, _ = plt.hist(porcolumn,color='red',bins=12,edgecolor='black',linewidth=2);
plt.xlabel('Porosity (%)')
plt.savefig('histogram.png')
print('program run, figure saved!')