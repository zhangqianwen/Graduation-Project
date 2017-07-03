import numpy as np
import matplotlib.pyplot as plt

def SDC100(source,name):
	file = open(source)

	singlefiresult = []
	while 1:
		lines = file.readlines(100000)
		if not lines:
			break
		for line in lines:
			singlefiresult.append(line)
		
	singlenuminstype = {}
	singleSDCnumall = {}
	singleSymptomnumall = {}
	singleMaskednumall = {}
	for ins in singlefiresult:
		singleins = ins.split()
		singleinstype = singleins[2]
		singlewidth = int(singleins[3])
		singleSDCnum = int(singleins[4])
		singleSymptomnum = int(singleins[5])
		singleMaskednum = int(singleins[6])
		
		if singleinstype not in singlenuminstype:
			singlenuminstype[singleinstype] = 1
		else:
			singlenuminstype[singleinstype] += 1
		
		if singleinstype not in singleSDCnumall:
			#singleSDCnumall[singleinstype] = singleSDCnum/singlewidth
			singleSDCnumall[singleinstype] = singleSDCnum/100
		else:
			#singleSDCnumall[singleinstype] += singleSDCnum/singlewidth
			singleSDCnumall[singleinstype] += singleSDCnum/100
			
		if singleinstype not in singleSymptomnumall:
			#singleSymptomnumall[singleinstype] = singleSymptomnum/singlewidth
			singleSymptomnumall[singleinstype] = singleSymptomnum/100
		else:
			#singleSymptomnumall[singleinstype] += singleSymptomnum/singlewidth
			singleSymptomnumall[singleinstype] += singleSymptomnum/100
			
		if singleinstype not in singleMaskednumall:
			#singleMaskednumall[singleinstype] = singleMaskednum/singlewidth
			singleMaskednumall[singleinstype] = singleMaskednum/100
		else:
			#singleMaskednumall[singleinstype] += singleMaskednum/singlewidth
			singleMaskednumall[singleinstype] += singleMaskednum/100
		
	singleSDCpercent = singleSDCnumall
	singleSymptompercent = singleSymptomnumall
	singleMaskedpercent = singleMaskednumall

	for ins in singleSDCpercent:
		singleSDCpercent[ins] = singleSDCpercent[ins]/singlenuminstype[ins]
		singleSymptompercent[ins] = singleSymptompercent[ins]/singlenuminstype[ins]
		singleMaskedpercent[ins] = singleMaskedpercent[ins]/singlenuminstype[ins]

	singleinstypeall = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','getelementptr','sext','bitcast','fptrunc','fpext','sitofp','call']
	singleinstypeallx = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','gete','sext','bitcast','fptrunc','fpext','sitofp','call']
	singleMasked = [0]*len(singleinstypeall)
	singleSymptom = [0]*len(singleinstypeall)
	singleSDC = [0]*len(singleinstypeall)

	for i in range(len(singleinstypeall)):
		if singleinstypeall[i] in singleMaskedpercent:
			singleMasked[i] = singleMaskedpercent[singleinstypeall[i]]
		if singleinstypeall[i] in singleSymptompercent:
			singleSymptom[i] = singleSymptompercent[singleinstypeall[i]]
		if singleinstypeall[i] in singleSDCpercent:
			singleSDC[i] = singleSDCpercent[singleinstypeall[i]]

	N = len(singleinstypeall)
	ind = np.arange(N)    # the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence
	for i in range(len(singleinstypeall)):
		print(singleMasked[i]+singleSDC[i]+singleSymptom[i])
	a = np.array(singleMasked)
	b = np.array(singleSymptom)
	c = np.array(singleSDC)
	p1 = plt.bar(ind, a, width,bottom=0,color='black')
	p2 = plt.bar(ind, b, width,bottom=sum([a]),color='dimgray')
	p3 = plt.bar(ind, c, width,bottom=sum([a, b]),color='darkgray')

	plt.ylabel('result percent')
	plt.title(name)
	plt.xticks(ind, singleinstypeallx)
	plt.yticks(np.arange(0, 1.1, 0.1))
	plt.ylim(0,1)
	plt.legend((p1[0], p2[0],p3[0]), ('Masked', 'Symptom','SDC'))

	plt.show()	

	for singleins in singleSDCpercent:
		singleSDCpercent[singleins] = singleSDCpercent[singleins]/singlenuminstype[singleins]
		singleSymptompercent[singleins] = singleSymptompercent[singleins]/singlenuminstype[singleins]
		singleMaskedpercent[singleins] = singleMaskedpercent[singleins]/singlenuminstype[singleins]

	cyclenum = 0
	for key in singlenuminstype:
		cyclenum += singlenuminstype[key]
	print(cyclenum)
	SDCsum = 0
	for key in singlenuminstype:
		singlenuminstype[key] = singlenuminstype[key]*SDCpercent[key]/cyclenum
		SDCsum += singlenuminstype[key]
		
	print(SDCsum)

