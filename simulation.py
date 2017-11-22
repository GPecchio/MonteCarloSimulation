import numpy as np
import matplotlib.pyplot as plt
import random
import time

points = 1000
cumSum = 0
n = points

xVal=[]
yVal=[]

start = time.time()
for j in range(1000):
    pointsOut = 0
    pointsIn = 0
    x = [random.random()*8 for i in xrange(n)]
    y = [random.random()*8 for i in xrange(n)]
    
    for i in range(n):
        if (y[i] < ((-(1.2*x[i]-5) ** 2 + 7.5)) and y[i] > (0.8*x[i]-4) ** 2 + 2):
            pointsIn += 1
	    xVal.append(x[i])
	    yVal.append(y[i])
    cumSum += pointsIn
print "done"

f = open('result.txt', 'w')
f.write(str(cumSum/1000)) #remember to do /1000
f.close()
end = time.time()

xRange=[0,9]
yRange=[0,1]
startPoint=xRange[0]
endPoint=xRange[1]

x1=[]
y1=[]
for r1 in np.arange(startPoint,endPoint,.1):
        x1.append(r1)
        y1.append((-(1.2*r1-5) ** 2 + 7.5))

x2=[]
y2=[]
for r2 in np.arange(startPoint,endPoint,.1):
        x2.append(r2)
        y2.append((0.8*r2-4) ** 2 + 2)

plt.ylim([0,9])
plt.plot(x1,y1,'-',color='blue')
plt.plot(x2,y2,'-',color='red')
plt.plot(xVal,yVal,marker='o',linestyle='',color='green')
plt.show()
