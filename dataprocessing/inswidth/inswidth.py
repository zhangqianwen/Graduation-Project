import numpy as np
import matplotlib.pyplot as plt


file = open("all1.txt")

firesult = []
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        firesult.append(line)
		
numinswidth = {}
SDCnumall = {}
Symptomnumall = {}
Maskednumall = {}
for ins in firesult:
	singleins = ins.split()
	instype = singleins[2]
	width = int(singleins[3])
	SDCnum = int(singleins[4])
	Symptomnum = int(singleins[5])
	Maskednum = int(singleins[6])
	
	if width not in numinswidth:
		numinswidth[width] = 1
	else:
		numinswidth[width] += 1
	
	if width not in SDCnumall:
		SDCnumall[width] = SDCnum/width
	else:
		SDCnumall[width] += SDCnum/width
		
	if width not in Symptomnumall:
		Symptomnumall[width] = Symptomnum/width
	else:
		Symptomnumall[width] += Symptomnum/width
		
	if width not in Maskednumall:
		Maskednumall[width] = Maskednum/width
	else:
		Maskednumall[width] += Maskednum/width
	
SDCpercent = SDCnumall
Symptompercent = Symptomnumall
Maskedpercent = Maskednumall

for width in SDCpercent:
	SDCpercent[width] = SDCpercent[width]/numinswidth[width]
	Symptompercent[width] = Symptompercent[width]/numinswidth[width]
	Maskedpercent[width] = Maskedpercent[width]/numinswidth[width]

print(SDCpercent)	
print(Symptompercent)
print(Maskedpercent)

x = []
y = []
for key in [1,8,32,64]:
	y.append(SDCpercent[key])
	x.append(key)
plt.plot(x,y,linewidth=2,color='black',marker='^',markerfacecolor='black',markersize=8) 
plt.xlabel('BITS') 
plt.ylabel('Average SDC Rate') 
plt.title('') 
plt.show()