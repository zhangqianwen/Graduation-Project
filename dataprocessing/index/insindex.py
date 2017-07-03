import os

def insarray(instype,index,category,categoryarray):
	if index not in categoryarray:
		if instype in category:
			categoryarray[index] = 1
		else:
			categoryarray[index] = 0
			
def resultpercent(width,index,indextoresult,resultnum):
	if index not in indextoresult:
		#indextoresult[index] = resultnum/width
		indextoresult[index] = resultnum/100
		
	else:
		#indextoresult[index] += resultnum/width
		indextoresult[index] += resultnum/100
		
def getfeature(source,target):
	file1 = open(source)

	firesult = []
	while 1:
		lines = file1.readlines(100000)
		if not lines:
			break
		for line in lines:
			firesult.append(line)
	file1.close()

	indextocycle={}	
	indextotype = {}
	indextoSDC = {}
	indextoSymptom = {}
	indextoMasked = {}
	indextowidth = {}
	normalcycle = {}
	
	
	floatbinary = {'fadd','fsub','fmul','fdiv'}
	floatbinaryarray = {}
	intbinary = {'add','sub','mul'}
	intbinaryarray = {}
	logical = {'and','or'}
	logicalarray = {}
	cmp = {'icmp','fcmp'}
	cmparray = {}
	call = {'call'}
	callarray = {}
	shift = {'shl','lshr','shr'}
	shiftarray = {}
	trans = {'bitcast','fptrunc','fpext','sitofp','sext'}
	transarray = {}
	memory = {'alloca','getelementptr'}
	memoryarray = {}
	load = {'load'}
	loadarray = {}
	phi = {'phi'}
	phiarray = {}


	for ins in firesult:
		singleins = ins.split()
		index = singleins[1]
		instype = singleins[2]
		width = int(singleins[3])
		SDCnum = int(singleins[4])
		Symptomnum = int(singleins[5])
		Maskednum = int(singleins[6])
		
		if index not in indextocycle:
			indextocycle[index] = 1
			normalcycle[index] = 1
		else:
			indextocycle[index] += 1
			normalcycle[index] += 1
			
		if index not in indextowidth:
			indextowidth[index] = round(width/64,2)
			
		if index not in indextotype:
			indextotype[index] = instype
			
		insarray(instype,index,floatbinary,floatbinaryarray)
		insarray(instype,index,intbinary,intbinaryarray)
		insarray(instype,index,logical,logicalarray)
		insarray(instype,index,cmp,cmparray)
		insarray(instype,index,call,callarray)
		insarray(instype,index,shift,shiftarray)
		insarray(instype,index,trans,transarray)
		insarray(instype,index,memory,memoryarray)
		insarray(instype,index,load,loadarray)
		insarray(instype,index,phi,phiarray)
		
		
		resultpercent(width,index,indextoSDC,SDCnum)
		resultpercent(width,index,indextoSymptom,Symptomnum)
		resultpercent(width,index,indextoMasked,Maskednum)

		
	SDCpercent = indextoSDC
	Symptompercent = indextoSymptom
	Maskedpercent = indextoMasked

	for index in SDCpercent:
		SDCpercent[index] = round(SDCpercent[index]/indextocycle[index],2)
		Symptompercent[index] = round(Symptompercent[index]/indextocycle[index],2)
		Maskedpercent[index] = round(Maskedpercent[index]/indextocycle[index],2)

	os.remove(target)
	f = open(target,"a+")
	relstr = '{0: <5}'.format("index")
	relstr = relstr+'{0: <15}'.format("type")
	relstr = relstr+'{0: <8}'.format("float")
	relstr = relstr+'{0: <8}'.format("int")
	relstr = relstr+'{0: <8}'.format("logical")
	relstr = relstr+'{0: <8}'.format("cmp")
	relstr = relstr+'{0: <8}'.format("call")
	relstr = relstr+'{0: <8}'.format("shift")
	relstr = relstr+'{0: <8}'.format("trans")
	relstr = relstr+'{0: <8}'.format("memory")
	relstr = relstr+'{0: <8}'.format("load")
	relstr = relstr+'{0: <8}'.format("phi")
	relstr = relstr+'{0: <8}'.format("width")
	relstr = relstr+'{0: <8}'.format("cycle")
	relstr = relstr+'{0: <8}'.format("SDC")
	relstr = relstr+'{0: <8}'.format("Symptom")
	relstr = relstr+'{0: <8}'.format("Masked")
	
	f.write(relstr+'\n')
	
	cyclesum = 0
	for key in indextocycle:
		cyclesum += indextocycle[key]
	
	SDCpercentall = 0
	for key in normalcycle:
		SDCpercentall += normalcycle[key] * SDCpercent[key] / cyclesum
		normalcycle[key] = round(normalcycle[key] / cyclesum,3)
	print(cyclesum)
	print(target[6:-4]+"---"+str(SDCpercentall))
	for index in indextotype:
		relstr = '{0: <5}'.format(index)
		relstr = relstr+'{0: <15}'.format(indextotype[index])
		relstr = relstr+'{0: <8}'.format(floatbinaryarray[index])
		relstr = relstr+'{0: <8}'.format(intbinaryarray[index])
		relstr = relstr+'{0: <8}'.format(logicalarray[index])
		relstr = relstr+'{0: <8}'.format(cmparray[index])
		relstr = relstr+'{0: <8}'.format(callarray[index])
		relstr = relstr+'{0: <8}'.format(shiftarray[index])
		relstr = relstr+'{0: <8}'.format(transarray[index])
		relstr = relstr+'{0: <8}'.format(memoryarray[index])
		relstr = relstr+'{0: <8}'.format(loadarray[index])
		relstr = relstr+'{0: <8}'.format(phiarray[index])
		relstr = relstr+'{0: <8}'.format(indextowidth[index])
		relstr = relstr+'{0: <8}'.format(normalcycle[index])
		relstr = relstr+'{0: <8}'.format(SDCpercent[index])
		if SDCpercent[index] == 0:
			relstr = relstr+'{0: <8}'.format(0)
		else:
			relstr = relstr+'{0: <8}'.format(1)
		relstr = relstr+'{0: <8}'.format(Symptompercent[index])
		relstr = relstr+'{0: <8}'.format(Maskedpercent[index])
		f.write(relstr+'\n')
		
	f.close()
	
#getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\bitstrng\\result\\cycle_result.txt","index_bitstrng.txt")
#getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\isqrt\\result\\cycle_result.txt","index_isqrt.txt")
#getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\fft\\result\\cycle_result.txt","index_fft.txt")
#getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\qsort_small\\result\\cycle_result.txt","index_qsort_small.txt")
#getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\rad2deg\\result\\cycle_result.txt","index_rad2deg.txt")
getfeature("C:\\Users\\cheven\\Desktop\\exp\\data\\dijkstra_small\\result\\all1.txt","index_dijkstra.txt")


