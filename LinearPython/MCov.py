import csv
import numpy as np
reader = csv.reader(open('data/covAllcal.csv','r'),delimiter = ",")
i = list(reader)
x = np.array(i).astype('int')
print('matrix x')
print(x)
print('-------')
print('size of x (rows,colums)')
print(x.shape)  #rows,colums
print('-------')
xDimention = x.shape[0]
print('rows')
print(xDimention)
print('-------')
oneM= np.full((xDimention,xDimention), 1) # make One Square Matrix
print('one of matrix')
print(oneM)
print('-------')
xb = (1/int(xDimention))*np.dot(oneM,x) # Xbar
print("Xbar")
print(xb)
print('-------')
# x - xbar
x_xb = x - xb
print('x-xbar')
print(x_xb)
print('-------')
x_xbT = x_xb.T
print('x_xbT')
print(x_xbT)
print('-------')
covX = (1/int(xDimention))*np.dot(x_xbT,x_xb)
print('covariance matrix')
print(covX)
print('-------')
coverCovX = str(covX)
coverCovX = coverCovX.split(" ")
np.savetxt("data/CovFinishAll.csv", covX, delimiter=",",fmt='%.2f')
filename = 'data/covAllcal.csv'








