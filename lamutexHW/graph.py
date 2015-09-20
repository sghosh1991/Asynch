import matplotlib.pyplot as plt

x = []
y = []
z = []

for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/RT_varyProc",'r'):

	data = line.split(":")
	x.append(int(data[0]))
	y.append(float(data[1]))


for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/CT_varyProc",'r'):

	data = line.split(":")
	z.append(float(data[1]))


print("y=" + str(y))
print("z=" + str(z))

plt.plot(x,y)
plt.ylabel('Running Time in seconds')
plt.xlabel('Processes' )
plt.savefig('RT_lamutex.png')

plt.figure()


plt.plot(x,z)
plt.ylabel('CPU Time in seconds')
plt.xlabel('Processes' )
plt.savefig('CT_lamutex.png')