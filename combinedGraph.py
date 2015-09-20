import matplotlib.pyplot as plt

x = []
laRT = []
raRT = []
laCT = []
raCT = []

for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/RT_varyProc",'r'):

	data = line.split(":")
	x.append(int(data[0]))
	laRT.append(float(data[1]))


for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/CT_varyProc",'r'):

	data = line.split(":")
	laCT.append(float(data[1]))



for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/ramutex/RT_varyProc",'r'):

	data = line.split(":")
	#x.append(int(data[0]))
	raRT.append(float(data[1]))


for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/ramutex/CT_varyProc",'r'):

	data = line.split(":")
	raCT.append(float(data[1]))








plt.plot(x,raRT)
plt.plot(x,laRT)
plt.ylabel('Running Time in seconds')
plt.xlabel('Processes' )
plt.legend(['RA Mutex', 'LA Mutex'], loc='upper left')
plt.savefig('RT.png')

plt.figure()

plt.plot(x,raCT)
plt.plot(x,laCT)
plt.ylabel('CPU Time in seconds')
plt.xlabel('Processes' )
plt.legend(['RA Mutex', 'LA Mutex'], loc='upper left')
plt.savefig('CT.png')