def SDCwidth(source,name):
	file = open(source)

	singlefiresult = []
	while 1:
		lines = file.readlines(100000)
		if not lines:
			break
		for line in lines:
			singlefiresult.append(line)
		
	singlenuminstype = {}
	singleSDCnumall = {}
	singleSymptomnumall = {}
	singleMaskednumall = {}
	for ins in singlefiresult:
		singleins = ins.split()
		singleinstype = singleins[2]
		singlewidth = int(singleins[3])
		singleSDCnum = int(singleins[4])
		singleSymptomnum = int(singleins[5])
		singleMaskednum = int(singleins[6])
		
		if singleinstype not in singlenuminstype:
			singlenuminstype[singleinstype] = 1
		else:
			singlenuminstype[singleinstype] += 1
		
		if singleinstype not in singleSDCnumall:
			singleSDCnumall[singleinstype] = singleSDCnum/singlewidth
			#singleSDCnumall[singleinstype] = singleSDCnum/100
		else:
			singleSDCnumall[singleinstype] += singleSDCnum/singlewidth
			#singleSDCnumall[singleinstype] += singleSDCnum/100
			
		if singleinstype not in singleSymptomnumall:
			singleSymptomnumall[singleinstype] = singleSymptomnum/singlewidth
			#singleSymptomnumall[singleinstype] = singleSymptomnum/100
		else:
			singleSymptomnumall[singleinstype] += singleSymptomnum/singlewidth
			#singleSymptomnumall[singleinstype] += singleSymptomnum/100
			
		if singleinstype not in singleMaskednumall:
			singleMaskednumall[singleinstype] = singleMaskednum/singlewidth
			#singleMaskednumall[singleinstype] = singleMaskednum/100
		else:
			singleMaskednumall[singleinstype] += singleMaskednum/singlewidth
			#singleMaskednumall[singleinstype] += singleMaskednum/100
		
	singleSDCpercent = singleSDCnumall
	singleSymptompercent = singleSymptomnumall
	singleMaskedpercent = singleMaskednumall

	for ins in singleSDCpercent:
		singleSDCpercent[ins] = singleSDCpercent[ins]/singlenuminstype[ins]
		singleSymptompercent[ins] = singleSymptompercent[ins]/singlenuminstype[ins]
		singleMaskedpercent[ins] = singleMaskedpercent[ins]/singlenuminstype[ins]

	singleinstypeall = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','getelementptr','sext','bitcast','fptrunc','fpext','sitofp','call']
	singleinstypeallx = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','gete','sext','bitcast','fptrunc','fpext','sitofp','call']
	singleMasked = [0]*len(singleinstypeall)
	singleSymptom = [0]*len(singleinstypeall)
	singleSDC = [0]*len(singleinstypeall)

	for i in range(len(singleinstypeall)):
		if singleinstypeall[i] in singleMaskedpercent:
			singleMasked[i] = singleMaskedpercent[singleinstypeall[i]]
		if singleinstypeall[i] in singleSymptompercent:
			singleSymptom[i] = singleSymptompercent[singleinstypeall[i]]
		if singleinstypeall[i] in singleSDCpercent:
			singleSDC[i] = singleSDCpercent[singleinstypeall[i]]

	N = len(singleinstypeall)
	ind = np.arange(N)    # the x locations for the groups
	width = 0.35       # the width of the bars: can also be len(x) sequence
	a = np.array(singleMasked)
	b = np.array(singleSymptom)
	c = np.array(singleSDC)
	p1 = plt.bar(ind, a, width,bottom=0,color='black')
	p2 = plt.bar(ind, b, width,bottom=sum([a]),color='dimgray')
	p3 = plt.bar(ind, c, width,bottom=sum([a, b]),color='darkgray')

	plt.ylabel('result percent')
	plt.title(name)
	plt.xticks(ind, singleinstypeallx)
	plt.yticks(np.arange(0, 1.1, 0.1))
	plt.legend((p1[0], p2[0],p3[0]), ('Masked', 'Symptom','SDC'))

	plt.show()	

	for singleins in singleSDCpercent:
		singleSDCpercent[singleins] = singleSDCpercent[singleins]/singlenuminstype[singleins]
		singleSymptompercent[singleins] = singleSymptompercent[singleins]/singlenuminstype[singleins]
		singleMaskedpercent[singleins] = singleMaskedpercent[singleins]/singlenuminstype[singleins]

	cyclenum = 0
	for key in singlenuminstype:
		cyclenum += singlenuminstype[key]
	print(cyclenum)
	SDCsum = 0
	for key in singlenuminstype:
		singlenuminstype[key] = singlenuminstype[key]*SDCpercent[key]/cyclenum
		SDCsum += singlenuminstype[key]
		
	print(SDCsum)		

