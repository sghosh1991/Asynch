import matplotlib.pyplot as plt

x = []
y = []

for line in open("/home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/lamutexHW/RT",'r'):

	data = line.split(":")
	x.append(int(data[0]))
	y.append(float(data[1]))

print(x)
print(y)


plt.plot(x,y)
plt.show()