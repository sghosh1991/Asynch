import sys,os,time

nprocs = "60"
nrequests = "20"
nruns =  3
nrepetations =  4

test = {}

os.system("python3 -m da /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/ramutex/ramutex.da " + str(nprocs) + " " + str(nrequests))

# for runs in range(nruns):

# 	repetationTimes = []

# 	for rep in range(nrepetations):

		
# 		startRunTime = time.time()
# 		os.system("python3 -m da /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/ramutex/ramutex.da " + str(nprocs) + " " + str(nrequests))
# 		repetationTimes.append(time.time() - startRunTime)

# 	print(repetationTimes)
# 	print(sum(repetationTimes))
# 	print(sum(repetationTimes)/len(repetationTimes))

# 	print("Average Time for run " + str(runs) + " : " + str(sum(repetationTimes)/len(repetationTimes)))
# #os.system("python3 /home/santosh/AsyncSystems/DistAlgo-1.0.0b14/examples/ramutex/test.py " + str(nprocs) + " " + str(nrequests))

print("Back in main:" + str(test))