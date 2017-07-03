import numpy as np
import matplotlib.pyplot as plt

x = [0.380,0.370,0.449,0.076,0.1,0.089,0.336,0.290,0.400]
benchmark = ["bitstrng","qsort","rad2deg","dijstra","strsearch","patricia","fft","sha","CRC"]
N = len(benchmark)
ind = np.arange(N) 
plt.plot(x,linewidth=2,color='black',marker='^',markerfacecolor='black',markersize=8) 
plt.xlabel('benchmark') 
plt.ylabel('SDC Rate') 
plt.xticks(ind, benchmark)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.title('') 
plt.show()