file = open("all1.txt")

firesult = []
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        firesult.append(line)
	
numinstype = {}
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
	
	if instype not in numinstype:
		numinstype[instype] = 1
	else:
		numinstype[instype] += 1
	
	if instype not in SDCnumall:
		SDCnumall[instype] = SDCnum/width
		#SDCnumall[instype] = SDCnum/100
	else:
		SDCnumall[instype] += SDCnum/width
		#SDCnumall[instype] += SDCnum/100
		
	if instype not in Symptomnumall:
		Symptomnumall[instype] = Symptomnum/width
		#Symptomnumall[instype] = Symptomnum/100
	else:
		Symptomnumall[instype] += Symptomnum/width
		#Symptomnumall[instype] += Symptomnum/100
		
	if instype not in Maskednumall:
		Maskednumall[instype] = Maskednum/width
		#Maskednumall[instype] = Maskednum/100
	else:
		Maskednumall[instype] += Maskednum/width
		#Maskednumall[instype] += Maskednum/100
	
SDCpercent = SDCnumall
Symptompercent = Symptomnumall
Maskedpercent = Maskednumall

for ins in SDCpercent:
	SDCpercent[ins] = SDCpercent[ins]/numinstype[ins]
	Symptompercent[ins] = Symptompercent[ins]/numinstype[ins]
	Maskedpercent[ins] = Maskedpercent[ins]/numinstype[ins]

instypeall = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','getelementptr','sext','bitcast','fptrunc','fpext','sitofp','call']
instypeallx = ['fadd','fsub','fmul','fdiv','add','sub','mul','and','or','shl','lshr','shr','icmp','fcmp','phi','load','alloca','gete','sext','bitcast','fptrunc','fpext','sitofp','call']
Masked = [0]*len(instypeall)
Symptom = [0]*len(instypeall)
SDC = [0]*len(instypeall)

for i in range(len(instypeall)):
	if instypeall[i] in Maskedpercent:
		Masked[i] = Maskedpercent[instypeall[i]]
	if instypeall[i] in Symptompercent:
		Symptom[i] = Symptompercent[instypeall[i]]
	if instypeall[i] in SDCpercent:
		SDC[i] = SDCpercent[instypeall[i]]

N = len(instypeall)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
a = np.array(Masked)
b = np.array(Symptom)
c = np.array(SDC)
p1 = plt.bar(ind, a, width,bottom=0,color='black')
p2 = plt.bar(ind, b, width,bottom=sum([a]),color='dimgray')
p3 = plt.bar(ind, c, width,bottom=sum([a, b]),color='darkgray')

plt.ylabel('result percent')
plt.title('all')
plt.xticks(ind, instypeallx)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0],p3[0]), ('Masked', 'Symptom','SDC'))

plt.show()	

SDC100("C:\\Users\\cheven\\Desktop\\exp\\data\\dijkstra_small\\result\\all1.txt","dijkstra")
SDCwidth("C:\\Users\\cheven\\Desktop\\exp\\data\\isqrt\\result\\cycle_result.txt","isqrt")
SDCwidth("C:\\Users\\cheven\\Desktop\\exp\\data\\fft\\result\\cycle_result.txt","fft")
SDCwidth("C:\\Users\\cheven\\Desktop\\exp\\data\\qsort_small\\result\\cycle_result.txt","qsort")
SDCwidth("C:\\Users\\cheven\\Desktop\\exp\\data\\rad2deg\\result\\cycle_result.txt","rad2deg")
SDCwidth("C:\\Users\\cheven\\Desktop\\exp\\data\\bitstrng\\result\\cycle_result.txt","bitstrng")