import sys,os,time

nprocs = int(sys.argv[1]) if len(sys.argv) > 2 else 4
nrequests = int(sys.argv[2]) if len(sys.argv) > 2 else 5
nruns = int(sys.argv[3]) if len(sys.argv) > 2 else 1
nruns_c = int(sys.argv[4]) if len(sys.argv) > 2 else 3
nrepetations = int(sys.argv[5]) if len(sys.argv) > 2 else 4


os.system("python3 -m da /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/laMutex.da " + str(nprocs) + " " + str(nrequests))


#======================= Correctness testing





















#=========================Performance Testing=========================

#Vary number of requests


statsAcrossRuns_rt = []
statsAcrossRuns_ct = []
for s in range(nruns_c):
	
	x = []
	y = []

	for numRequests in range(1,nrequests):

		for m in range(1,nrepetations):

			statsRunTime = []
			statsCPUTime = []

			

			startRunTime = time.time()
			startProcessTime = time.process_time()

			os.system("python3 -m da /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/laMutex.da " + str(nprocs) + " " + str(numRequests))

			statsRunTime.append(time.time() - startRunTime)
			statsCPUTime.append(time.process_time() - startProcessTime)

		#print("Stats for " + str(nprocs) + " processes and " + str(numRequests) + " requests")
		
		avgRunTime = sum(statsRunTime)/len(statsRunTime)
		avgCPUTime = sum(statsCPUTime)/len(statsCPUTime)
		
		x.append((numRequests,avgRunTime))
		y.append((numRequests,avgCPUTime))
		


	statsAcrossRuns_rt.append(x)
	statsAcrossRuns_ct.append(y)


#print(statsAcrossRuns_rt)

RTFile = open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/RT_varyReq",'w+')
CTFile = open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/CT_varyReq",'w+')

statsRT = {}
statsCT = {}

for a in statsAcrossRuns_rt:

	for (x,y) in a:

		if(statsRT.__contains__(x)):
			statsRT[x] += y
		else:
			statsRT[x] = y


for a in statsAcrossRuns_ct:

	for (x,y) in a:

		if(statsCT.__contains__(x)):
			statsCT[x] += y
		else:
			statsCT[x] = y


for key, value in statsCT.items():

	statsCT[key] = statsCT[key]/nruns_c
	CTFile.write(str(key) + ":" + str(statsCT[key]) + "\n")


for key, value in statsRT.items():

	statsRT[key] = statsRT[key]/nruns_c
	RTFile.write(str(key) + ":" + str(statsRT[key]) + "\n")



RTFile.close()
CTFile.close()


#============================================================


#vary number of process:


statsAcrossRuns_rt = []
statsAcrossRuns_ct = []
for s in range(nruns_c):
	
	x = []
	y = []

	for num_proc in range(1,nprocs):

		for m in range(1,nrepetations):

			statsRunTime = []
			statsCPUTime = []

			

			startRunTime = time.time()
			startProcessTime = time.process_time()

			os.system("python3 -m da /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/laMutex.da " + str(num_proc) + " " + str(nrequests))

			statsRunTime.append(time.time() - startRunTime)
			statsCPUTime.append(time.process_time() - startProcessTime)

		#print("Stats for " + str(nprocs) + " processes and " + str(numRequests) + " requests")
		
		avgRunTime = sum(statsRunTime)/len(statsRunTime)
		avgCPUTime = sum(statsCPUTime)/len(statsCPUTime)
		
		x.append((num_proc,avgRunTime))
		y.append((num_proc,avgCPUTime))
		


	statsAcrossRuns_rt.append(x)
	statsAcrossRuns_ct.append(y)


#print(statsAcrossRuns_rt)

RTFile = open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/RT_varyProc",'w+')
CTFile = open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/CT_varyProc",'w+')

statsRT = {}
statsCT = {}

for a in statsAcrossRuns_rt:

	for (x,y) in a:

		if(statsRT.__contains__(x)):
			statsRT[x] += y
		else:
			statsRT[x] = y


for a in statsAcrossRuns_ct:

	for (x,y) in a:

		if(statsCT.__contains__(x)):
			statsCT[x] += y
		else:
			statsCT[x] = y


for key, value in statsCT.items():

	statsCT[key] = statsCT[key]/nruns_c
	CTFile.write(str(key) + ":" + str(statsCT[key]) + "\n")


for key, value in statsRT.items():

	statsRT[key] = statsRT[key]/nruns_c
	RTFile.write(str(key) + ":" + str(statsRT[key]) + "\n")



RTFile.close()
CTFile.close()

