# -*- coding: utf-8 -*-  
""" 
Created on Mon Jan  2 16:09:49 2017 
 
@author: ZQW
"""  
  
import numpy as np  
from sklearn.svm import SVR  
import matplotlib.pyplot as plt  
import sklearn.metrics as metrics
from sklearn.model_selection import learning_curve 

def openfile(firesult,source):
	file1 = open(source)

	while 1:
		lines = file1.readlines(100000)
		if not lines:
			break
		for line in lines:
			firesult.append(line)
	file1.close()
	
firesult = []
openfile(firesult,"index_bitstrng.txt")
openfile(firesult,"index_isqrt.txt")
openfile(firesult,"index_fft.txt")
openfile(firesult,"index_qsort_small.txt")
openfile(firesult,"index_rad2deg.txt")


y = []
x = []
for ins in firesult:
	singleins = ins.split()
	y.append(singleins[14])
	singlefeature = []
	for i in np.arange(2,14,1):
		singlefeature.append(singleins[i])
	singlefeature.append(singleins[15])
	x.append(singlefeature)
	
y = np.array(y,dtype=float)
x = np.array(x)

plt.figure()

svr = SVR(kernel='rbf', C=1e3, gamma=0.1)  
train_sizes, train_scores_svr, test_scores_svr = learning_curve(svr, x[:6787], y[:6787], train_sizes=np.linspace(0.1, 1, 10),  
                   scoring="neg_mean_squared_error", cv=10)  
  
plt.plot(train_sizes, -test_scores_svr.mean(1), 'o-', color="black",  
         label="SVR")  
  
plt.xlabel("Train size")  
plt.ylabel("Mean Squared Error")  
plt.title('Learning curves')  
plt.legend(loc="best")  
  
plt.show()  
  
#fit regression model拟合回归模型  
svr_rbf = SVR(kernel = 'rbf',C = 1e3,gamma = 0.1)  
svr_lin = SVR(kernel = 'linear',C = 1e3)  
svr_poly = SVR(kernel = 'sigmoid',C = 1e3,degree = 2)  
y_rbf = svr_rbf.fit(x,y).predict(x)  
y_lin = svr_lin.fit(x,y).predict(x)  
y_poly = svr_poly.fit(x,y).predict(x)  


y_rbf = np.array(y_rbf,dtype=float)
 
sum_mean=0
sum_mean = float(sum_mean)  
for i in range(len(y_rbf)):  
    sum_mean+=(y_rbf[i]-y[i])**2  
sum_erro= sum_mean/y.size
print(y)
print(y_rbf)
# calculate RMSE by hand  
print(sum_erro) 
corr = np.corrcoef(y_rbf,y)
print(corr)
print(metrics.mean_squared_error(y,y_rbf))
print(metrics.r2_score(y,y_rbf))